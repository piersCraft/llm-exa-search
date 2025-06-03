from exa_py import Exa
import os


exa = Exa(os.getenv("KEY_EXA_PYTHON"))

companyName: str = "hills pet nutrition"


def fetchDomain(companyName: str):
    return exa.search(companyName, num_results=1, category="company")


print(fetchDomain(companyName).results.__getitem__(0).url)
