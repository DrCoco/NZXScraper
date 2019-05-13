import pandas
from datetime import datetime, timedelta
from numpy import loadtxt
import csv
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from nzxscraper.environment import *
from nzxscraper.classes import Stock
from bs4 import BeautifulSoup
from time import sleep
from nzxscraper import logger

def get_browser() :
    """
    Creates a chrome driver which will be used by selenium to conduct the website navigation
    Sets the following options to aid in webscraping
        - Auto file download
        - Removal the images
        - Disables internal pdf viewer

    Returns:
        webdriver: Driver for site navigation
    """
    # Set up driver options
    chromeOptions = Options()
    chromeOptions.add_argument('log-level=3') # Remove warnings
    # chromeOptions.add_argument('headless')
    # chromeOptions.add_argument("--proxy-server='direct://'")
    # chromeOptions.add_argument("--proxy-bypass-list=*")
    # chromeOptions.add_argument('--no-proxy-server')
    prefs = {"download.default_directory": downloadDirectory , # Sets default directory for downloads
            "directory_upgrade": True, # Provides write permissions to the directory
			"plugins.always_open_pdf_externally": True, # Disables the built-in pdf viewer (Helps with pdf download)
            "safebrowsing.enabled": True, # Tells  driver all file downloads and sites are safe
            "download.prompt_for_download": False, # Auto downloads files into default directory
            "profile.managed_default_content_settings.images":2 } # Removes images for faster load times
    chromeOptions.add_experimental_option("prefs",prefs)
    browser = webdriver.Chrome(chromeDriverLocation, chrome_options = chromeOptions) # Apply options
    homeURL = "https://library.aut.ac.nz/databases/nzx-deep-archive"

    browser.get(homeURL)

    delay = 15 # seconds
    # Wait 15 seconds for the driver to get started and get to the landing page
    try:
        myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, "form-field")))
        logger.info("Browser is ready!")
    except TimeoutException:
        logger.error("Loading took too much time!")
    logger.info("get_browser() complete")
    return browser

def get_stock_summary(stockSoup) :
    """
    Gets the stock summary information including
        - Name
        - Price
        - Market Cap
        - Price Earnings Ratio
        - Price Change
        - Ticker
        - Earnings per Share
        - Net Tangible Assets
        - Net DPS
        - Gross DPS
        - Beta Value
        - Price/NTA
        - Net Yield
        - Gross Yield
        - Sharpe Ratio

    Args:
        param1 (BeautifulSoup): The parsed page source of the summary page.

    Returns:
        dict: A dictionary which contains all the information captured on this page
    """

    summaryDict = {}
    summaryDict["Name"] = (stockSoup.find('h1').text).split(' -')[0]
    summaryDict["Price"] = stockSoup.find('td', text= 'Market Price').find_next_sibling('td').text
    summaryDict["Market Cap"] = stockSoup.find('td', text= 'Marketcap').find_next_sibling('td').text
    summaryDict["Price Earnings Ratio"] = stockSoup.find('td', text= 'P/E ratio').find_next_sibling('td').text
    summaryDict["Price Change"] = stockSoup.find('td', text= 'Price Change').find_next('td').text
    summaryDict["Ticker"] = stockSoup.find('td', text= 'Ticker').find_next_sibling('td').text
    summaryDict["EPS"] = stockSoup.find('td', text= 'EPS').find_next('td').text
    summaryDict["NTA"] = stockSoup.find('td', text= 'NTA').find_next_sibling('td').text
    summaryDict["Net DPS"] = stockSoup.find('td', text= 'Net DPS').find_next_sibling('td').text
    summaryDict["Gross DPS"] = stockSoup.find('td', text= 'Gross DPS').find_next_sibling('td').text
    summaryDict["Beta Value"] = stockSoup.find('td', text= 'Beta Value').find_next_sibling('td').text
    summaryDict["Price/NTA"] = stockSoup.find('td', text= 'Price/NTA').find_next_sibling('td').text
    summaryDict["Net Yield"] = stockSoup.find('td', text= 'Net Yield').find_next_sibling('td').text
    summaryDict["Gross Yield"] = stockSoup.find('td', text= 'Gross Yield').find_next_sibling('td').text
    summaryDict["Sharpe Ratio"] = stockSoup.find('td', text= 'Sharpe Ratio').find_next_sibling('td').text

    logger.debug(summaryDict)
    return summaryDict

