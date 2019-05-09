import functions
import test_inputs
import pytest

summaryDict = functions.get_stock_summary(test_inputs.getStockSummaryInput)
def test_get_stock_summary_ticker() :
    assert summaryDict["Ticker"] ==  "TLS"
def test_get_stock_summary_name_is_present() :
    assert "Name" in summaryDict.keys()
def test_get_stock_summary_is_dict() :
    assert type(summaryDict) is dict