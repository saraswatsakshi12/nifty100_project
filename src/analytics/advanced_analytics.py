import sqlite3
import pandas as pd

DB = "nifty100.db"

conn = sqlite3.connect(DB)

profit = pd.read_sql(
    """
    SELECT
        company_id,
        year,
        sales,
        net_profit
    FROM profitandloss
    """,
    conn
)

conn.close()

profit = profit.sort_values(
    ["company_id", "year"]
)

profit["sales_growth"] = (
    profit.groupby("company_id")["sales"]
    .pct_change() * 100
)

profit["profit_growth"] = (
    profit.groupby("company_id")["net_profit"]
    .pct_change() * 100
)

top_sales = (
    profit.groupby("company_id")["sales"]
    .mean()
    .sort_values(ascending=False)
    .head(20)
)

top_profit = (
    profit.groupby("company_id")["net_profit"]
    .mean()
    .sort_values(ascending=False)
    .head(20)
)

profit.to_csv(
    "output/advanced_metrics.csv",
    index=False
)

top_sales.to_csv(
    "output/top_sales_companies.csv"
)

top_profit.to_csv(
    "output/top_profit_companies.csv"
)

print("Advanced analytics completed")