"""
Setup OAuth for Google Drive using personal Google account.
This will authorize access to hmikaeltewolde@gmail.com's Google Drive.
"""
import os
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# Scopes needed for Google Drive
SCOPES = ['https://www.googleapis.com/auth/drive.file']

def setup_oauth():
    """Set up OAuth for personal Google account."""
    creds = None
    
    # Check if we already have a token
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    # If there are no (valid) credentials available, let the user log in
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # You'll need to create OAuth credentials in Google Cloud Console
            # For now, we'll use a manual flow
            print("=" * 60)
            print("Google Drive OAuth Setup")
            print("=" * 60)
            print("\nTo use your personal Google account (hmikaeltewolde@gmail.com):")
            print("\n1. Go to: https://console.cloud.google.com/")
            print("2. Create a new project or select existing one")
            print("3. Enable Google Drive API")
            print("4. Go to 'Credentials' → 'Create Credentials' → 'OAuth client ID'")
            print("5. Choose 'Desktop app'")
            print("6. Download the credentials JSON file")
            print("7. Save it as 'credentials.json' in this directory")
            print("\nThen run this script again.")
            print("=" * 60)
            
            # Check if credentials.json exists
            if os.path.exists('credentials.json'):
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES
                )
                creds = flow.run_local_server(port=0)
            else:
                print("\n⚠️  'credentials.json' not found. Please create it first.")
                return None
    
    # Save the credentials for the next run
    with open('token.json', 'w') as token:
        token.write(creds.to_json())
    
    print("\n✅ OAuth setup complete!")
    print(f"✅ Authorized for: {creds.id_token.get('email') if hasattr(creds, 'id_token') and creds.id_token else 'Google Drive'}")
    print("✅ Token saved to token.json")
    print("\nFiles will now upload to your personal Google Drive!")
    
    return creds

if __name__ == '__main__':
    setup_oauth()