def create_historical_prices_csv_link(stockSummaryDict) :
    fromDate = (datetime.now() - timedelta(days=365*3)).strftime('%Y-%m-%d')
    toDate = datetime.now().strftime('%Y-%m-%d')
    csvLink =  "https://companyresearch-nzx-com.ezproxy.aut.ac.nz/deep_ar/functions/csv_prices.php?"
    csvLink += ("default=" + stockSummaryDict["Ticker"] + "&" + "fd=" + fromDate + "&" + "td=" + toDate)
    logger.info("Pulling historical price data from: " + csvLink)
    return csvLink

def create_historical_dividends_csv_link(stockTicker) :
    csvLink = "https://companyresearch-nzx-com.ezproxy.aut.ac.nz/deep_ar/divhistory_csv.php?selection=" + stockTicker
    logger.info("Pulling historical dividend data from: " + csvLink)
    return csvLink

def get_stock_historical_prices(stockHistoricalPricesCSV) :
    logger.debug(pandas.read_csv(stockHistoricalPricesCSV))
    return pandas.read_csv(stockHistoricalPricesCSV).to_dict('r')

def get_director_information(directorSoup):
    tableData = directorSoup.find_all('table')[13]
    # print(tableData[0])
    # print(len(tableData))
    directorDict = {}
    directorTableData = [[ td.text for td in row.select('td')]
                         for row in tableData.find_all('tr')]
    for item in directorTableData:
        directorDict[item[0]] = item[1]

    return directorDict

def get_stock_historical_dividends(stockHistoricalDividendsCSV) :
    logger.debug(pandas.read_csv(stockHistoricalDividendsCSV))
    dividendDF = pandas.read_csv(stockHistoricalDividendsCSV)
    dividendDF = dividendDF.dropna()
    try:
        dividendDF = dividendDF[['Ex Date', 'Gross Amount']]
        dividendDF.columns = ['Date', 'Dividend Paid']
        dividendDF = dividendDF[dividendDF['Dividend Paid'] != '-']
        return dividendDF.to_dict('r')
    except:
        logger.warning("No dividend information")
        return None

def get_financial_profile(stockSoup) :
    tables = stockSoup.find_all('table')
    incomeTableHeaders = [item.get_text()[1:-1] for item in tables[7].find_all('tr')]
    incomeTableData =    [[ td.text for td in row.select('td')]
                        for row in tables[8].find_all('tr')]

    balanceTableHeaders = [item.get_text() for item in tables[11].find_all('td')]
    balanceTableData = [[ td.text for td in row.select('td')]
                        for row in tables[12].find_all('tr')]

    cashTableHeaders = [item.get_text() for item in tables[15].find_all('td')]
    cashTableData = [[ td.text for td in row.select('td')]
                        for row in tables[16].find_all('tr')]

    financialProfileDict = {}

    for item in incomeTableHeaders:
        financialProfileDict[item] = incomeTableData[incomeTableHeaders.index(item)][0]

    for item in balanceTableHeaders:
        financialProfileDict[item] = balanceTableData[balanceTableHeaders.index(item)][0]

    for item in cashTableHeaders:
        financialProfileDict[item] = cashTableData[cashTableHeaders.index(item)][0]

    return financialProfileDict

def get_company_profile(profileSoup):
    companyProfileDict = {}
    # Put all table rows into a list.
    profList = profileSoup.find_all("tr", 'heading')
    
    #profList[1] is the business description header. Store business description in Dictionary
    companyProfileDict[profList[1].text] = profList[1].find_next_sibling('tr').td.text 
    #profList[2] is the overview header. Store in Dictionary
    companyProfileDict[profList[2].text] = profList[2].find_next_sibling('tr').td.text
    #profList[3] is the Performance header. Store in Dictionary
    companyProfileDict[profList[3].text] = profList[3].find_next_sibling('tr').td.text
    #profList[4] is the Outlook header. Store in Dictionary
    companyProfileDict[profList[4].text] = profList[4].find_next_sibling('tr').td.text
    return companyProfileDict

def list_companies(browser):
    # Login
    browser.find_element_by_xpath('//*[@id="username"]').send_keys(username)
    browser.find_element_by_xpath('//*[@id="password"]').send_keys(password)
    browser.find_element_by_xpath('//*[@id="login"]/section[4]/button').click()
    logger.info("Logged into NZX System")

    # Arrive at Market Activity Page
    browser.find_element_by_xpath(".//a[contains(text(), 'Company Research')]").click()
    logger.info("Arrived at Market Activity Page")
    # Click "View all" for main market
    browser.find_elements_by_xpath(".//a[contains(text(), 'view all')]")[0].click()
    logger.info("Arrived at Market Overview Page")
    # Sort in descending order by clicking the 26th "a" tag
    browser.find_elements_by_css_selector('td > a')[25].click()
    logger.info("Arrived at Market Overview sorted by marketcap in descending order")

    # Parse the page source into BeautifulSoup
    # The page is the list of stocks in Descending order of Market Cap
    html = browser.page_source
    htmlSoup =   BeautifulSoup(html,'lxml')
    logger.info("Market Overview Page parsed")

    # Put all the stock tickers into a list
    stocksSoup = htmlSoup.find_all('a', {'class' : 'text'}, limit=COMPANIES)
    stockNames = ['ATM']
    # for stock in stocksSoup :
    #     stockNames.append(stock.getText())

    logger.info("List of companies to scrape finalised")
    return stockNames

