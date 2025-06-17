from exa_py import Exa
import os
from exa_py.api import ResultWithTextAndSummary
import pandas as pd
import argparse
from typing import Any

# Initialise Exa.ai SDK with api key
exa = Exa(os.getenv("KEY_EXA_PYTHON"))


# Function - Read company names from csv
def readNames(file_path: str, column_name: str) -> list[Any]:
    df_input_file: pd.DataFrame = pd.read_csv(file_path)

    if column_name not in df_input_file.columns:
        raise ValueError(f"Column '{column_name}' does not exist in the csv file.")
    return df_input_file[column_name].tolist()


# Function - Get data from Exa.ai
def apiCall(query_string: str) -> list[dict[str, Any]]:
    raw_response = exa.search_and_contents(
        query_string,
        type="keyword",
        category="company",
        livecrawl="fallback",
        livecrawl_timeout=10000,
        summary={
            "query": "Include the industry sector of the company, then a short description of the company from the website text"
        },
        text={"max_characters": 500},
        num_results=2,
    )
    matches = raw_response.results
    for match in matches:
        match["input_name"] = query_string
    return matches


# Function - loop over company names and fetch data
def fetchLoop(query_strings: list[str]):
    results = []
    for query_string in query_strings:
        matches = apiCall(query_string)
        for match in matches:
            results.append(match)
    return results


# MAIN FUNCTION
def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(
        description="Read a specific column from a CSV file."
    )
    parser.add_argument("file_path", type=str, help="The path to the CSV file.")
    parser.add_argument("column_name", type=str, help="The name of the column to read.")

    args = parser.parse_args()

    # Execute function and handle errors
    try:
        names: list[str] = readNames(args.file_path, args.column_name)
        results_array = fetchLoop(names)
        results_df = pd.DataFrame(results_array)
        results_df.to_csv("exa_results.csv")

    except Exception as e:
        print(f"Error: {e}")


# Ensure correct entry point
if __name__ == "__main__":
    main()
