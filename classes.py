class Stock:
    def __init__(self, stockSummaryDict, stockHistoricalPrices, stockHistoricalDividends, stockFinancialProfile) :
        self.stockSummaryDict = stockSummaryDict
        self.stockHistoricalPrices = stockHistoricalPrices
        self.stockHistoricalDividends = stockHistoricalDividends
        self.stockFinancialProfile = stockFinancialProfile

    def __str__(self):
        return str(self.__dict__)