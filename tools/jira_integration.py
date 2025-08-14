import requests
import os
import json
from dotenv import load_dotenv


# Load secrets from .env in the project root
env_path = os.path.join(os.path.dirname(__file__), '../.env')
load_dotenv(dotenv_path=env_path)

JIRA_BASE_URL = os.getenv("JIRA_BASE_URL")
JIRA_EMAIL = os.getenv("JIRA_EMAIL")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")
JIRA_PROJECT_KEY = os.getenv("JIRA_PROJECT_KEY")

def create_issues_bulk(issue_payloads):
    """
    Create multiple issues in Jira using bulk API
    Returns a mapping of story summaries to Jira issue keys
    """
    url = f"{JIRA_BASE_URL}/rest/api/3/issue/bulk"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    auth = (JIRA_EMAIL, JIRA_API_TOKEN)

    # Prepare the bulk create payload
    bulk_data = {
        "issueUpdates": []
    }
    
    for payload in issue_payloads:
        bulk_data["issueUpdates"].append({
            "fields": payload["fields"]
        })

    response = requests.post(url, headers=headers, auth=auth, json=bulk_data)
    
    if response.status_code == 201:
        result = response.json()
        print(f"✅ {len(result.get('issues', []))} issues successfully created.")
        
        # Create mapping of story summary to issue key
        story_mappings = []
        for i, issue_data in enumerate(result.get('issues', [])):
            if i < len(issue_payloads):
                story_summary = issue_payloads[i]['fields']['summary']
                issue_key = issue_data.get('key', 'Unknown')
                story_mappings.append({
                    "story_name": story_summary,
                    "issue_key": issue_key,
                    "issue_url": f"{JIRA_BASE_URL}/browse/{issue_key}"
                })
        
        return {
            "success": True,
            "story_mappings": story_mappings,
            "raw_response": result
        }
    else:
        print("❌ Failed to create issues.")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
        return {
            "success": False,
            "error": f"HTTP {response.status_code}: {response.text}",
            "story_mappings": []
        }

def load_jira_payload(file_path="../outputs/06_jira_payload.json"):
    """Load Jira payload from JSON file"""
    try:
        full_path = os.path.join(os.path.dirname(__file__), file_path)
        with open(full_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"❌ Jira payload file not found: {file_path}")
        return None
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON in payload file: {e}")
        return None

def create_stories_from_payload():
    """
    Load the Jira payload and create stories in Jira
    Returns story name to issue number mappings
    """
    print("🚀 Loading Jira payload and creating stories...")
    
    # Load the payload
    payload = load_jira_payload()
    if not payload:
        return None
    
    print(f"📋 Found {len(payload)} stories to create")
    
    # Create issues in Jira
    result = create_issues_bulk(payload)
    
    if result["success"]:
        print("\n📊 Story Creation Summary:")
        print("=" * 50)
        for mapping in result["story_mappings"]:
            print(f"✅ {mapping['story_name']} → {mapping['issue_key']}")
            
        return result["story_mappings"]
    else:
        print(f"\n❌ Failed to create stories: {result['error']}")
        return None

if __name__ == "__main__":
    # Run the story creation process
    mappings = create_stories_from_payload()
    
    if mappings:
        # Save mappings to file
        mappings_file = os.path.join(os.path.dirname(__file__), "../outputs/07_jira_mappings.json")
        with open(mappings_file, 'w', encoding='utf-8') as f:
            json.dump({
                "created_date": "2025-08-14",
                "total_stories": len(mappings),
                "story_mappings": mappings
            }, f, indent=2, ensure_ascii=False)
        print(f"\n💾 Story mappings saved to: 07_jira_mappings.json")
    else:
        print("\n❌ No story mappings to save")
