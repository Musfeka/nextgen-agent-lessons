import os
import sqlite3
import pandas as pd
import pytest


# =====================================================================
# AGENT TOOL FUNCTIONS FOR TESTING
# =====================================================================
def execute_sql_query(query: str) -> str:
    try:
        conn = sqlite3.connect(":memory:")
        df_demo = pd.DataFrame({
            "id": [1, 2, 3, 4],
            "name": ["Alice", "Bob", "Charlie", "David"],
            "salary": [70000, 80000, 90000, None],
            "department": ["IT", "HR", "IT", "Finance"],
        })
        df_demo.to_sql("employees", conn, index=False, if_exists="replace")
        result = pd.read_sql_query(query, conn)
        conn.close()
        return result.to_string()
    except Exception as e:
        return f"SQL Execution Error: {str(e)}"


def read_csv_file(file_path: str, num_rows: int = 5) -> str:
    try:
        if not os.path.exists(file_path):
            return f"Error: File '{file_path}' does not exist."
        df = pd.read_csv(file_path)
        preview = df.head(num_rows).to_string()
        info = f"Shape: {df.shape[0]} rows, {df.shape[1]} columns\nColumns: {list(df.columns)}"
        return f"{info}\n\nPreview:\n{preview}"
    except Exception as e:
        return f"CSV Reading Error: {str(e)}"


def check_data_quality(file_path: str) -> str:
    try:
        if not os.path.exists(file_path):
            return f"Error: File '{file_path}' does not exist."
        df = pd.read_csv(file_path)
        null_counts = df.isnull().sum().to_dict()
        duplicates = int(df.duplicated().sum())

        report = f"--- DATA QUALITY REPORT ---\n"
        report += f"Total Rows: {len(df)}\n"
        report += f"Duplicate Rows: {duplicates}\n"
        report += f"Missing Values:\n"
        for col, count in null_counts.items():
            report += f"  - {col}: {count} missing\n"
        return report
    except Exception as e:
        return f"Data Quality Check Error: {str(e)}"


# =====================================================================
# UNIT TESTS
# =====================================================================
def test_execute_sql_query():
    result = execute_sql_query(
        "SELECT name FROM employees WHERE department = 'IT'"
    )
    assert "Alice" in result
    assert "Charlie" in result
    assert "Bob" not in result


def test_read_csv_file(tmp_path):
    d = tmp_path / "sample.csv"
    d.write_text("id,name\n1,Alpha\n2,Beta")
    result = read_csv_file(str(d), num_rows=1)
    assert "Alpha" in result


def test_check_data_quality(tmp_path):
    d = tmp_path / "data_with_nulls.csv"
    d.write_text("id,val\n1,10\n2,\n1,10")
    report = check_data_quality(str(d))
    assert "Duplicate Rows: 1" in report
    assert "val: 1 missing" in report
