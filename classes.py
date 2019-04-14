class Stock:
    def __init__(self, stockSummaryDict, stockHistoricalPrices) :
        self.stockSummaryDict = stockSummaryDict
        self.stockHistoricalPrices = stockHistoricalPrices

    def __str__(self):
        return str(self.__dict__)
