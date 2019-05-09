from bs4 import BeautifulSoup
import sys
from time import time
from nzxscraper.scrape_data import get_browser, list_companies, scrape_company
from nzxscraper.print_excel import print_excel
from nzxscraper.environment import DEBUG, downloadDirectory, COMPANIES
import shutil
from nzxscraper import logger

startTime = time()
browser = get_browser()

stockTickersList = list_companies(browser)

# Initialise the array which is  going to store Stock class objects
stockDataArray = []

# For each ticker in the list, find the link to the respective summary page
for stock in stockTickersList :
    stockData = scrape_company(browser, stock)
    stockDataArray.append(stockData)

logger.info("Scraping complete")
browser.quit()
logger.info("Temporary files deleted")
shutil.rmtree(downloadDirectory)

print_excel(stockDataArray)

logger.info("Excel ready")

if DEBUG: endTime = time()
logger.info("That took a total of: " + str(round(endTime-startTime)) + " seconds.")
logger.info(str(round((endTime-startTime)/COMPANIES)) + " seconds per company.")
