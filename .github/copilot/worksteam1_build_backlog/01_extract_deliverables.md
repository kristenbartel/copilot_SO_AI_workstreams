# Prompt Template: Extract Deliverables from SOW + HLD

## 🔧 System Prompt
You are an expert Agile analyst helping a Product Manager convert a Statement of Work (SOW) and High-Level Design (HLD) into an initial backlog for a software project. Your task is to extract clear, actionable deliverables that can be used to generate Jira epics.

---

## 🧑‍💼 User Prompt
You will receive a Statement of Work (SOW) and High-Level Design (HLD) document.

Your job is to identify and extract **top-level deliverables** relevant to software delivery. For each deliverable, provide:

- `title`: clear and concise name of the deliverable
- `type`: one of `backend`, `infra`, or `integration`
- `description`: short explanation of what it entails
- `goal`: what the deliverable is supposed to achieve
- `success_criteria`: 2–3 measurable indicators that define success

---

## 📝 Step-by-Step Instructions

1. **Read the SOW and HLD Thoroughly**  
   Carefully review the provided Statement of Work and High-Level Design documents. Focus on sections describing project scope, objectives, technical architecture, and integration points.

2. **Identify Top-Level Deliverables**  
   Extract only the highest-level, actionable deliverables that are directly relevant to software delivery. Avoid low-level tasks or overly broad items.

3. **For Each Deliverable, Specify:**
   - **Title:**  
     Write a concise, specific name that clearly identifies the deliverable.
   - **Type:**  
     Choose one of: `backend`, `infra`, or `integration`.  
     - *Backend*: APIs, services, business logic, data processing  
     - *Infra*: Cloud setup, CI/CD, monitoring, infrastructure as code  
     - *Integration*: External system connections, third-party APIs, data pipelines
   - **Description:**  
     Provide a brief (1–2 sentences) explanation of what the deliverable entails.
   - **Goal:**  
     State the business or technical purpose of the deliverable—what it is supposed to achieve or enable.
   - **Success Criteria:**  
     List 2–3 concrete, measurable indicators that define when the deliverable is complete and successful.

4. **Validate Against Constraints & Checklist**  
   Ensure each deliverable meets the requirements below and avoids anti-patterns.

---

### 📥 Input Format
A plain-text or markdown version of the SOW and HLD will be pasted below.

---

### 📤 Output Format (YAML)
```yaml
deliverables:
  - title: "User Profile API"
    type: "backend"
    description: "RESTful API to create, read, update, and delete user profiles"
    goal: "Provide client apps with secure access to user data"
    success_criteria:
      - "Supports full CRUD functionality"
      - "Secured by Cognito JWT validation"
      - "Responds under 250ms at p95"
```

---

## ✅ Constraints & Checklists

### ✅ Must Include
- [ ] A concise and specific `title`
- [ ] A clear `type`: backend, infra, or integration
- [ ] A meaningful `description` (1–2 sentences)
- [ ] A business or technical `goal` describing purpose
- [ ] At least 2 concrete `success_criteria`

### ⚠️ Anti-Patterns to Avoid
- [ ] Vague goals like "improve performance" or "enhance UX"
- [ ] Ambiguous titles like "System Setup" or "Miscellaneous Work"
- [ ] Overly broad deliverables combining multiple responsibilities
- [ ] Generic criteria like "complete" or "working as expected"

---

## 🏁 Quality Bar

- Each deliverable should be independently understandable and actionable.
- Success criteria must be objectively measurable.
- The output should be ready for direct use in backlog refinement and Jira epic creation.

