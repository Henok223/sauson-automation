# Slauson & Co. Portfolio Onboarding Automation

Automation suite for streamlining portfolio company onboarding across Canva, DocSend, and Notion.

## Features

1. **Portfolio Onboarding Automation**
   - Notion form submission triggers automation
   - Automatic Canva slide generation with image processing
   - DocSend deck updates
   - Notion database and folder creation

2. **Granola Notes Integration** (Future)
   - Automatic note import to Notion
   - AI-generated key insights

## Setup

1. Create virtual environment (recommended):
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up environment variables:
```bash
cp .env.example .env
# Fill in your API keys
```

3. Run the automation:
```bash
python main.py
```

Or start the webhook server:
```bash
./start_server.sh
# Or manually:
source venv/bin/activate
python webhook_listener.py
```

## Configuration

- `NOTION_API_KEY`: Your Notion integration token
- `CANVA_API_KEY`: Your Canva API key
- `DOCSEND_API_KEY`: Your DocSend API key
- `REMOVEBG_API_KEY`: Remove.bg API key for background removal
- `OPENAI_API_KEY`: OpenAI API key for LLM insights (optional)

## Project Structure

```
slauson-automation/
├── main.py                 # Main orchestrator
├── config.py               # Configuration management
├── notion_integration.py   # Notion API wrapper
├── canva_integration.py    # Canva API wrapper
├── docsend_integration.py  # DocSend API wrapper
├── image_processor.py      # Image processing utilities
├── granola_integration.py  # Granola integration (future)
└── utils.py                # Helper functions
```

