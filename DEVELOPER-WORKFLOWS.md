# Developer Workflows: Alamia-Skills-System in Action

> **A practical guide and walkthrough demonstrating how developers interact with the Alamia-Skills-System lifecycle operating model.**

---

## 1. The Interaction Model

Traditional AI pair programming forces developers into **tool micromanagement**:
- *"Read file A, check git status, see what we did yesterday."*
- *"Run pytest on tests/test_foo.py."*
- *"Review the code smells in this function."*
- *"Write a handoff note in docs/handoffs."*

With **Alamia-Skills-System**, the developer operates strictly at the **lifecycle stage level**. The developer uses 5 high-level commands, and the system resolves state, dependencies, and atomic skills autonomously:

```text
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌─────────────────────┐     ┌──────────────┐
│  bootstrap   │ ──> │  implement   │ ──> │      qa      │ ──> │ architecture-review │ ──> │ session-end  │
│ (Kickoff/Ctx)│     │ (Coding/TDD) │     │ (Validation) │     │  (Drift Governance) │     │ (Next Handoff│
└──────────────┘     └──────────────┘     └──────────────┘     └─────────────────────┘     └──────────────┘
```

---

## Workflow 1: Starting a Work Session (`bootstrap`)

### The Developer's Input
```text
"Bootstrap this project"
```
*(or simply `"Start session"`)*

### Behind the Scenes: What Alamia-Skills-System Does
1. **Dynamic Stack Discovery (`core/adapters/stack_detector.py`):**
   - Discovers Python 3.12, FastAPI, LangGraph, pip, and Docker compose.
2. **Dynamic Test Runner Discovery (`core/adapters/test_detector.py`):**
   - Locates `tests/` and identifies `pytest` as the test command.
3. **Session Memory Discovery (`core/adapters/memory_detector.py`):**
   - Scans `.ai/transient/handoffs/`, finds the latest handoff file (`07-session-handoff-dashboard-autonomous-scout-and-autologin.md`), extracts its title, and parses the 4 active pending objectives.
4. **Git Inspection:**
   - Detects active branch `standalone-flow` and latest commit.
5. **Idempotent Reconciliation (`core/reconciler.py`):**
   - Ensures `.alamia/project.json` matches project state without overwriting local custom rules.

### The System's Response to the Developer
```markdown
# Alamia-Skills-System: Bootstrap & Reconciliation Report

**Project:** `KamalExpress-Agents` | **Status:** `Case D` (Configured & Reconciled)

---

### 1. Discovered Stack & Environment
- **Primary Language:** `python` (Frameworks: `fastapi, langgraph, langchain`)
- **Package Manager:** `pip` | **Containers:** `docker, docker-compose`

### 2. Testing Configuration
- **Runner:** `pytest` | **Command:** `pytest` | **Dir:** `tests`

### 3. Discovered Project Memory
- **Latest Handoff:** `.ai/transient/handoffs/07-session-handoff-dashboard-autonomous-scout-and-autologin.md`
- **Active Pending Objectives:**
  1. Autonomous Scout Standby Decoupling (Pure Scout Mode)
  2. Dedicated In-Card Log Console for Slot Inspector
  3. Queue-to-Booking End-to-End Validation
  4. Portainer Staging Deployment

### 4. Git State
- **Branch:** `standalone-flow` (`1e825fd add to gitignore`)

---
**Ready.** You can now say `implement`, `qa`, `architecture-review`, or `session-end`.
```

---

## Workflow 2: Active Feature Implementation (`implement`)

### Scenario A: Working on Next Queued Task
The developer does not need to re-type the task from the previous session:

```text
"Implement the next pending objective"
```

#### What Alamia-Skills-System Does:
1. Reads `.alamia/project.json` $\rightarrow$ inspects the latest handoff $\rightarrow$ selects Task 1: **"Autonomous Scout Standby Decoupling (Pure Scout Mode)"**.
2. Reads the relevant architectural specification: `.ai/permanent/architecture/08-failproof-autonomous-workers-specification.md`.
3. Invokes Matt Pocock's atomic skill `/tdd`:
   - Writes a reproduction/unit test in `tests/test_operational_mode_and_day_rules.py` verifying that when `queued_clients == 0`, the monitor does *not* enter standby if pure scout mode is active.
