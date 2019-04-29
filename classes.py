class Stock:
    def __init__(self, stockSummaryDict, stockHistoricalPrices, stockHistoricalDividends, stockFinancialProfile, stockCompanyProfile, stockDirectorDict) :
        self.stockSummaryDict = stockSummaryDict
        self.stockHistoricalPrices = stockHistoricalPrices
        self.stockHistoricalDividends = stockHistoricalDividends
        self.stockFinancialProfile = stockFinancialProfile
        self.stockCompanyProfile = stockCompanyProfile
        self.stockDirectorDict = stockDirectorDict

    def __str__(self):
        return str(self.__dict__)