import pandas as pd
from unittest.mock import patch
from src.extract import extract_financial_data

@patch('src.extract.yf.Ticker')
def test_extract_financial_data(mock_ticker_class):
    mock_df = pd.DataFrame({'Open': [100], 'Close': [105], 'Volume': [1000]})
    mock_instance = mock_ticker_class.return_value
    mock_instance.history.return_value = mock_df

    result = extract_financial_data(['AAPL'], period="1d")
    assert len(result) == 1
    assert result['symbol'].iloc[0] == 'AAPL'