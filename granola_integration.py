"""
Granola integration for automatic note import and AI insights.
"""
import requests
from typing import Dict, Optional
from config import Config
from notion_integration import NotionIntegration
import openai


class GranolaIntegration:
    """Handle Granola API operations and note processing."""
    
    def __init__(self):
        """Initialize Granola client."""
        self.api_key = Config.GRANOLA_API_KEY
        self.base_url = "https://api.granola.ai"  # Placeholder - verify actual URL
        self.notion = NotionIntegration() if Config.NOTION_API_KEY else None
    
    def get_meeting_notes(self, folder_id: Optional[str] = None) -> list:
        """
        Retrieve meeting notes from Granola.
        
        Args:
            folder_id: Optional folder ID to filter notes
            
        Returns:
            List of meeting note dictionaries
        """
        if not self.api_key:
            raise ValueError("GRANOLA_API_KEY not configured")
        
        headers = {
            "Authorization": f"Bearer {self.api_key}",
        }
        
        url = f"{self.base_url}/notes"
        if folder_id:
            url += f"?folder_id={folder_id}"
        
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            return response.json().get("notes", [])
        else:
            raise Exception(f"Granola API error: {response.status_code} - {response.text}")
    
    def get_transcript(self, note_id: str) -> str:
        """
        Get full transcript for a meeting note.
        
        Args:
            note_id: Granola note ID
            
        Returns:
            Full transcript text
        """
        if not self.api_key:
            raise ValueError("GRANOLA_API_KEY not configured")
        
        headers = {
            "Authorization": f"Bearer {self.api_key}",
        }
        
        response = requests.get(
            f"{self.base_url}/notes/{note_id}/transcript",
            headers=headers
        )
        
        if response.status_code == 200:
            return response.json().get("transcript", "")
        else:
            raise Exception(f"Granola API error: {response.status_code} - {response.text}")
    
    def extract_company_name(self, meeting_title: str, participants: list) -> Optional[str]:
        """
        Extract company name from meeting title or participants.
        
        Args:
            meeting_title: Title of the meeting
            participants: List of participant names
            
        Returns:
            Company name if found, None otherwise
        """
        # Simple extraction logic - can be enhanced with fuzzy matching
        # Look for common patterns in meeting titles
        title_lower = meeting_title.lower()
        
        # Check if title contains company name patterns
        # This is a placeholder - actual implementation would use
        # fuzzy matching against Notion company database
        
        return None
    
    def generate_key_insights(self, transcript: str) -> Dict:
        """
        Generate key insights from meeting transcript using LLM.
        
        Args:
            transcript: Full meeting transcript
            
        Returns:
            Dictionary with key insights, takeaways, metrics, etc.
        """
        if not Config.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY not configured for insights generation")
        
        client = openai.OpenAI(api_key=Config.OPENAI_API_KEY)
        
        prompt = f"""Analyze the following meeting transcript and extract key insights.

Transcript:
{transcript}

Please provide:
1. Three main takeaways (bullet points)
2. Key metrics discussed (if any)
3. Action items mentioned
4. Any concerns or challenges raised

Format as JSON with keys: takeaways, metrics, action_items, concerns."""

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an assistant that extracts key insights from meeting transcripts. Always respond with valid JSON."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )
        
        import json
        try:
            insights = json.loads(response.choices[0].message.content)
            return insights
        except json.JSONDecodeError:
            # Fallback if JSON parsing fails
            return {
                "takeaways": [response.choices[0].message.content],
                "metrics": [],
                "action_items": [],
                "concerns": []
            }
    
    def process_and_import_note(
        self,
        note_id: str,
        company_name: Optional[str] = None
    ) -> Dict:
        """
        Process a Granola note and import it to Notion.
        
        Args:
            note_id: Granola note ID
            company_name: Optional company name (if not provided, will try to extract)
            
        Returns:
            Dictionary with processing results
        """
        # Get transcript
        transcript = self.get_transcript(note_id)
        
        # Get note metadata
        notes = self.get_meeting_notes()
        note_data = next((n for n in notes if n["id"] == note_id), None)
        
        if not note_data:
            raise ValueError(f"Note {note_id} not found")
        
        # Extract company name if not provided
        if not company_name:
            company_name = self.extract_company_name(
                note_data.get("title", ""),
                note_data.get("participants", [])
            )
        
        if not company_name:
            raise ValueError("Could not determine company name")
        
        # Find company in Notion
        company_page = self.notion.get_company_by_name(company_name)
        if not company_page:
            raise ValueError(f"Company '{company_name}' not found in Notion")
        
        # Generate insights
        insights = self.generate_key_insights(transcript)
        
        # Format note content
        note_content = f"""**Full Transcript:**
{transcript}

**Key Insights:**
{chr(10).join(f"- {takeaway}" for takeaway in insights.get("takeaways", []))}

**Metrics Discussed:**
{chr(10).join(f"- {metric}" for metric in insights.get("metrics", []))}

**Action Items:**
{chr(10).join(f"- {item}" for item in insights.get("action_items", []))}

**Concerns:**
{chr(10).join(f"- {concern}" for concern in insights.get("concerns", []))}
"""
        
        # Add to Notion
        self.notion.add_granola_note(
            company_page["id"],
            note_content,
            note_data.get("title", "Meeting Notes")
        )
        
        return {
            "success": True,
            "company_name": company_name,
            "insights": insights
        }

