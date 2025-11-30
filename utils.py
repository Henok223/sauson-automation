"""
Utility functions for the automation suite.
"""
import re
from typing import Optional, List, Dict


def extract_company_name_from_title(title: str, known_companies: List[str]) -> Optional[str]:
    """
    Extract company name from meeting title using fuzzy matching.
    
    Args:
        title: Meeting title
        known_companies: List of known company names from Notion
        
    Returns:
        Best matching company name or None
    """
    title_lower = title.lower()
    
    # Simple matching - can be enhanced with fuzzywuzzy or similar
    for company in known_companies:
        company_lower = company.lower()
        if company_lower in title_lower or title_lower in company_lower:
            return company
    
    return None


def format_date_for_notion(date_str: str) -> str:
    """
    Format date string for Notion API.
    
    Args:
        date_str: Date in various formats
        
    Returns:
        ISO format date string
    """
    # Handle common date formats
    # This is simplified - in production, use dateutil.parser
    return date_str


def sanitize_filename(filename: str) -> str:
    """
    Sanitize filename for file operations.
    
    Args:
        filename: Original filename
        
    Returns:
        Sanitized filename
    """
    # Remove invalid characters
    sanitized = re.sub(r'[<>:"/\\|?*]', '_', filename)
    return sanitized[:255]  # Limit length


def validate_company_data(data: Dict) -> List[str]:
    """
    Validate company data before processing.
    
    Args:
        data: Company data dictionary
        
    Returns:
        List of validation errors (empty if valid)
    """
    errors = []
    required_fields = ["name"]
    
    for field in required_fields:
        if field not in data or not data[field]:
            errors.append(f"Missing required field: {field}")
    
    return errors

