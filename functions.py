import classes

def getStockSummary(stockSoup) :
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