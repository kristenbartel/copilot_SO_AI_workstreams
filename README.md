# Co1. **Extract Deliverables**
2. **Map Deliverables to Epics**
3. **Generate User Stories**
4. **Add Acceptance Criteria**
5. **Infer Dependencies**
6. **Format for Jira**
7. **Create Stories in Jira**

Each prompt is stored in a separate markdown file and includes:

- A system instruction
- A user instruction
- Input and output format
- Constraints and examples
- Format validation requirements

## How to Use

These prompts can be loaded dynamically into a Copilot agent, script, or CLI-based refinement tool. You can:
- Embed them into your GitHub Copilot Workspace agent
- Use them in local scripts with OpenAI's SDK
- Chain them together for full backlog automation
- Execute the complete workflow including Jira integration

## Enhanced Features

### Format Validation
Each prompt now includes validation steps to ensure:
- YAML outputs are properly formatted
- JSON payloads are valid and parseable
- No markdown artifacts remain in output files
- All files can be processed by standard parsers

### Jira Integration
Step 7 provides complete Jira integration:
- Bulk story creation via REST API
- Story name → issue key mappings
- Project statistics and summaries
- Ready-to-use tracking documentsLibrary

This repository contains modular prompt templates for building an AI-powered backlog generator using GitHub Copilot Pro Plus. Prompts are designed to work in a sequential pipeline:

1. **Extract Deliverables**
2. **Map Deliverables to Epics**
3. **Generate User Stories**
4. **Add Acceptance Criteria**
5. **Infer Dependencies**

Each prompt is stored in a separate markdown file and includes:

- A system instruction
- A user instruction
- Input and output format
- Constraints and examples

## How to Use

These prompts can be loaded dynamically into a Copilot agent, script, or CLI-based refinement tool. You can:
- Embed them into your GitHub Copilot Workspace agent
- Use them in local scripts with OpenAI’s SDK
- Chain them together for full backlog automation

---

Feel free to customize prompt tone, terminology, or format based on your Jira config and team vocabulary.
