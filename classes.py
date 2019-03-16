class StockSummary:
    def __init__(self, stockName,
                       stockPrice,
                       stockMarketcap,
                       stockPERatio,
                       stockPriceChange,
                       stockTicker,
                       stockEPS,
                       stockNTA,
                       stockNetDPS,
                       stockGrossDPS,
                       stockBetaValue,
                       stockPriceNTA,
                       stockNetYield,
                       stockGrossYield,
                       stockSharpeRatio):
        self.stockName = stockName
        self.stockTicker = stockTicker
        self.stockPrice = stockPrice
        self.stockMarketcap = stockMarketcap
        self.stockPERatio = stockPERatio
        self.stockPriceChange = stockPriceChange
        self.stockEPS = stockEPS
        self.stockNTA = stockNTA
        self.stockNetDPS =   stockNetDPS
        self.stockGrossDPS = stockGrossDPS
        self.stockBetaValue = stockBetaValue
        self.stockPriceNTA = stockPriceNTA
        self.stockNetYield = stockNetYield
        self.stockGrossYield = stockGrossYield
        self.stockSharpeRatio = stockSharpeRatio
    def __str__(self):
        return str(self.__dict__)

class Stock:
    def __init__(self, stockSummary) :
        self.stockSummary = stockSummary

    def __str__(self):
        return str(self.__dict__)
