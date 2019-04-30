import classes
import xlsxwriter
import pandas
from datetime import datetime, timedelta
from numpy import loadtxt
DEBUG = True
import csv
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
import environment
from bs4 import BeautifulSoup

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
    prefs = {"download.default_directory": environment.downloadDirectory , # Sets default directory for downloads
            "directory_upgrade": True, # Provides write permissions to the directory
			"plugins.always_open_pdf_externally": True, # Disables the built-in pdf viewer (Helps with pdf download)
            "safebrowsing.enabled": True, # Tells  driver all file downloads and sites are safe
            "download.prompt_for_download": False, # Auto downloads files into default directory
            "profile.managed_default_content_settings.images":2 } # Removes images for faster load times
    chromeOptions.add_experimental_option("prefs",prefs)
    browser = webdriver.Chrome(environment.chromeDriverLocation, chrome_options = chromeOptions) # Apply options
    homeURL = "https://library.aut.ac.nz/databases/nzx-deep-archive"

    browser.get(homeURL)

    delay = 15 # seconds
    # Wait 15 seconds for the driver to get started and get to the landing page
    try:
        myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, "form-field")))
        if DEBUG: print ("Page is ready!")
    except TimeoutException:
        print ("Loading took too much time!")
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

    if DEBUG: print(summaryDict)
    return summaryDict

def create_historical_prices_csv_link(stockSummaryDict) :
    fromDate = (datetime.now() - timedelta(days=365*3)).strftime('%Y-%m-%d')
    toDate = datetime.now().strftime('%Y-%m-%d')
    csvLink =  "https://companyresearch-nzx-com.ezproxy.aut.ac.nz/deep_ar/functions/csv_prices.php?"
    csvLink += ("default=" + stockSummaryDict["Ticker"] + "&" + "fd=" + fromDate + "&" + "td=" + toDate)
    if DEBUG: print("Pulling historical price data from: " + csvLink)
    return csvLink

def create_historical_dividends_csv_link(stockTicker) :
    return "https://companyresearch-nzx-com.ezproxy.aut.ac.nz/deep_ar/divhistory_csv.php?selection=" + stockTicker

def print_overview_sheet(workbook,stockDataArray, formats) :
    if DEBUG: print("Printing Overview")
    overviewSheet = workbook.add_worksheet("Overview")
    overviewSheet.write_string(0,0, "Stocks")
    row = 1
    col = 0
    for stock in stockDataArray :
        overviewSheet.write_url(row, col, "internal:" + stock.stockSummaryDict["Ticker"] + "_Summary!A1",string = stock.stockSummaryDict["Name"])
        row += 1

def print_summary_sheet(workbook,stock, formats) :
    if DEBUG: print("       Printing Summary & Ratios for " + stock.stockSummaryDict["Ticker"])
    row = 0
    col = 0
    worksheet = workbook.add_worksheet(stock.stockSummaryDict["Ticker"] + "_Summary")
    for key, value in stock.stockSummaryDict.items():
        worksheet.write_string(row, col, key)
        worksheet.write_string(row, col+2, value)
        row += 1

    worksheet.write_url(0, col+5, "internal:Overview!A1",string = "BACK")
    worksheet.write_url(0, col+7, "internal:"+stock.stockSummaryDict["Ticker"]+"_HistoricalPrices!A1",string = "Historical Prices")

def print_historical_prices_sheet(workbook, stock, formats) :
    if DEBUG: print("       Printing Historical Prices for " + stock.stockSummaryDict["Ticker"])
    row = 0
    col = 0

    # Create sheet
    worksheet = workbook.add_worksheet(stock.stockSummaryDict["Ticker"]+"_HistoricalPrices")
    # Print Headers
    keys = stock.stockHistoricalPrices[0].keys()
    for key in keys :
        worksheet.write_string(row, col, key)
        col += 1
    worksheet.write_url(row, col+13, "internal:"+stock.stockSummaryDict["Ticker"]+"_Summary!A1",string = "BACK")

    row = 1
    col = 0

    # Print Items
    for rowItems in stock.stockHistoricalPrices:
        #print(rowItems)
        for key, value in rowItems.items():
            #print(value)
            if (key == 'Date') :
                worksheet.write_datetime(row, col, datetime.strptime(value,'%d %b %Y'), formats['dateFormat'])
            else :
                worksheet.write_number(row, col, value)
            col += 1
        row += 1
        col = 0

