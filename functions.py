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

def get_browser() :
    # Set up driver options
    chromeOptions = Options()
    chromeOptions.add_argument('log-level=3') # Remove warnings
    # prefs = {"profile.managed_default_content_settings.images":2} # Remove images to lower load times
    prefs = {"download.default_directory": environment.downloadDirectory ,
            "directory_upgrade": True,
            "safebrowsing.enabled": True,
            "download.prompt_for_download": False,
            "profile.managed_default_content_settings.images":2 }
    chromeOptions.add_experimental_option("prefs",prefs)
    browser = webdriver.Chrome(environment.chromeDriverLocation, chrome_options = chromeOptions) # Apply options
    homeURL = "https://library.aut.ac.nz/databases/nzx-deep-archive"

    browser.get(homeURL)

    delay = 15 # seconds
    try:
        myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, "form-field")))
        if DEBUG: print ("Page is ready!")
    except TimeoutException:
        print ("Loading took too much time!")
    return browser

def get_stock_summary(stockSoup) :
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

    workbook.close()



def get_stock_historical_prices(stockHistoricalPricesCSV) :
    if DEBUG: print(pandas.read_csv(stockHistoricalPricesCSV))
    return pandas.read_csv(stockHistoricalPricesCSV).to_dict('r')
