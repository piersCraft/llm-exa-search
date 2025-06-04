# llm-exa-search

Python script to pull data from the exa.ai Search API using the python SDK. It takes a list of company names as the input and outputs a single match per company name that has details of the company website

## Dependencies
- Python 3
- pandas
- exa_py 
- argparse
- os

## Installation
Python packages
```sh
pip install pandas exa_py argparse os
```
Navigate to the directory that you want to store the project in and clone the repo
```sh
git clone https://github.com/piersCraft/llm-exa-search.git
```
## Usage
You can now navigate to the project directory and run the script in the terminal. The CLI command takes two arguments:
1. Path to the input csv file that contains the company names you want to query
2. Name of the column within the file that holds the company names

Execute the script like so:
```sh
python3 main.py your_file_path_here column_name_here
```
It will output a csv file of the results to the project directory
