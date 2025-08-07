# BacklogBuilderCopilot - AI-Powered Backlog Generator

This repository contains a complete AI-powered backlog generation system using GitHub Copilot agents. The **BacklogBuilderCopilot** agent transforms Statement of Work (SOW) and High-Level Design (HLD) documents into a full Agile backlog with Jira-compatible output.

## Pipeline Process

The system works through a sequential 7-step pipeline:

1. **Extract Deliverables** - Identify key deliverables from SOW/HLD documents
2. **Map Deliverables to Epics** - Convert deliverables into structured epics
3. **Generate User Stories** - Create detailed user stories from epics
4. **Add Acceptance Criteria** - Generate comprehensive acceptance criteria
5. **Infer Dependencies** - Analyze and document inter-story dependencies
6. **Review and Format for Jira** - Prepare structured Jira API payloads
7. **Create CSV** - Generate bulk upload formats

## Repository Structure

```
├── copilot.yaml                           # Copilot agent configuration
├── requirements.txt                       # Python dependencies
├── prompts/                               # Modular prompt templates
│   ├── 01_extract_deliverables.md         # SOW/HLD analysis
│   ├── 02_map_to_epics.md                 # Epic mapping
│   ├── 03_generate_stories.md             # User story generation
│   ├── 04_generate_acceptance_criteria.md # Acceptance criteria
│   ├── 05_infer_dependencies.md           # Dependency analysis
│   ├── 06_review_and_format_for_jira.md   # Jira formatting
│   └── 07_create_csv.md                   # CSV generation
└── tools/
    └── jira_integration.py                # Jira API integration
```

Each prompt template includes:
- System instructions for AI context
- User instructions and examples
- Input and output format specifications
- Constraints and validation rules

## Getting Started

### Prerequisites

- GitHub Copilot Pro Plus subscription
- Access to SOW and HLD documents
- Python 3.7+ (for Jira integration tool)
- (Optional) Jira instance for direct integration

### Usage Options

#### 1. GitHub Copilot Workspace Agent

The primary usage is through the **BacklogBuilderCopilot** agent defined in `copilot.yaml`:

```bash
# Ensure your SOW and HLD documents are ready
# The agent expects:
# - inputs/sow.md (Statement of Work)
# - inputs/hld.md (High-Level Design)

# Run the complete pipeline through GitHub Copilot Workspace
```

#### 2. Individual Prompt Usage

For custom implementations or debugging:
- Embed them into your GitHub Copilot Workspace agent
- Use them in local scripts with OpenAI’s SDK
- Chain them together for automated backlog generation
- Integrate with existing project management workflows

#### 3. Jira Integration

For direct Jira integration, configure the Python tool:

```bash
# Install Python dependencies
pip install -r requirements.txt

# Set up environment variables:
export JIRA_BASE_URL=https://your-domain.atlassian.net
export JIRA_EMAIL=your-email@company.com
export JIRA_API_TOKEN=your-api-token
export JIRA_PROJECT_KEY=YOUR_PROJECT

# Use tools/jira_integration.py for bulk issue creation
```

## Input Requirements

The system expects two primary input documents:

- **Statement of Work (SOW)**: Business requirements and project scope
- **High-Level Design (HLD)**: Technical architecture and system design

These should be provided as markdown files for optimal parsing and analysis.

## Output Formats

The pipeline generates multiple output formats:

- **Structured Deliverables**: JSON/YAML format for epics and stories
- **Jira Payloads**: REST API compatible JSON for direct upload
- **CSV Files**: Bulk import format for various project management tools
- **Dependency Maps**: Visual representation of story relationships

---

**Customization**: Feel free to customize prompt tone, terminology, or format based on your Jira configuration and team vocabulary.