4. Modifies `agents/appointments/monitor.py` to allow the scout to probe without queued applicants.
5. Runs the immediate test suite via `pytest` to verify the green phase.
6. Hands control back to the developer:
   > *"Implemented Pure Scout mode in `agents/appointments/monitor.py`. Targeted tests are passing. Ready for `qa`."*

---

### Scenario B: Working on a Specific Requested Feature
The developer specifies custom requirements:

```text
"Implement dedicated in-card log console for the slot inspector"
```

#### What Alamia-Skills-System Does:
1. Recognizes user-specified task overrides default handoff queue.
2. Reads architecture for UI conventions: inspects `api/static/index.html` and existing log streaming endpoint (`/api/logs/stream`).
3. Invokes atomic skill `/prototype` or `/to-spec` to ensure the DOM structure and CSS follow existing shadcn/ui patterns.
4. Implements the scrolling log box under the Telemetry Summary Bar in `api/static/index.html`.
5. Prompts the developer:
   > *"In-card log stream integrated. Ready for `qa` or visual check."*

---

## Workflow 3: Validation & Quality Assurance (`qa`)

### The Developer's Input
```text
"Run QA"
```
*(or `"Test changes"`, `"Validate"`)*

### Behind the Scenes: What Alamia-Skills-System Does
1. Checks `.alamia/project.json` for the discovered test configuration:
   ```json
   "testing": { "runner": "pytest", "command": "pytest" }
   ```
2. Executes the test suite against changed files:
   ```bash
   pytest tests/test_operational_mode_and_day_rules.py
   ```
3. Checks for regressions across dependent modules.
4. If tests pass, generates a structured verification matrix.
5. **Failure Case Handling:** If a test fails, the orchestrator automatically invokes Matt Pocock's `/diagnosing-bugs` atomic skill, isolates the root cause (e.g., deprecated `utcnow()` or missing fixture), and presents the fix hypothesis.

### The System's Response to the Developer
```markdown
## QA Verification Matrix

| Target | Tests Run | Passed | Failed | Warnings | Execution Time |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `tests/test_operational_mode_and_day_rules.py` | 4 | 4 | 0 | 30 | 0.62s |

- **Automated Tests:** PASSED
- **Static Check:** Clean syntax
- **Deprecation Warnings:** 30 warnings (`datetime.utcnow()` and FastAPI `@app.on_event`) noted for future refactor.
- **Overall QA Status:** **PASSED (Green)**
```

---

## Workflow 4: Architectural Drift Governance (`architecture-review`)

### The Developer's Input
```text
"Review architecture"
```
*(or `"Check drift"`)*

### Behind the Scenes: What Alamia-Skills-System Does
1. Checks `.alamia/project.json` for `memory.architecture_dir` (`.ai/permanent/architecture/`).
2. Gathers `git diff` of all changes made during the session.
3. Invokes Matt Pocock's two-axis `/code-review` atomic skill:
   - **Axis 1 (Standards):** Checks against Fowler smell baseline (Feature Envy, Data Clumps, Shotgun Surgery).
   - **Axis 2 (Spec & Architecture):** Validates against `.ai/permanent/architecture/01-system-architecture.md`:
     - *Rule:* Does new code access SQLite directly without thread-safe connection helpers?
     - *Rule:* Does the frontend talk to the database directly or route through FastAPI?
     - *Rule:* Are background worker loops properly decoupled from request handlers?

### The System's Response to the Developer
```markdown
## Architecture Review & Drift Analysis

### Axis 1: Standards & Code Smells
- **Duplicated Code:** None detected.
- **Shotgun Surgery:** Changes isolated to `monitor.py` and `index.html`.

### Axis 2: Architectural Alignment (01-system-architecture.md)
- **SQLite Concurrency:** Conforms to WAL thread-safe connection patterns.
- **Control Plane Boundaries:** Clean separation maintained; UI uses `/api/logs/stream`.
- **Verdict:** **ALIGNED (Zero Drift Detected)**
```

