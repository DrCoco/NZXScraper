import classes
import xlsxwriter
import pandas as pd
import wget
import datetime
DEBUG = True

def get_stock_summary(stockSoup) :
    return classes.StockSummary((
        stockSoup.find('h1').text).split('-')[0], #Name
        stockSoup.find('td', text= 'Market Price').find_next_sibling('td').text, # Price
        stockSoup.find('td', text= 'Marketcap').find_next_sibling('td').text, # Market Cap
        stockSoup.find('td', text= 'P/E ratio').find_next_sibling('td').text, # PE Ratio
        stockSoup.find('td', text= 'Price Change').find_next('td').text, #Price Change
        stockSoup.find('td', text= 'Ticker').find_next_sibling('td').text, # Ticker
        stockSoup.find('td', text= 'EPS').find_next('td').text, #EPS
        stockSoup.find('td', text= 'NTA').find_next_sibling('td').text,  #NTA
        stockSoup.find('td', text= 'Net DPS').find_next_sibling('td').text, # NetDPS
        stockSoup.find('td', text= 'Gross DPS').find_next_sibling('td').text, # GrossDPS
        stockSoup.find('td', text= 'Beta Value').find_next_sibling('td').text, # BetaValue
        stockSoup.find('td', text= 'Price/NTA').find_next_sibling('td').text, # PriceNTA
        stockSoup.find('td', text= 'Net Yield').find_next_sibling('td').text, # NetYield
        stockSoup.find('td', text= 'Gross Yield').find_next_sibling('td').text, # GrossYield
        stockSoup.find('td', text= 'Sharpe Ratio').find_next_sibling('td').text # SharpeRatio
    )

def print_excel(stockDataArray) :
    if DEBUG: print("Printing excel document")
    workbook = xlsxwriter.Workbook('StockApp.xlsx')

    if DEBUG: print("Printing Overview")
    overviewSheet = workbook.add_worksheet("Overview")
    overviewSheet.write_string(0,0, "Stocks")
    row = 1
    col = 0
    for stock in stockDataArray :
        overviewSheet.write_url(row, col, "internal:" + stock.stockSummary.stockTicker + "_Summary!A1",string = stock.stockSummary.stockName)
        row += 1
    
    if DEBUG: print("   Printing Summary & Ratios")
    for stock in stockDataArray :
        if DEBUG: print("       Printing Summary & Ratios for " + stock.stockSummary.stockTicker)
        row = 0
        col = 0
        # money_format = workbook.add_format({'num_format': '$#,##0'})
        # number2dec_format = workbook.add_format({'num_format': '#.##'})
        worksheet = workbook.add_worksheet(stock.stockSummary.stockTicker + "_Summary")
        worksheet.write_string(row, col, "Stock Name:")
        worksheet.write_string(row, col+2, stock.stockSummary.stockName)
        worksheet.write_string(row+1, col, "Stock Ticker:")
        worksheet.write_string(row+1, col+2, stock.stockSummary.stockTicker)
        worksheet.write_string(row+2, col, "Stock Price:")
        worksheet.write_string(row+2, col+2, stock.stockSummary.stockPrice)
        worksheet.write_string(row+3, col, "Stock Marketcap:")
        worksheet.write_string(row+3, col+2, stock.stockSummary.stockMarketcap)
        worksheet.write_string(row+4, col, "Stock Price Change:")
        worksheet.write_string(row+4, col+2, stock.stockSummary.stockPriceChange)
        worksheet.write_string(row+5, col, "Stock Net Yield:")
        worksheet.write_string(row+5, col+2, stock.stockSummary.stockNetYield)
        worksheet.write_string(row+6, col, "Stock PE Ratio:")
        worksheet.write_string(row+6, col+2, stock.stockSummary.stockPERatio)
        worksheet.write_url(row, col+5, "internal:Overview!A1",string = "BACK")
        worksheet.write_url(row, col+7, "internal:"+stock.stockSummary.stockTicker+"_HistoricalPrices!A1",string = "Historical Prices")
    
    if DEBUG: print("   Printing Historical Prices ")
    for stock in stockDataArray:      
        if DEBUG: print("       Printing Historical Prices for " + stock.stockSummary.stockTicker)  
        row = 0
        col = 0
        dateFormat = workbook.add_format({'num_format': 'd mmm yyyy'})
        datesList = stock.stockHistoricalPrices['Date'].tolist()
        bidList = stock.stockHistoricalPrices['Bid'].tolist()
        askList = stock.stockHistoricalPrices['Ask'].tolist()
        firstList = stock.stockHistoricalPrices['First'].tolist()
        highList = stock.stockHistoricalPrices['High'].tolist()
        lowList = stock.stockHistoricalPrices['Low'].tolist()
        lastList = stock.stockHistoricalPrices['Last'].tolist()
        changeList = stock.stockHistoricalPrices['Change'].tolist()
        capitalAdjustedList = stock.stockHistoricalPrices['Capital Adjusted'].tolist()
        volumeTradedList = stock.stockHistoricalPrices['Volume Traded'].tolist()
        dollarValueTradedList = stock.stockHistoricalPrices['$ Value Traded'].tolist()
        tradesList = stock.stockHistoricalPrices['Trades'].tolist()

        # Write headers
        worksheet = workbook.add_worksheet(stock.stockSummary.stockTicker + "_HistoricalPrices")
        worksheet.write_string(row, col, "Date")
        worksheet.write_string(row, col+1, "Bid")
        worksheet.write_string(row, col+2, "Ask")
        worksheet.write_string(row, col+3, "First")
        worksheet.write_string(row, col+4, "High")
        worksheet.write_string(row, col+5, "Low")
        worksheet.write_string(row, col+6, "Last")
        worksheet.write_string(row, col+7, "Change")
        worksheet.write_string(row, col+8, "Capital Adjusted")
        worksheet.write_string(row, col+9, "Volume Traded")
        worksheet.write_string(row, col+10, "$ Value Traded")
        worksheet.write_string(row, col+11, "Trades")

        worksheet.write_url(row, col+13, "internal:"+stock.stockSummary.stockTicker+"_Summary!A1",string = "BACK")
        row += 1

        for i in range(len(datesList)):
            worksheet.write_datetime(row, col, datetime.datetime.strptime(datesList[i],'%d %b %Y'), dateFormat)
            worksheet.write_number(row,col+1, bidList[i])
            worksheet.write_number(row,col+2, askList[i])
            worksheet.write_number(row,col+3, firstList[i])
            worksheet.write_number(row,col+4, highList[i])
            worksheet.write_number(row,col+5, lowList[i])
            worksheet.write_number(row,col+6, lastList[i])
            worksheet.write_number(row,col+7, changeList[i])
            worksheet.write_number(row,col+8, capitalAdjustedList[i])
            worksheet.write_number(row,col+9, volumeTradedList[i])
            worksheet.write_number(row,col+10, dollarValueTradedList[i])
            worksheet.write_number(row,col+11, tradesList[i])
            row += 1

    workbook.close()



def get_stock_historical_prices(stockHistoricalPricesCSV) :
    return pd.read_csv(stockHistoricalPricesCSV)