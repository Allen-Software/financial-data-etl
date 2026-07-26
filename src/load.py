import os
from sqlalchemy import create_engine
import logging

def load_data_to_mysql(df, table_name='daily_stock_prices'):
    logging.info("準備寫入 MySQL")
    db_url = f"mysql+mysqlconnector://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    engine = create_engine(db_url)
    df.to_sql(name=table_name, con=engine, if_exists='append', index=False)