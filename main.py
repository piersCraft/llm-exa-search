from exa_py import Exa
import os
import pandas as pd
import argparse

exa = Exa(os.getenv("KEY_EXA_PYTHON"))

companyName: str = "hills pet nutrition"


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
    return result


def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(
        description="Read a specific column from a CSV file."
    )
    parser.add_argument("file_path", type=str, help="The path to the CSV file.")
    parser.add_argument("column_name", type=str, help="The name of the column to read.")

    # Parse the arguments
    args = parser.parse_args()

    # Read the specified column from the CSV file
    try:
        names: list[str] = readNames(args.file_path, args.column_name)
        print(names)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