def scrape_company(browser, stock):
    logger.info("Current Stock: " + stock)

    # Arrive at Summary & Ratios page and pull information
    browser.find_element_by_link_text(stock).click()
    summarySoup = BeautifulSoup(browser.page_source, 'lxml')
    logger.info("Pulling ratio information")
    stockSummaryDict = get_stock_summary(summarySoup)

    # Arrive at Company Directory and pull directors information
    browser.find_element_by_xpath(".//span[contains(text(), 'Company Directory')]").click()
    directorSoup = BeautifulSoup(browser.page_source, 'lxml')
    logger.info("Pulling Director's information")
    stockDirectorDict = get_director_information(directorSoup)
    browser.execute_script("window.history.go(-1)") # Go back to summary page

    # Arrive at Company Profile and pull description information
    browser.find_element_by_xpath(".//span[contains(text(), 'Company Profile')]").click()
    profileSoup = BeautifulSoup(browser.page_source, 'lxml')
    logger.info("Pulling company description")
    stockProfileDict = get_company_profile(profileSoup)
    logger.debug(stockProfileDict)
    browser.execute_script("window.history.go(-1)") # Go back to summary page

    # Arrive at Financial Profile and pull debt-equity information
    browser.find_element_by_xpath(".//span[contains(text(), 'Financial Profile')]").click()
    stockSoup = BeautifulSoup(browser.page_source, 'lxml')
    logger.info("Pulling financial profile information")
    stockFinancialProfileDict = get_financial_profile(stockSoup)
    browser.execute_script("window.history.go(-1)") # Go back to summary page

    # Arrive at Annual Reports and pull latest annual report
    # ? May require refactor of xpath to shorten it (Looks nicer)
    # TODO change dl directory outside temp
    browser.find_element_by_xpath(".//span[contains(text(), 'Annual Reports')]").click()
    logger.info("Pulling annual report")
    browser.find_element_by_xpath(r"""//*[@id="content"]/center/table/tbody/tr[3]/td/table/tbody/tr[2]/
                                      td[2]/table/tbody/tr/td/table[2]/tbody/tr[1]/td[1]/table/tbody/
                                      tr[1]/td[2]/form/input""").click()
    # sleep(10)
    browser.execute_script("window.history.go(-1)") # Go back to summary page

    # Arrive at Tear Sheet and pull latest tear sheet
    browser.find_element_by_xpath(".//span[contains(text(), 'Tear Sheet')]").click()
    logger.info("Pulling tear sheet")
    browser.find_element_by_xpath(r"""//*[@id="content"]/center/table/tbody/tr[3]/td/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr/td/p[2]/a""").click()
    # sleep(10)
    browser.execute_script("window.history.go(-1)") # Go back

    # Create csv link for historical prices and pull it into a temporary folder
    csvLink = create_historical_prices_csv_link(stockSummaryDict)
    logger.info("Pulling historical prices information")
    browser.get(csvLink)
    sleep(3)
    stockHistoricalPricesDict = get_stock_historical_prices(
                                tempDirectory + stockSummaryDict["Ticker"]
                                + " Historical Prices.csv")

    # Create csv link for dividends and pull it into a temporary folder
    csvLink = create_historical_dividends_csv_link(stockSummaryDict["Ticker"])
    logger.info("Pulling historical dividends information")
    browser.get(csvLink)
    sleep(3)
    stockHistoricalDividendsDict = get_stock_historical_dividends(
                                   tempDirectory + stockSummaryDict["Ticker"]
                                   + " Historical Dividends.csv")

    # Go back to the stock ticker page
    logger.info("Back to company listings")
    browser.execute_script("window.history.go(-1)")

    # Create the stock obj and store it in an array
    stockData = Stock(stockSummaryDict, stockHistoricalPricesDict,
                              stockHistoricalDividendsDict, stockFinancialProfileDict,
                              stockProfileDict, stockDirectorDict)

    return stockData

