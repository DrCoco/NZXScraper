from pathlib import Path
# from nzxscraper import scrape_data
import glob
import errno
from bs4 import BeautifulSoup
import sys
print(sys.path)
testInputDirectory = str(Path(r"C:/Users/Kiran/Documents/GitHub/NZXScraper/testnzxscraper/testinputs"))

def read_in_html(regex):
    inputList = list()
    path = testInputDirectory + regex # '/*SummaryPageSource.txt'
    files = glob.glob(path)
    for name in files:
        try:
            with open(name) as file:
                inputList.append(BeautifulSoup(file.read(),'lxml'))
        except IOError as exc:
            if exc.errno != errno.EISDIR:
                raise
    return inputList
