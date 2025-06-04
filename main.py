from exa_py import Exa
import os
import pandas as pd
import argparse

# Initialise Exa.ai SDK with api key
exa = Exa(os.getenv("KEY_EXA_PYTHON"))


# Function - Read company names from csv
def readNames(file_path: str, column_name: str):
    df_input_file = pd.read_csv(file_path)

    if column_name not in df_input_file.columns:
        raise ValueError(f"Column '{column_name}' does not exist in the csv file.")
    return df_input_file[column_name].tolist()


# Function - Get data from Exa.ai
def apiCall(query_string: str):
    raw_response = exa.search(query_string, num_results=1, category="company")
    result = raw_response.results[0]
    data = {
        "domain": result.id,
        "score": result.score,
        "query": raw_response.autoprompt_string,
        "description": result.title,
    }
    return data


# Function - loop over company names and fetch data
def fetchLoop(items: list[str]):
    results = []
    for i in items:
        results.append(apiCall(i))
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