---

## Workflow 5: Ending a Session & Preserving Continuity (`session-end`)

### The Developer's Input
```text
"End session"
```
*(or `"Wrap up"`, `"Handoff"`)*

### Behind the Scenes: What Alamia-Skills-System Does
1. Inspects Git status (`git status --short`) to catalog all staged and unstaged files.
2. Checks latest test health.
3. Detects the project's memory pattern:
   - Discovered sequential numbering scheme in `.ai/transient/handoffs/`.
   - Previous file was `07-...`.
   - **Automatically calculates the next sequence:** `08-session-handoff-...md`.
4. Writes the new handoff adhering strictly to the headings and formatting of previous handoffs:
   - *Section 1: Objectives Achieved in This Session*
   - *Section 2: Key Verification Artifacts & System State*
   - *Section 3: Pending Work / Next Session Objectives* (carries forward remaining items).
5. Reports Git status cleanly without auto-pushing.

### The Generated Artifact: `.ai/transient/handoffs/08-session-handoff-...md`
```markdown
# Session Handoff 08: Autonomous Scout Decoupling & In-Card Console

> **Session Date:** 2026-10-05  
> **Branch:** `standalone-flow`  
> **Status:** Verified (Pytest Green)  

---

## 1. Objectives Achieved in This Session
1. **Autonomous Scout Standby Decoupling:**
   - Modified `agents/appointments/monitor.py` to probe GVC portal even when client queue is 0.
2. **Dedicated In-Card Log Console:**
   - Integrated streaming log display directly into GVC Slot Inspector view in `api/static/index.html`.

---

## 2. Key Verification Artifacts & System State
| Component | State / Verification | Location |
| :--- | :--- | :--- |
| **Monitor Loop** | Verified decoupled standby logic | `agents/appointments/monitor.py` |
| **Unit Tests** | 4 passed in 0.62s | `tests/test_operational_mode_and_day_rules.py` |

---

## 3. Pending Work / Next Session Objectives
1. **Queue-to-Booking End-to-End Validation:**
   - Add test applicant and verify auto-booking triggers on discovered slots.
2. **Portainer Staging Deployment:**
   - Merge `standalone-flow` to `main` and trigger Portainer staging script.
```

---

## Cross-Project Portability Example (Drop into Laravel)

If you copy the identical `Alamia-Skills-System` folder into an unrelated **Laravel** project:

1. You run: `"Bootstrap this project"`.
2. Alamia detects:
   - Stack: `php`, framework: `laravel`, package manager: `composer`.
   - Testing: `pest` (command: `./vendor/bin/pest`).
   - Memory: `docs/handoffs/`.
3. You run: `"Run QA"`.
4. Alamia executes: `./vendor/bin/pest` automatically.
5. **Zero lines of Alamia-Skills-System source code were modified.**

---

## Developer Cheatsheet

| Command | What to Say | What Alamia Does | Next Recommended Step |
| :--- | :--- | :--- | :--- |
| **`bootstrap`** | *"Bootstrap project"* / *"Start session"* | Discovers stack, tests, git, and extracts last handoff's pending tasks. | Proceed to `implement`. |
| **`implement`** | *"Implement next task"* / *"Implement X"* | Reads architecture spec, routes to `/to-spec` or `/tdd`, writes code & unit tests. | Proceed to `qa`. |
| **`qa`** | *"Run QA"* / *"Validate changes"* | Dynamically executes detected test runner & linters; isolates bugs with `/diagnosing-bugs`. | Proceed to `architecture-review`. |
| **`architecture-review`** | *"Review architecture"* / *"Check drift"* | Compares diff against architecture specs using two-axis `/code-review`. | Proceed to `session-end`. |
| **`session-end`** | *"End session"* / *"Wrap up"* | Verifies tests, catalogs git diff, and writes the next sequential handoff file. | Session closed cleanly. |
