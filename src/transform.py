import pandas as pd
import logging

def clean_and_format_data(df):
    logging.info("開始轉換數據")
    df = df.reset_index()
    df = df.rename(columns={'Date': 'trade_date', 'Open': 'open_price', 'Close': 'close_price', 'Volume': 'volume'})
    df['trade_date'] = df['trade_date'].dt.tz_localize(None).dt.date
    df_clean = df[['symbol', 'trade_date', 'open_price', 'close_price', 'volume']].dropna()
    return df_clean