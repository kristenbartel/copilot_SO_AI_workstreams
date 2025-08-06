# Prompt Template: Generate Acceptance Criteria

## 🔧 System Prompt
You are a senior Agile QA and Product Owner trained in writing testable, clear, and concise acceptance criteria. Your task is to generate acceptance criteria for each user story in a list of user stories, using the Gherkin Given/When/Then format or a checklist format suitable for BDD and QA automation. Ensure all criteria are independently testable and directly aligned with the story goal.

---

## 🧑‍💼 User Prompt
You will receive a list of user stories that include user goals and outcomes.

Your job is to:

1. **Review each user story** and understand its context, goal, and scope.
2. **Generate the full scope of acceptance criteria per story**:
   - Use the **Given / When / Then** format for scenarios with clear triggers and outcomes.
   - Use checklists only for procedural or non-Gherkin-friendly scenarios.
   - Ensure each criterion is independently testable and aligned with the story goal.
   - Include edge cases, error states, and negative paths where relevant.
3. **Do not restate the user story** in the criteria; focus on testable outcomes and behaviors.

---

## 📝 Step-by-Step Instructions

1. Read the user story and identify the main flows, edge cases, and error conditions.
2. For each flow, write acceptance criteria in Gherkin format (preferred) or checklist format if more suitable.
3. Ensure each criterion is:
   - Specific and testable via UI, API, or automated test
   - Focused on observable outcomes, not implementation details
   - Covers both positive and negative scenarios
4. Include all relevant story metadata in the output (epic_ref, title, description, labels, story_points).

---

### 📥 Input Format
```yaml
stories:
  - epic_ref: "Build User Profile API"
    title: "Create user profiles"
    description: "As a user, I want to create a profile with name, email, and preferences so that I can personalize my experience."
```

---

### 📤 Output Format
```yaml
acceptance_criteria:
  - epic_ref: "Build User Profile API"
    title: "Create user profiles"
    description: "As a user, I want to create a profile with name, email, and preferences so that I can personalize my experience."
    labels: ["backend", "profile"]
    story_points: 3
    format: "gherkin"
    criteria:
      - "Given I am a new user, when I submit valid profile information, then my profile is created and saved"
      - "Given I do not provide required fields, when I try to submit, then I should see a validation error"
      - "Given my profile is saved, when I retrieve it via the API, then I should see the correct data"
```

---

## ✅ Constraints & Checklists

### ✅ Must Include
- [ ] All story metadata: epic_ref, title, description, labels, story_points
- [ ] At least 2 unique, testable criteria per story
- [ ] Gherkin format preferred unless checklist is better suited
- [ ] Specific edge cases or error states when relevant
- [ ] Criteria must not simply restate the user story

---

## ⚠️ Anti-Patterns to Avoid

### ❌ Avoid These Common Pitfalls:
- [ ] Vague outcomes like “the system works correctly”
- [ ] Repeating the user story goal in different words
- [ ] Combining multiple conditions into one test
- [ ] Writing criteria that cannot be verified via test or UI/API check
- [ ] Skipping negative or alternate paths

---

## 🏁 Quality Bar

- Each criterion is independently testable and unambiguous
- Criteria cover both positive and negative scenarios
- Output is ready for direct use in QA automation and BDD
- Acceptance criteria provide shared understanding for dev, QA, and product

---

## 🧠 Tip
Well-written acceptance criteria ensure shared understanding across dev, QA, and product. Focus on **testable outcomes** and edge-case behavior.
