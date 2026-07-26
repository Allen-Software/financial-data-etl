import yfinance as yf
import pandas as pd
import logging

def extract_financial_data(symbols, period="1mo"):
    logging.info(f"開始抓取數據: {symbols}")
    raw_data = []
    for symbol in symbols:
        try:
            ticker = yf.Ticker(symbol)
            df = ticker.history(period=period)
            df['symbol'] = symbol
            raw_data.append(df)
        except Exception as e:
            logging.error(f"抓取 {symbol} 失敗: {e}")

    if not raw_data:
        raise ValueError("無有效數據")
    return pd.concat(raw_data)