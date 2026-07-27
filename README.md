# 自動化金融市場數據 ETL 管線 (Automated Financial Data ETL Pipeline)

這是一個小型 ETL (Extract, Transform, Load) 專案。透過 Python 自動抓取公開金融市場數據，進行資料清洗與轉換後，載入至 MySQL 資料庫，並具備完整的單元測試與 CI/CD 防護機制。


## 專案亮點 (Key Features)

- **模組化架構 (SoC)**：將萃取、轉換、載入邏輯嚴格拆分至獨立模組，確保程式碼具備高可讀性與可維護性。
- **資料品質與冪等性防護 (Idempotency)**：MySQL 資料表採用 Unique Key 約束與 DECIMAL 精準度設定，防範重複寫入與浮點數誤差。
- **無副作用測試 (Mock Testing)**：使用 pytest 搭配 unittest.mock 技術，隔離網路請求與資料庫依賴，確保商業邏輯穩定。
- **自動化持續整合 (CI/CD)**：結合 GitHub Actions，在每次推送程式碼時自動執行單元測試。
- **資安合規**：使用 .env 隔離敏感憑證，杜絕密碼外洩風險。


## 系統架構 (Architecture)

1. **Extract**: 透過 yfinance API 獲取 Apple, Microsoft, TSMC 等標的之歷史股價。
2. **Transform**: 使用 pandas 進行資料清洗、時區處理、欄位重命名與缺失值過濾。
3. **Load**: 透過 SQLAlchemy 與 mysql-connector-python 將清洗後的數據載入至 MySQL 關聯式資料庫。

## 技術堆疊 (Tech Stack)

- **Language**: Python 3.10+
- **Database**: MySQL 8.0+
- **Data Processing**: Pandas
- **Testing**: Pytest, Mock
- **DevOps**: GitHub Actions, Virtual Environment (venv)

## 快速啟動 (Quick Start)

### 1. 建立環境與安裝相依套件
```bash
python -m venv venv
source venv/bin/activate  # Windows 使用: .\venv\Scripts\activate
pip install -r requirements.txt
