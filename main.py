from bs4 import BeautifulSoup
import sys
from time import sleep, time
import functions
import environment
import classes
import shutil
DEBUG = True
COMPANIES = 3

if DEBUG: startTime = time()
browser = functions.get_browser()
sleep(2)

# Login
browser.find_element_by_xpath('//*[@id="username"]').send_keys(environment.username)
browser.find_element_by_xpath('//*[@id="password"]').send_keys(environment.password)
browser.find_element_by_xpath('//*[@id="login"]/section[4]/button').click()

# Arrive at Market Activity Page
browser.find_element_by_xpath(".//a[contains(text(), 'Company Research')]").click()
browser.find_elements_by_xpath(".//a[contains(text(), 'view all')]")[0].click()
    # first "view all" text corresponds to Main Board
browser.find_elements_by_css_selector('td > a')[25].click()
    # 26th a tag corresponds to sorting by marketcap descending order

html = browser.page_source
htmlSoup = BeautifulSoup(html,'lxml')

#stocksSoup = htmlSoup.find_all('td', {'class' : 'text'}, limit=None)
stocksSoup = htmlSoup.find_all('a', {'class' : 'text'}, limit=COMPANIES)
stockNames = []
for stock in stocksSoup :
    stockNames.append(stock.getText())

stockDataArray = []

for stock in stockNames :
    if DEBUG: print("Current Stock: " + stock)
    # Arrive at Summary & Ratios page and pull ratio information
    browser.find_element_by_link_text(stock).click()
    stockSoup = BeautifulSoup(browser.page_source, 'lxml')
    if DEBUG: print("Pulling ratio information")
    stockSummaryDict = functions.get_stock_summary(stockSoup)

    csvLink = functions.create_historical_prices_csv_link(stockSummaryDict)
    browser.get(csvLink)
    sleep(3)
    stockHistoricalPricesDictionary = functions.get_stock_historical_prices(environment.tempDirectory + stockSummaryDict["Ticker"] + " Historical Prices.csv")

    # Arrive at Company Directory and pull directors information

    # Arrive at Company Profile and pull description information

    # Arrive at Annual Reports and pull latest annual report

    # Arrive at Dividends and pull dividend information
    # Link Sample: https://companyresearch-nzx-com.ezproxy.aut.ac.nz/deep_ar/divhistory_csv.php?selection=TLS
    csvLink = functions.create_historical_dividends_csv_link(stockSummaryDict["Ticker"])
    browser.get(csvLink)
    sleep(3)
    stockHistoricalDividendsDictionary = functions.get_stock_historical_dividends(environment.tempDirectory + stockSummaryDict["Ticker"] + " Historical Dividends.csv")

    # Arrive at Financial Profile and pull debt-equity information
    browser.find_element_by_xpath(".//span[contains(text(), 'Financial Profile')]").click()
    stockSoup = BeautifulSoup(browser.page_source, 'lxml')
    if DEBUG: print("Pulling ratio information")
    browser.execute_script("window.history.go(-1)")
    stockFinancialProfileDictionary = functions.get_financial_profile(stockSoup)

    # Create the stock obj and store it in an array
    stockData = classes.Stock(stockSummaryDict, stockHistoricalPricesDictionary, 
                                stockHistoricalDividendsDictionary, stockFinancialProfileDictionary)
    stockDataArray.append(stockData)

    # BACK
    browser.execute_script("window.history.go(-1)")

if DEBUG: print("Scraping complete")
browser.quit()
if DEBUG: print("Temporary files deleted")
shutil.rmtree(environment.downloadDirectory)

functions.print_excel(stockDataArray)

print("Excel ready")

if DEBUG: endTime = time()
if DEBUG: print("That took a total of: " + str(round(endTime-startTime)) + " seconds.")
if DEBUG: print(str(round((endTime-startTime)/COMPANIES)) + " seconds per company.")