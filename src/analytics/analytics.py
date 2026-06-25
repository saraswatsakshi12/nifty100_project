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
        operating_profit,
        net_profit
    FROM profitandloss
    """,
    conn
)

companies = pd.read_sql(
    """
    SELECT
        id,
        company_name,
        roe_percentage,
        roce_percentage
    FROM companies
    """,
    conn
)

df = profit.merge(
    companies,
    left_on="company_id",
    right_on="id",
    how="left"
)

df["npm"] = (
    df["net_profit"] /
    df["sales"]
) * 100

df["opm"] = (
    df["operating_profit"] /
    df["sales"]
) * 100

df["roe"] = df["roe_percentage"]

df["roce"] = df["roce_percentage"]

kpi = df[
    [
        "company_id",
        "year",
        "npm",
        "opm",
        "roe",
        "roce"
    ]
]

kpi.to_csv(
    "output/kpi_metrics.csv",
    index=False
)

print(kpi.head())
print("KPI file created")