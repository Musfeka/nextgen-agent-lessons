# Data Engineering AI Agent

An autonomous Data Engineering AI Agent built with Google's `google-genai` SDK and Python. The agent uses the ReAct pattern to process user prompts and invoke local tools.

## Features
- **SQL Tool**: Executes queries on an in-memory database.
- **CSV Inspection**: Reads, previews, and inspects CSV files.
- **Data Quality Checker**: Identifies missing values and duplicate records.
- **Automated Tests**: Unit testing implemented via `pytest`.

## Setup & Running Tests
```bash
pip install -r requirements.txt
pytest test_agent.py
```
