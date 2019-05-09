from nzxscraper.environment import DEBUG
import xlsxwriter
from datetime import datetime
from nzxscraper import logger

def print_overview_sheet(workbook,stockDataArray, formats) :
    logger.info("Printing Overview")
    overviewSheet = workbook.add_worksheet("Overview")
    overviewSheet.write_string(0,0, "Stocks")
    row = 1
    col = 0
    for stock in stockDataArray :
        overviewSheet.write_url(row, col, "internal:" + stock.stockSummaryDict["Ticker"] + "_Summary!A1",string = stock.stockSummaryDict["Name"])
        row += 1

def print_summary_sheet(workbook,stock, formats) :
    logger.info("       Printing Summary & Ratios for " + stock.stockSummaryDict["Ticker"])
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

    logger.info("       Printing Historical Prices for " + stock.stockSummaryDict["Ticker"])
    row = 0
    col = 0

    # Create sheet
    worksheet = workbook.add_worksheet(stock.stockSummaryDict["Ticker"]+"_HistoricalPrices")
    # Print Headers
    keys = stock.stockHistoricalPricesDict[0].keys()
    for key in keys :
        worksheet.write_string(row, col, key)
        col += 1
    worksheet.write_url(row, col+13, "internal:"+stock.stockSummaryDict["Ticker"]+"_Summary!A1",string = "BACK")

    row = 1
    col = 0

    # Print Items
    for rowItems in stock.stockHistoricalPricesDict:
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
    logger.info("Printing excel document")
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
    logger.info("       Printing Historical Dividends for " + stock.stockSummaryDict["Ticker"])
    row = 0
    col = 0

    # Create sheet
    worksheet = workbook.add_worksheet(stock.stockSummaryDict["Ticker"]+"_HistoricalDividends")
    # Print Headers
    keys = stock.stockHistoricalDividendsDict[0].keys()
    for key in keys :
        worksheet.write_string(row, col, key)
        col += 1
    worksheet.write_url(row, col+13, "internal:"+stock.stockSummaryDict["Ticker"]+"_Summary!A1",string = "BACK")

    row = 1
    col = 0

    # Print Items
    for rowItems in stock.stockHistoricalDividendsDict:
        logger.debug(rowItems)
        for key, value in rowItems.items():
            logger.debug(value)
            if (key == 'Date') :
                worksheet.write_datetime(row, col, datetime.strptime(value,'%d %b %Y'), formats['dateFormat'])
            else :
                worksheet.write_number(row, col, float(value))
            col += 1
        row += 1
        col = 0

def print_Directors(workbook, stock, format) :
    row = 0
    col = 0
    worksheet = workbook.add_worksheet(stock.stockSummaryDict["Ticker"] + "_Directors")
    for key, value in stock.stockDirectorDict.items():
        worksheet.write_string(row, col, key)
        worksheet.write_string(row, col+2, value)
        row += 1

def print_financial_profile_sheet(workbook, stock, formats):
    logger.info("       Printing Financial Profile for " + stock.stockSummaryDict["Ticker"])
    row = 0
    col = 0

    # Create sheet
    worksheet = workbook.add_worksheet(stock.stockSummaryDict["Ticker"]+"_FinancialProfile")
    # Print Headers & Values
    keys = stock.stockFinancialProfileDict.keys()
    logger.debug(keys)
    for key in keys :
        worksheet.write_string(row, col, key)
        row += 1
    worksheet.write_url(0, 13, "internal:"+stock.stockSummaryDict["Ticker"]+"_Summary!A1",string = "BACK")

def print_company_profile(workbook, stock, format) :
    row = 0
    col = 0
    worksheet = workbook.add_worksheet(stock.stockSummaryDict["Ticker"] + "_company_profile")
    for key, value in stock.stockCompanyProfileDict.items():
        worksheet.write_string(row, col, key)
        worksheet.write_string(row, col+2, value)
        row += 1

def print_dividends_info(workbook,dividendsDict,stock) :
    if dividendsDict is not None:
        row = 0
        col = 0
        worksheet = workbook.add_worksheet(stock.stockSummaryDict["Ticker"] + "_dividends_info")
        for key, value in dividendsDict.items():
            worksheet.write_string(row, col, key)
            worksheet.write_string(row, col+2, value)
            row += 1