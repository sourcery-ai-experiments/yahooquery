import pandas as pd
import pytest
from yahooquery.ticker import Ticker


@pytest.fixture
def ticker():
    return Ticker("AAPL")


def test_dividend_history_no_dividends(ticker):
    df = ticker.dividend_history("2019-01-01", "2019-01-02")
    assert isinstance(df, pd.Series)
    assert df.empty


# Need to figure out why this sometimes fails and sometimes doesn't
def test_dividend_history_with_dividends(ticker):
    df = ticker.dividend_history("2024-02-08", "2024-02-11")
    print(df)
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert "dividends" in df.columns


def test_dividend_history_index(ticker):
    df = ticker.dividend_history("2019-01-01", "2019-01-02")
    assert df.index.names == ["symbol", "date"]
