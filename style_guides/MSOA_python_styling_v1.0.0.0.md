# MSOA Python Styling Guide (Concord) v1.1.0.0

This document provides the coding and structural guidelines for Python projects under the Modular Service-Oriented Architecture - Concord (MSOA-Concord) standard.

## Python Code Style Guidelines

**Naming Conventions:**
- **Modules:** Lowercase with underscores (e.g., `market_analysis_engine.py`).
- **Classes:** CapWords convention (e.g., `TradeEntryEngine`).
- **Functions:** Lowercase with underscores (e.g., `enter_trade`).
- **Variables:** Lowercase with underscores (e.g., `api_key`).
- **Constants:** Uppercase with underscores (e.g., `API_KEY`).

**Code Structure:**
- **Indentation:** 4 spaces per indentation level.
- **Line Length:** Max 79 characters.
- **Blank Lines:** Two between classes and top-level functions, one within class methods.
- **Imports:** Grouped and separated by a blank line in the order of standard library, third-party, application-specific.
- **Parameter Passing:** Prefer named parameters over positional for better readability and to prevent errors.

**Documentation:**
- **Docstrings:** Triple-double quotes, describing function/class purpose, parameters, return types, and exceptions.
- **Comments:** Inline sparingly, explaining non-obvious details.

**Error Handling:**
- Utilize specific exceptions rather than generic catch-all.

**Performance Best Practices:**
- Employ list comprehensions and generator expressions judiciously. Limit the use of global variables.

## Project Folder Structure Guidelines

**Top-Level Directory:**
- Name after the project with a `README.md`.

**Source Directory (`src`):**
- Contains all source files with subdirectories by functionality.

**Service Layer (`services`):**
- Related services grouped within their own subdirectory.

**Configurations and Scripts:**
- Configuration files in `configs`.
- Scripts for tasks in `scripts`.

**Tests:**
- A tests directory mirroring the `src` structure.

**Virtual Environment:**
- `.env` for environment variables, exclude sensitive information from version control.

**Documentation and Drafts:**
- A `docs` or `drafts` directory for extensive project documentation.

**Initialization Files:**
- An `__init__.py` in each package.

**Miscellaneous:**
- Appropriate directories for Docker files, CI/CD scripts (`docker`, `ci_cd`).

## System Initialization with Builders

**System Initialization:**
- For systems requiring multiple service components with complex configurations, use a builder class to encapsulate the construction process.
- The builder class allows for a step-by-step construction and provides a single point of configuration for the entire system.

**Example:**
- The `ScalpingSystemBuilder` is responsible for constructing the `ScalpingSystem` by piecing together the `SessionManager`, `TradeEntryEngine`, `DataFetcher`, and any other required components.

## Architecture Naming Convention

**Modular Service-Oriented Architecture - Concord (MSOA-Concord):**
- Reflects the principles of "Clean Architecture" with a focus on modularity and service orientation.
- Encourages independence from frameworks, testability, UI and database agnosticism, and external agency agnosticism.

## Versioning and Documentation

- The guide follows semantic versioning (v1.1.0.0) indicating major changes, minor updates, patches, and builds.
- All updates to the guide should be documented with an incremented version number.
