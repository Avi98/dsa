# Agent Guidelines for dsa-py-strivers

This repository contains Python implementations of data structures and algorithms following the Striver's SDE sheet.

## Build/Test/Lint Commands

**Package Management (uv)**
- `uv sync` - Install dependencies from pyproject.toml
- `uv add <package>` - Add a dependency
- `uv add --dev <package>` - Add a dev dependency
- `uv run <command>` - Run a command in the virtual environment
- `uv run python <file.py>` - Run a Python file
- `uv run main.py` - Run the main entry point

**Running Tests**
- `uv run pytest` - Run all tests
- `uv run pytest -v` - Run tests with verbose output
- `uv run pytest <path/to/test_file.py>` - Run a specific test file
- `uv run pytest <path/to/test_file.py>::<test_function>` - Run a single test
- `uv run pytest -k <test_name_pattern>` - Run tests matching pattern

**Linting & Formatting (when configured)**
- `uv run ruff check .` - Run linter on all files
- `uv run ruff check --fix .` - Run linter with auto-fix
- `uv run ruff format .` - Format all files
- `uv run mypy .` - Run type checker

## Code Style Guidelines

**Python Version**: 3.12+

**Imports**
- Use absolute imports: `from array.problem import solution`
- Group imports: stdlib, third-party, local
- Sort imports alphabetically within groups

**Formatting**
- Follow PEP 8 style guide
- Use 4 spaces for indentation
- Maximum line length: 88 characters (Black/Ruff default)
- Use double quotes for strings

**Type Hints**
- Add type hints to all function signatures
- Use `from typing import ...` for complex types
- Use built-in generic types (list[int], dict[str, Any])
- Example: `def two_sum(nums: list[int], target: int) -> list[int]:`

**Naming Conventions**
- `snake_case` for functions and variables
- `PascalCase` for classes
- `UPPER_CASE` for constants
- Descriptive names: `left_pointer` not `lp`

**Function Structure**
```python
def function_name(param1: type1, param2: type2) -> return_type:
    """
    Brief description of what the function does.
    
    Args:
        param1: Description of param1
        param2: Description of param2
    
    Returns:
        Description of return value
    
    Time Complexity: O(?)
    Space Complexity: O(?)
    """
    # Implementation
    pass
```

**Documentation**
- Add docstrings to all modules, classes, and functions
- Include time/space complexity in docstrings
- Document edge cases and assumptions

**Error Handling**
- Use specific exceptions (ValueError, TypeError)
- Avoid bare except clauses
- Validate inputs explicitly
- Example: `if not nums: raise ValueError("Input list cannot be empty")`

**Algorithm Patterns**
- Prefer clarity over clever one-liners
- Add comments for complex logic
- Use descriptive variable names
- Separate concerns: parsing, processing, output

**File Organization**
- Each algorithm/problem in its own file
- Group related problems in directories
- Include `__init__.py` in all packages
- Add example usage in `if __name__ == "__main__":` block

**Testing**
- Use pytest for all tests
- Name test files: `test_<module>.py`
- Name test functions: `test_<function_name>_<scenario>`
- Include edge cases: empty input, single element, duplicates
- Use parametrize for multiple test cases

**Git Workflow**
- Make atomic commits
- Use descriptive commit messages
- Test before committing

## Project Structure

```
dsa-py-strivers/
├── array/              # Array problems
├── linked_list/        # Linked list problems
├── tree/               # Tree problems
├── graph/              # Graph problems
├── dp/                 # Dynamic programming
├── main.py             # Entry point
├── pyproject.toml      # Project configuration
└── README.md           # Documentation
```

## Quick Commands Reference

```bash
# Run the project
uv run main.py

# Run a specific algorithm file
uv run python array/two_sum.py

# Add testing framework
uv add --dev pytest

# Add linting tools
uv add --dev ruff mypy

# Run single test
uv run pytest array/test_two_sum.py::test_two_sum_basic -v
```
