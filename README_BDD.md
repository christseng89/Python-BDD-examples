# Mastering BDD with Python Behave
git clone https://github.com/NehaAuchar/bdd_behave_pom.git

## Introduction to Course

- Gain a solid understanding of BDD and its role in modern software development.
- Learn how to write clear, structured tests using Gherkin, a simple, plain-text language designed to describe software behavior.
- Master the Behave framework to automate test scenarios, ensuring your code functions as expected while keeping the focus on business outcomes.
- Understand the Discovery, Formulation, and Automation phases of BDD, ensuring full alignment between stakeholders and development teams.

### Gherkin Vs Behave

#### Gherkin
- What it is? Gherkin is a human-readable language.
- Purpose: Bridge between business language and code.
- Usability: Writing behavior specifications that anyone can understand.

#### Behave
- What it is? Testing Framework.
- Purpose: Takes scenarios written in Gherkin, converts them into executable code.
- Usability: Automating the test specifications.

Enable teams to write tests in plain language and ensure that the system behaves as expected.

### Gherkin – Key concepts
- Feature: High-level description of a functionality.
- Scenario: Specific example illustrating the feature.
- Scenario Outline: Specific example illustrating the feature with multiple data sets.
- Steps: Given, When, Then statements that define the scenario.
- Background: Keyword defining shared steps.
- Tags: Categorizing scenarios or features.

** Refer to BddTemplate.feature file
Developers, Testers, and Business Stakeholders are involved in writing Gherkin Scenarios.

### Behave key concepts
- Specifications: Executable Gherkin scenarios.
- Step Definition: Steps to actual code.
- Glue Code: Connect step definition to Gherkin scenarios.
- Report: Shows which tests passed, failed, or were skipped.

## BDD Phases
1. Discovery: The requirement-gathering phase involves structured conversations during Discovery Workshops. Teams explore and agree on desired system behaviors, enhancing shared understanding and prioritizing functionality. This minimizes unnecessary meetings while maximizing productivity.
2. Formulation: This documentation phase converts key examples from discovery into structured, executable documentation. Unlike traditional documentation, BDD uses human- and machine-readable formats, enabling validation, automation, and fostering a common language across teams for clarity and consistency.
3. Automation: The implementation phase translates formulated examples into automated tests that drive development. Initially failing tests guide the coding process, ensuring alignment with desired behaviors. Automated tests act as a safety net during maintenance, reducing manual regression testing and enabling teams to focus on exploratory testing.

### Advantages of BDD
- Enhanced Collaboration: By uniting developers, testers, business analysts, and stakeholders, BDD fosters shared understanding and alignment, ensuring the right solution is built.
- Iterative Development: BDD supports rapid feedback loops through small, iterative chunks, allowing early validation and adjustments, improving value flow and issue detection.
- Living Documentation: Executable tests ensure up-to-date, user-friendly documentation that simplifies system understanding and maintenance.

## Discovery Phase
PO - Product Owner

### Discovery Phase in 7 Steps
1. Kickoff
2. Preparation: This involves defining the project scope, refining user stories and acceptance criteria, and preparing business examples. Stakeholders are identified to ensure comprehensive perspectives are included, while developers assess technical feasibility and testers review testability.
   - Pre-session preparation includes:
     - PO/BA - Define scope, Prioritized user stories, refine acceptance criteria, some business examples 
     - PO/BA - Identifying stakeholders who should be part of Discovery Workshops.
     - Developer - Technical feasibility, potential blockers, system impacts.
     - Testers - Testability review, queries, automation opportunities.
