from exa_py import Exa
import os


exa = Exa(os.getenv("KEY_EXA_PYTHON"))

companyName: str = "hills pet nutrition"


def fetchDomain(companyName: str):
    response = exa.search(companyName, num_results=1, category="company")
    result = response.results[0]
    return result


print(fetchDomain(companyName))
