# Copilot Agent Prompt Library

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

## 🚀 NEW: Execute the Complete Workflow

You can now run the entire workflow using the included Python runner:

```bash
# Install dependencies
pip install -r requirements.txt

# Run the workflow with sample inputs
python run_copilot.py
```

This processes your `inputs/sow.md` and `inputs/hld.md` files through all 6 steps and generates a complete backlog in `workflow_results.json`.

**Sample inputs included:** The repository includes example SOW and HLD files for an e-commerce platform to get you started immediately.

For detailed usage instructions, see [EXECUTION_GUIDE.md](EXECUTION_GUIDE.md).

---

Feel free to customize prompt tone, terminology, or format based on your Jira config and team vocabulary.
