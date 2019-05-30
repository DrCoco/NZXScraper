import pytest
import sys
sys.path.append(r'C:/Users/Kiran/Documents/GitHub/NZXScraper')
from nzxscraper import scrape_data
from testnzxscraper import read_in_html

stockSummarySoupList = read_in_html('/*SummaryPageSource.txt')
stockSummaryDictList = [scrape_data.get_stock_summary(soup) for soup in stockSummarySoupList]


def test_get_stock_summary_ticker() :
    assert stockSummaryDictList[0]["Ticker"] ==  "ATM"
    assert stockSummaryDictList[1]["Ticker"] ==  "NTL"
    assert stockSummaryDictList[2]["Ticker"] ==  "TLS"

def test_get_stock_summary_name_is_present() :
    assert "Name" in stockSummaryDictList[0].keys()
    assert "Price" in stockSummaryDictList[1].keys()
    assert "Beta Value" in stockSummaryDictList[2].keys()

def test_get_stock_summary_is_dict() :
    assert type(stockSummaryDictList[0]) is dict
    assert type(stockSummaryDictList[1]) is dict
    assert type(stockSummaryDictList[2]) is dict

def test_create_historical_prices_csv_link() :
    assert scrape_data.create_historical_prices_csv_link(stockSummaryDictList[0]) == "https://companyresearch-nzx-com.ezproxy.aut.ac.nz/deep_ar/functions/csv_prices.php?default=ATM&fd=2016-05-28&td=2019-05-28"
    assert scrape_data.create_historical_prices_csv_link(stockSummaryDictList[1]) == "https://companyresearch-nzx-com.ezproxy.aut.ac.nz/deep_ar/functions/csv_prices.php?default=NTL&fd=2016-05-28&td=2019-05-28"
    assert scrape_data.create_historical_prices_csv_link(stockSummaryDictList[2]) == "https://companyresearch-nzx-com.ezproxy.aut.ac.nz/deep_ar/functions/csv_prices.php?default=TLS&fd=2016-05-28&td=2019-05-28"