def print_excel(stockDataArray) :
    if DEBUG: print("Printing excel document")
    # Create excel workbook
    workbook = xlsxwriter.Workbook('StockDB.xlsx')

    # Excel Cell Formats
    formats = {}
    formats['dateFormat'] = workbook.add_format({'num_format': 'd mmm yyyy'})
    formats['moneyFormat'] = workbook.add_format({'num_format': '$#,##0'})
    formats['number2decFormat'] = workbook.add_format({'num_format': '#.##'})

    print_overview_sheet(workbook, stockDataArray, formats)

    for stock in stockDataArray :
        print_summary_sheet(workbook, stock, formats)
        print_historical_prices_sheet(workbook, stock, formats)
        print_Directors(workbook, stock, formats)
        print_company_profile(workbook, stock, formats)
        print_historical_dividends_sheet(workbook, stock, formats)
        print_financial_profile_sheet(workbook, stock, formats)

    workbook.close()

def print_historical_dividends_sheet(workbook, stock, formats) :
    if DEBUG: print("       Printing Historical Dividends for " + stock.stockSummaryDict["Ticker"])
    row = 0
    col = 0

    # Create sheet
    worksheet = workbook.add_worksheet(stock.stockSummaryDict["Ticker"]+"_HistoricalDividends")
    # Print Headers
    keys = stock.stockHistoricalDividends[0].keys()
    for key in keys :
        worksheet.write_string(row, col, key)
        col += 1
    worksheet.write_url(row, col+13, "internal:"+stock.stockSummaryDict["Ticker"]+"_Summary!A1",string = "BACK")

    row = 1
    col = 0

    # Print Items
    for rowItems in stock.stockHistoricalDividends:
        if DEBUG: print(rowItems)
        for key, value in rowItems.items():
            if DEBUG: print(value)
            if (key == 'Date') :
                worksheet.write_datetime(row, col, datetime.strptime(value,'%d %b %Y'), formats['dateFormat'])
            else :
                worksheet.write_number(row, col, float(value))
            col += 1
        row += 1
        col = 0

def get_stock_historical_prices(stockHistoricalPricesCSV) :
    if DEBUG: print(pandas.read_csv(stockHistoricalPricesCSV))
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

def print_Directors(workbook, stock, format) :
    row = 0
    col = 0
    worksheet = workbook.add_worksheet(stock.stockSummaryDict["Ticker"] + "_Directors")
    for key, value in stock.stockDirectorDict.items():
        worksheet.write_string(row, col, key)
        worksheet.write_string(row, col+2, value)
        row += 1

def get_stock_historical_dividends(stockHistoricalDividendsCSV) :
    dividendDF = pandas.read_csv(stockHistoricalDividendsCSV)
    dividendDF = dividendDF.dropna()
    dividendDF = dividendDF[['Ex Date', 'Gross Amount']]
    dividendDF.columns = ['Date', 'Dividend Paid']
    dividendDF = dividendDF[dividendDF['Dividend Paid'] != '-']
    return dividendDF.to_dict('r')

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

def print_financial_profile_sheet(workbook, stock, formats):
    if DEBUG: print("       Printing Financial Profile for " + stock.stockSummaryDict["Ticker"])
    row = 0
    col = 0

    # Create sheet
    worksheet = workbook.add_worksheet(stock.stockSummaryDict["Ticker"]+"_FinancialProfile")
    # Print Headers & Values
    keys = stock.stockFinancialProfile.keys()
    if DEBUG: print(keys)
    for key in keys :
        worksheet.write_string(row, col, key)
        row += 1
    worksheet.write_url(0, 13, "internal:"+stock.stockSummaryDict["Ticker"]+"_Summary!A1",string = "BACK")

def get_company_profile(profileSoup):
    companyProfileDict = {}
    # Put all table rows into a list.
    profList = profileSoup.find_all("tr", 'heading')
    if DEBUG: print("Pulling company profile information...")
    #profList[1] is the business description header. Store business description in Dictionary
    companyProfileDict[profList[1].text] = profList[1].find_next_sibling('tr').td.text 
    #profList[2] is the overview header. Store in Dictionary
    companyProfileDict[profList[2].text] = profList[2].find_next_sibling('tr').td.text
    #profList[3] is the Performance header. Store in Dictionary
    companyProfileDict[profList[3].text] = profList[3].find_next_sibling('tr').td.text
    #profList[4] is the Outlook header. Store in Dictionary
    companyProfileDict[profList[4].text] = profList[4].find_next_sibling('tr').td.text
    return companyProfileDict

def print_company_profile(workbook, stock, format) :
    row = 0
    col = 0
    worksheet = workbook.add_worksheet(stock.stockSummaryDict["Ticker"] + "_company_profile")
    for key, value in stock.stockCompanyProfile.items():
        worksheet.write_string(row, col, key)
        worksheet.write_string(row, col+2, value)
        row += 1

def print_dividends_info(workbook,dividendsDict,stock) :
    row = 0
    col = 0
    worksheet = workbook.add_worksheet(stock.stockSummaryDict["Ticker"] + "_dividends_info")
    for key, value in dividendsDict.items():
        worksheet.write_string(row, col, key)
        worksheet.write_string(row, col+2, value)
        row += 1
