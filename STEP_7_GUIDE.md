# BacklogBuilderCopilot - Step 7 Implementation Guide

## Overview
Step 7 integrates with Jira to create stories and generates story name → issue key mappings.

## Prerequisites

### Required Python Packages
```bash
pip install requests python-dotenv
```

### Environment Setup
Ensure your `.env` file contains:
```env
JIRA_BASE_URL=https://your-instance.atlassian.net
JIRA_EMAIL=your-email@domain.com
JIRA_API_TOKEN=your-api-token
JIRA_PROJECT_KEY=YOUR-PROJECT-KEY
```

## Execution Steps

### 1. Validate Setup
```bash
cd /Users/bartel/Projects/copilot_SO_AI_workstreams
python3 -c "
import os
from dotenv import load_dotenv
load_dotenv()
required_vars = ['JIRA_BASE_URL', 'JIRA_EMAIL', 'JIRA_API_TOKEN', 'JIRA_PROJECT_KEY']
missing = [var for var in required_vars if not os.getenv(var)]
if missing:
    print(f'❌ Missing environment variables: {missing}')
else:
    print('✅ All Jira environment variables are configured')
"
```

### 2. Execute Step 7
```bash
python3 tools/jira_integration.py
```

### 3. Verify Output
The script will create `outputs/07_jira_mappings.json` containing:
- Story name → Jira issue key mappings
- Creation summary and metadata
- Project statistics and next steps

## Expected Output Structure

```json
{
  "created_date": "2025-08-14",
  "total_stories": 21,
  "story_mappings": [
    {
      "story_name": "User login with email and password",
      "issue_key": "SCRUM-123",
      "issue_url": "https://kristenbartel.atlassian.net/browse/SCRUM-123"
    }
  ]
}
```

## Error Handling

- **Missing Dependencies**: Install required packages
- **Authentication Errors**: Verify Jira credentials
- **API Rate Limits**: The script handles bulk creation efficiently
- **Network Issues**: The script provides detailed error messages

## Integration with Workflow

This step completes the BacklogBuilderCopilot workflow by:
1. Creating actual Jira stories from the generated backlog
2. Providing trackable story mappings for project management
3. Enabling immediate development work to begin

## Next Steps After Step 7

1. Review created stories in your Jira project
2. Assign stories to sprints based on dependencies
3. Begin development work following the critical path
4. Use the story mappings for progress tracking
