<div align="center">
  <h1>cs50-python</h1>
  <p>Official problem sets, laboratory exercises, and coursework solutions for Harvard University's CS50P (Introduction to Programming with Python).</p>

  <p>
    <a href="LICENSE"><img src="https://img.shields.io/badge/License-Educational-lightgrey?style=flat-square&logo=academia&logoColor=white" alt="License"></a>
    <img src="https://img.shields.io/badge/Institution-Harvard_University-A51C30?style=flat-square&logo=harvard&logoColor=white" alt="Harvard">
    <img src="https://img.shields.io/badge/Course-CS50P-blue?style=flat-square&logo=edx&logoColor=white" alt="CS50P">
    <img src="https://img.shields.io/badge/Language-Python_3.11+-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
    <a href="https://github.com/itsgoharrehman/cs50-python/stargazers"><img src="https://img.shields.io/github/stars/itsgoharrehman/cs50-python?style=flat-square&logo=github&logoColor=white" alt="Stars"></a>
    <a href="https://github.com/itsgoharrehman/cs50-python/issues"><img src="https://img.shields.io/github/issues/itsgoharrehman/cs50-python?style=flat-square&logo=github&logoColor=white" alt="Issues"></a>
  </p>
</div>

---

> [!IMPORTANT]
> **Academic Honesty and Institutional Integrity**:
> This repository contains completed academic coursework for Harvard University's **CS50P (CS50's Introduction to Programming with Python)**. In strict accordance with Harvard's Policy on Academic Honesty and the edX Honor Code, students currently enrolled in the course are strictly prohibited from copying, plagiarizing, or submitting any part of these solutions. This repository exists solely for educational reference, code review, and portfolio demonstration.

---

## Curriculum and Problem Set Matrix

The repository covers all core pedagogical modules, problem sets, and unit testing requirements:

| Module | Core Concepts | Problem Sets & Exercises |
| :--- | :--- | :--- |
| **Week 0: Functions & Variables** | Return values, string formatting, mathematical functions, type conversion | `indoor.py`, `playback.py`, `faces.py`, `einstein.py`, `tip.py` |
| **Week 1: Conditionals** | Boolean logic, conditional branches, `match-case` statements | `deep.py`, `bank.py`, `meal.py`, `interpreter.py`, `extensions.py` |
| **Week 2: Loops** | `for` and `while` iteration, string traversal, list comprehension | `camel.py`, `coke.py`, `twttr.py`, `plates.py`, `nutrition.py` |
| **Week 3: Exceptions** | Defensive programming, `try-except-else-finally`, loop reprompting | `fuel.py`, `taqueria.py`, `grocery.py`, `outdated.py` |
| **Week 4: Libraries** | Python Standard Library (`sys`, `random`, `requests`, CLI arguments) | `emojize.py`, `figlet.py`, `adieu.py`, `game.py`, `professor.py`, `bitcoin.py` |

---

## Directory Structure

```
cs50-python/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.yml          # Defect reporting form
│   │   └── question.yml            # Conceptual question form
│   ├── PULL_REQUEST_TEMPLATE.md    # Academic integrity PR verification
│   └── dependabot.yml              # Weekly automated pip dependency scanner
├── week0/                          # Functions and variables exercises
├── week1/                          # Conditionals and match-case exercises
├── week2/                          # Loops and list iterations
├── week3/                          # Exception handling and input assertions
├── week4/                          # Standard library and third-party modules
├── requirements.txt                # Testing and execution dependencies
├── LICENSE                         # Educational Coursework License
├── SECURITY.md                     # Security policy and disclosure protocol
├── CONTRIBUTING.md                 # Academic archive contribution guidelines
└── CODE_OF_CONDUCT.md             # Contributor Covenant v2.1
```

---

## Running Exercises Locally

### Prerequisites

* Python 3.11 or later
* Virtual environment (recommended)

### Execution

1. Clone the repository:
   ```bash
   git clone https://github.com/itsgoharrehman/cs50-python.git
   cd cs50-python
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # Linux/macOS:
   source .venv/bin/activate
   ```

3. Install testing dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run any exercise:
   ```bash
   python week0/einstein.py
   python week4/bitcoin.py 2.5
   ```

---

## Governance and Licensing

* **License**: Licensed under the terms of the [Educational Coursework License](LICENSE).
* **Security & Vulnerabilities**: Please review [SECURITY.md](SECURITY.md) for vulnerability reporting.
* **Academic Guidelines**: See [CONTRIBUTING.md](CONTRIBUTING.md) regarding policy for completed coursework archives.
