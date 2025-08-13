# Running the Copilot.yaml Workflow

## Overview
The `copilot.yaml` file defines a 6-step workflow called "BacklogBuilderCopilot" that generates a complete Agile backlog from Statement of Work (SOW) and High-Level Design (HLD) documents.

## Quick Start
To run the copilot.yaml workflow:

```bash
python run_copilot.py
```

Or with specific options:
```bash
python run_copilot.py --workflow copilot.yaml --verbose
```

## Prerequisites
1. **Python 3.7+** installed on your system
2. **Required Python packages** (install with: `pip install -r requirements.txt`)
   - PyYAML>=6.0

## Workflow Steps

The workflow processes your input files through these sequential steps:

1. **Extract Deliverables** (`./prompts/01_extract_deliverables.md`)
   - Analyzes SOW and HLD to identify key deliverables
   - Categorizes them as backend, infra, or integration
   - Defines success criteria for each deliverable

2. **Map to Epics** (`./prompts/02_map_to_epics.md`)
   - Converts deliverables into Jira-style epics
   - Adds complexity estimates and labels
   - Creates outcome-oriented epic summaries

3. **Generate User Stories** (`./prompts/03_generate_stories.md`)
   - Creates detailed user stories for each epic
   - Assigns story points and acceptance criteria
   - Follows standard "As a... I want... So that..." format

4. **Add Acceptance Criteria** (`./prompts/04_generate_acceptance_criteria.md`)
   - Enhances stories with detailed acceptance criteria
   - Uses Given-When-Then format for clarity
   - Includes test scenarios and edge cases

5. **Infer Dependencies** (`./prompts/05_infer_dependencies.md`)
   - Analyzes and maps dependencies between stories
   - Identifies blocking relationships
   - Creates dependency graphs for project planning

6. **Format for Jira** (`./prompts/06_review_and_format_for_jira.md`)
   - Converts the backlog into Jira-compatible format
   - Generates JSON payloads for Jira API
   - Creates CSV format for bulk import

## Input Files

The workflow expects these input files in the `inputs/` directory:

### `inputs/sow.md` - Statement of Work
Should contain:
- Project overview and objectives
- Scope of work and requirements
- Technical specifications
- Success criteria and timeline
- Integration requirements

### `inputs/hld.md` - High-Level Design  
Should contain:
- System architecture overview
- Technology stack decisions
- Component interactions
- Security considerations
- Performance requirements

## Output Files

After execution, you'll get:

### `workflow_results.json`
Complete workflow results including:
- All step outputs in structured format
- Input context and processing history
- Generated deliverables, epics, and stories
- Jira-ready payloads and CSV data

## Example Usage

```bash
# Run with default inputs (inputs/sow.md and inputs/hld.md)
python run_copilot.py

# Run with verbose output
python run_copilot.py --verbose

# Specify a different workflow file
python run_copilot.py --workflow my_custom_copilot.yaml
```

## Integration with Jira

The workflow generates Jira-ready output that can be used with the included `tools/jira_integration.py` script:

1. Set up your Jira credentials in a `.env` file:
   ```
   JIRA_BASE_URL=https://your-domain.atlassian.net
   JIRA_EMAIL=your-email@example.com
   JIRA_API_TOKEN=your-api-token
   JIRA_PROJECT_KEY=YOUR-PROJECT
   ```

2. Use the generated JSON payload with the Jira integration tool to bulk-create issues.

## Customization

### Adding New Steps
To add new processing steps:
1. Create a new prompt template in the `prompts/` directory
2. Add the step to the `steps:` section in `copilot.yaml`
3. Update the runner script if needed

### Modifying Prompts
All prompt templates are in markdown format and can be easily customized:
- Update system instructions
- Modify output formats
- Add new constraints or examples
- Change the tone or terminology

### Custom Input Types
The workflow can be extended to support additional input types by:
1. Adding new input definitions in `copilot.yaml`
2. Updating the runner script to handle new file types
3. Modifying relevant prompt templates

## Troubleshooting

### Common Issues

**File Not Found Errors:**
- Ensure `inputs/sow.md` and `inputs/hld.md` exist
- Check file paths in `copilot.yaml` are correct

**YAML Parse Errors:**
- Validate YAML syntax in `copilot.yaml`
- Check for proper indentation and formatting

**Missing Dependencies:**
- Install required packages: `pip install -r requirements.txt`
- Ensure Python 3.7+ is installed

### Debug Mode
Run with Python's debug flag for detailed execution information:
```bash
python -v run_copilot.py
```

## Architecture Notes

The runner script (`run_copilot.py`) provides:
- YAML workflow interpretation
- Sequential step execution
- Context management between steps
- Simulated LLM processing for demonstration
- JSON output formatting

In a production environment, you would integrate this with:
- OpenAI GPT API or similar LLM service
- Proper error handling and retry logic
- Progress tracking and intermediate saves
- Integration with your CI/CD pipeline