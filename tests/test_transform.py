import pandas as pd
from pandas.testing import assert_frame_equal
from src.transform import clean_and_format_data

def test_clean_and_format_data():
    raw_data = {
        'Date': pd.to_datetime(['2023-10-01 00:00:00-04:00', '2023-10-02 00:00:00-04:00']),
        'Open': [150.0, None],
        'Close': [155.0, 152.0],
        'Volume': [10000, 15000],
        'symbol': ['AAPL', 'AAPL']
    }
    df_raw = pd.DataFrame(raw_data).set_index('Date')

    expected_data = {
        'symbol': ['AAPL'],
        'trade_date': [pd.to_datetime('2023-10-01').date()],
        'open_price': [150.0],
        'close_price': [155.0],
        'volume': [10000]
    }
    df_expected = pd.DataFrame(expected_data)

    result = clean_and_format_data(df_raw)
    assert_frame_equal(result, df_expected, check_dtype=False)