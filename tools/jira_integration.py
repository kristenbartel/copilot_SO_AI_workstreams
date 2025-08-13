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
    url = f"{JIRA_BASE_URL}/rest/api/3/issue/bulk"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    auth = (JIRA_EMAIL, JIRA_API_TOKEN)

    # Wrap issues in the required Jira format
    data = { "issueUpdates": issue_payloads }

    response = requests.post(url, headers=headers, auth=auth, json=data)
    
    if response.status_code == 201:
        print("✅ Issues successfully created.")
        return response.json()
    else:
        print("❌ Failed to create issues.")
        print(response.status_code, response.text)
        return None
