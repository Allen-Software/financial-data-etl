import logging
from dotenv import load_dotenv
from src.extract import extract_financial_data
from src.transform import clean_and_format_data
from src.load import load_data_to_mysql

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == "__main__":
    load_dotenv()
    target_symbols = ['AAPL', 'MSFT', 'TSM']

    try:
        raw_df = extract_financial_data(target_symbols, period="7d")
        clean_df = clean_and_format_data(raw_df)
        load_data_to_mysql(clean_df)
        logging.info("ETL 管線執行成功")
    except Exception as e:
        logging.critical(f"管線中斷: {e}")