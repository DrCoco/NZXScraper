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
sleep(2000)

# Login
browser.find_element_by_xpath('//*[@id="username"]').send_keys(environment.username)
browser.find_element_by_xpath('//*[@id="password"]').send_keys(environment.password)
browser.find_element_by_xpath('//*[@id="login"]/section[4]/button').click()

# Arrive at Market Activity Page
browser.find_element_by_xpath(".//a[contains(text(), 'Company Research')]").click()
    # Click "View all" for main market
browser.find_elements_by_xpath(".//a[contains(text(), 'view all')]")[0].click()
    # Sort in descending order by clicking the 26th "a" tag
browser.find_elements_by_css_selector('td > a')[25].click()

# Parse the page source into BeautifulSoup 
# The page is the list of stocks in Descending order of Market Cap
html = browser.page_source
htmlSoup =   BeautifulSoup(html,'lxml')

# Put all the stock tickers into a list
stocksSoup = htmlSoup.find_all('a', {'class' : 'text'}, limit=1)
stockNames = []
for stock in stocksSoup :
    stockNames.append(stock.getText())

# Initialise the array which is  going to store Stock class objects
stockDataArray = []

# For each ticker in the list, find the link to the respective summary page
for stock in stockNames :
    if DEBUG: print("Current Stock: " + stock)

    # Arrive at Summary & Ratios page and pull information
    browser.find_element_by_link_text(stock).click() 
    summarySoup = BeautifulSoup(browser.page_source, 'lxml')
    if DEBUG: print("Pulling ratio information")
    stockSummaryDict = functions.get_stock_summary(summarySoup)

    # Create csv link for historical prices and pull it into a temporary folder
    csvLink = functions.create_historical_prices_csv_link(stockSummaryDict)
    browser.get(csvLink)
    sleep(3)
    stockHistoricalPricesDict = functions.get_stock_historical_prices(environment.tempDirectory + stockSummaryDict["Ticker"] + " Historical Prices.csv")

    # Arrive at Company Directory and pull directors information
    browser.find_element_by_xpath(".//span[contains(text(), 'Company Directory')]").click()
    directorSoup = BeautifulSoup(browser.page_source, 'lxml')
    if DEBUG: print("Pulling Director's information")
    stockDirectorDict = functions.get_director_information(directorSoup)
    browser.execute_script("window.history.go(-1)") # Go back

    # Arrive at Company Profile and pull description information
    browser.find_element_by_xpath(".//span[contains(text(), 'Company Profile')]").click()
    profileSoup = BeautifulSoup(browser.page_source, 'lxml')
    if DEBUG: print("Pulling company description")
    stockProfileDict = functions.get_company_profile(profileSoup)
    if DEBUG: print(stockProfileDict)
    browser.execute_script("window.history.go(-1)") # Go back

    # Arrive at Annual Reports and pull latest annual report
    # ? May require refactor of xpath to shorten it
    browser.find_element_by_xpath(".//span[contains(text(), 'Annual Reports')]").click()
    browser.find_element_by_xpath(r"""//*[@id="content"]/center/table/tbody/tr[3]/td/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[2]/tbody/tr[1]/td[1]/table/tbody/tr[1]/td[2]/form/input""").click()
    browser.execute_script("window.history.go(-1)") # Go back

    #  Arrive at tearsheet and pull pdf
    browser.find_element_by_xpath(".//span[contains(text(), 'Tear Sheet')]").click()
    browser.find_element_by_xpath(r"""//*[@id="content"]/center/table/tbody/tr[3]/td/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr/td/p[2]/a""").click()
    browser.execute_script("window.history.go(-1)") # Go back


    # Create csv link for dividends and pull it into a temporary folder
    csvLink = functions.create_historical_dividends_csv_link(stockSummaryDict["Ticker"])
    browser.get(csvLink)
    sleep(3)
    stockHistoricalDividendsDict = functions.get_stock_historical_dividends(environment.tempDirectory + stockSummaryDict["Ticker"] + " Historical Dividends.csv")

    # Arrive at Financial Profile and pull debt-equity information
    browser.find_element_by_xpath(".//span[contains(text(), 'Financial Profile')]").click()
    stockSoup = BeautifulSoup(browser.page_source, 'lxml')
    if DEBUG: print("Pulling ratio information")
    stockFinancialProfileDict = functions.get_financial_profile(stockSoup)
    browser.execute_script("window.history.go(-1)")

    # Create the stock obj and store it in an array
    stockData = classes.Stock(stockSummaryDict, stockHistoricalPricesDict,
                                stockHistoricalDividendsDict, stockFinancialProfileDict, stockProfileDict, stockDirectorDict)
    stockDataArray.append(stockData)

    # Go back to the stock ticker page
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
