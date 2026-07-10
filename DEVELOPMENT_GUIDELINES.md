# RT-DOS Founder Alpha Development Guidelines

## Purpose

These guidelines define how contributors should extend RT-DOS Founder Alpha while preserving the project’s architecture, clarity, and long-term maintainability.

---

## Coding Standards

- Write clear, readable Python code.
- Use docstrings for all public classes and methods.
- Use type hints where practical.
- Prefer small, focused functions and classes.
- Keep modules free of hidden side effects.
- Avoid introducing business logic into UI components.
- Prefer explicit configuration over magic values.

---

## Naming Conventions

- Use PascalCase for classes.
- Use snake_case for functions, methods, and variables.
- Use descriptive names that reflect the module’s purpose.
- Keep engine names aligned with their analytical responsibility.
- Keep UI component names aligned with the display responsibility.

Examples:
- MarketSentinelEngine
- ExecutiveAlerts
- DailyBrief
- IntelligencePipeline

---

## File Organization

- Put core analytical logic in the engines/ directory.
- Put pure calculations in the indicators/ directory.
- Put presentation and Streamlit components in the ui/ directory.
- Keep shared configuration in config/.
- Keep documentation in docs/ and project root markdown files.

---

## Testing Workflow

- Validate new code before committing.
- Prefer small, targeted verification steps over broad assumptions.
- Ensure new engines and UI components behave safely when given minimal or empty data.
- Keep behavior deterministic and predictable.
- Add regression checks when extending existing workflows.

---

## Git Workflow

- Make focused changes that address one concern at a time.
- Keep commits descriptive and milestone-oriented.
- Avoid mixing unrelated changes in a single change set.
- Update documentation when architecture or behavior changes.
- Preserve existing functionality unless the task explicitly requires a change.

---

## Rules for Adding New Engines

1. Give the engine a single, clear responsibility.
2. Keep the public interface simple and stable.
3. Return structured dictionaries when appropriate.
4. Avoid hard-coded dependencies on live external services unless explicitly required.
5. Make the engine easy to test and easy to extend.
6. Document the engine’s purpose and expected inputs/outputs.

---

## Rules for Adding New UI Components

1. Keep the component presentation-only.
2. Do not implement trading or market logic inside a UI class.
3. Accept data from the application or engine layer and render it.
4. Preserve the current order of dashboard sections unless explicitly requested otherwise.
5. Use Streamlit primitives consistently and keep the user experience clean.

---

## Architecture Principles

- Separate analysis from display.
- Keep the pipeline composable.
- Favor clear interfaces over hidden coupling.
- Maintain explainability and transparency.
- Design for future extension, not only the current release.
- Treat the dashboard as a consumer of well-structured engine output.
