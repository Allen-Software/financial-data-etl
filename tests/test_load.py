import pandas as pd
from unittest.mock import patch
from src.load import load_data_to_mysql

@patch('src.load.create_engine')
@patch('pandas.DataFrame.to_sql')
def test_load_data_to_mysql(mock_to_sql, mock_create_engine):
    df_dummy = pd.DataFrame({'symbol': ['AAPL'], 'price': [150]})

    with patch('src.load.os.getenv', return_value='dummy'):
        load_data_to_mysql(df_dummy)

    mock_create_engine.assert_called_once()
    mock_to_sql.assert_called_once_with(
        name='daily_stock_prices',
        con=mock_create_engine.return_value,
        if_exists='append',
        index=False
    )