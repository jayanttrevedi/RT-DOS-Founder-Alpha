# RT-DOS Founder Alpha
# 03 - Project Structure

**Document Version:** 1.0
**Status:** Living Document
**Owner:** RT-DOS Founder Project
**Last Updated:** July 2026

---

# 1. Purpose

This document defines the complete folder structure of RT-DOS Founder Alpha.

Every folder has a single responsibility.

Future developers should understand the entire project simply by reading this document.

---

# 2. Root Structure

```
RT-DOS-Founder-Alpha/

app.py

README.md

requirements.txt

.gitignore

docs/

engines/

indicators/

ui/

data/

reports/

tests/

assets/

config/

logs/
```

---

# 3. Folder Responsibilities

## app.py

The application entry point.

Responsibilities

- Starts Streamlit
- Loads workspace
- Executes intelligence pipeline
- Controls application lifecycle

---

## docs/

Project documentation.

Contains

- Vision
- Architecture
- Data Flow
- Developer Guide
- Founder Notes

No production code belongs here.

---

## engines/

Business intelligence.

Contains all analytical engines.

Examples

- Data Provider
- Market Data Engine
- Validation Engine
- Technical Engine
- Momentum Engine
- ATR Engine
- Volume Engine
- Relative Strength Engine
- Composite Engine
- Decision Engine

Future

- Fundamental Engine
- AI Engine
- News Engine
- Options Engine
- Macro Engine

---

## indicators/

Mathematical calculations.

Contains

EMA

RSI

ATR

MACD

ADX

Bollinger Bands

VWAP

Moving averages

No business decisions should exist here.

Indicators only calculate values.

---

## ui/

Presentation layer.

Contains

Navigation

Workspace Router

Market Command Centre

Cards

Panels

Themes

Reusable Components

Future

Portfolio Workspace

Scanner Workspace

Options Workspace

AI Workspace

---

## data/

Local datasets.

Examples

Watchlists

Cached market data

Reference data

Exchange master files

No application logic.

---

## reports/

Generated output.

Examples

CSV

PDF

Excel

AI Reports

Trading Reports

---

## tests/

Automated testing.

Future

Unit Tests

Integration Tests

Regression Tests

Performance Tests

---

## assets/

Static resources.

Icons

Images

Logos

Fonts

Templates

---

## config/

Configuration files.

Examples

Application Settings

API Keys

Theme Configuration

Workspace Configuration

---

## logs/

Runtime logs.

Examples

Errors

Downloads

Validation

Debug Information

---

# 4. Coding Standards

Each folder should contain only one category of responsibility.

Business logic must never appear inside UI.

UI must never contain calculations.

Indicators must never make decisions.

---

# 5. Dependency Direction

```
Indicators

↓

Engines

↓

Presentation

↓

UI

↓

User
```

Dependencies should always move downward.

Reverse dependencies should be avoided.

---

# 6. Naming Standards

Folders

lower_case

Examples

engines

ui

tests

reports

Files

snake_case.py

Classes

PascalCase

Functions

snake_case()

Constants

UPPER_CASE

---

# 7. Expansion Strategy

Future modules should be added without disturbing existing folders.

Prefer new modules over modifying stable production components.

---

# 8. Summary

The project structure is intentionally modular.

Each directory has a clearly defined responsibility.

Maintaining this separation is essential for long-term maintainability.

---

End of Document