3. Discovery Workshops: Collaborative sessions where teams explore user stories in depth, clarify ambiguities, and identify edge cases. For example, during a workshop on fund transfers, teams discuss scenarios like insufficient funds or authentication requirements.
4. Three Amigos Practice: A collaboration between 'business representatives', 'developers', and 'testers' to refine user stories, clarify requirements, and ensure alignment across business goals, technical feasibility, and testability.
5. Defining Scenarios: Teams convert user stories and acceptance criteria into testable, plain-language scenarios that capture intended behaviors, uncover edge cases, and reduce misunderstandings.

   Business Example: 
   - User Story -> Fund Transfer
   - Description: As a customer, user wants to transfer the funds from checking account to savings account.
   - Acceptance Criteria:
     - User should be able to select from and to account from the list of accounts.
     - User should be able to enter amount.
     - Confirmation message post successful transactions.
     - Balance of these accounts should be updated accordingly.
   - Defining scenarios
      - Scenario 1: Successful fund transfer from checking to savings account
      - Scenario 2: Transaction rejected due to invalid amount 
   
   Scenarios are translated into a DRAFT Gherkin syntax.

6. Prioritization: Scenarios are reviewed and ranked based on their importance and business value to focus development efforts on critical areas. 
7. Scenario Review: Teams validate scenarios, ensuring comprehensive test coverage, refining gaps, and addressing edge cases.
   - Challenge Review / Test Scenarios
     - Scenario 1: Successful fund transfer from checking to savings account
     - Scenario 2: Transaction rejected due to invalid amount.
     - Scenario 3: Transaction rejected due to insufficient funds.
     - Scenario 4: Incomplete transaction due to session timeout.
     - Scenario 5: Invalid transaction when user has only one saving or checking account.
     - Scenario 6: Transaction failure due to blocked or closed "to"/"destination" account.
   
   Revise the Draft Gherkin after review. BDD promotes 
   - Collaboration, 
   - Iterative feedback loops, and 
   - User-centric development, 
 
   Ensuring quality software that aligns with user needs and reduces 'rework'.

   总结：
   - 在发现阶段，Gherkin场景通常会在定义场景（Defining Scenarios）步骤中开始撰写，但这些内容仍是草稿，主要用于团队的共同理解。正式的feature文件会在BDD工作流程的后续阶段创建。

## Formulation Phase
The formulation phase in BDD transforms the scenarios identified during the discovery phase into clear, executable specifications. 
This phase serves as a bridge between understanding the desired behavior and implementing it through automated tests. 
Its primary goal is to refine Gherkin scenarios to ensure they are accurate, precise, unambiguous, and aligned with business goals.

### Key Aspects of the Formulation Phase:
- Collaboration: Developers, testers, and product owners work closely to ensure scenarios are detailed, understandable by the entire team, and executable by automation tools.
- Gherkin Syntax: Scenarios are written in carefully crafted Gherkin syntax, reflecting the system's behavior. These scenarios serve both as documentation and as automated test cases, a key advantage of BDD.

Steps in the Formulation Phase:
- Review and Clarify: The team (Product Owner, Business Analyst, Developers, and Testers) reviews the outcomes from the discovery phase, addresses uncertainties, and refines acceptance criteria if needed. This serves as a second round of review to resolve both technical and non-technical challenges.
- Writing Gherkin Scenarios: Translating user stories and acceptance criteria into executable Gherkin scenarios.
- Refining and Organizing Scenarios: Ensuring scenarios are structured and organized for clarity and alignment with business objectives.
- Stakeholder Review: A final review by stakeholders to validate the scenarios and confirm alignment with business goals.

Summary:
- The formulation phase ensures that scenarios are polished and ready for automation, enhancing both documentation and testing efficiency. It emphasizes collaboration, refinement, and precision to maintain alignment with business goals and prepare for the implementation phase.

### Steps to Formulation Phase
1. Review and Clarify
2. Write Gherkin Scenarios
3. Refine and Organize
4. Stakeholder Review

### Formulation Phase Best Practices
- Split Scenarios by Valid and Invalid Cases.
- Utilize Background.
- Keep Scenarios short and focused.
- Use Scenario Outline.
- Behavior should be explained clearly from user's perspective.
- Single focused test scenario.
- Do not overcomplicate.

## Automation Phase
### Steps to Automation Phase
1. Setup Automation Framework
2. Map Feature files to step definition
3. Automate Test Scenarios
4. Review and Validate
5. Test Execution
