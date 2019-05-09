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