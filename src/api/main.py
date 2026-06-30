from fastapi import FastAPI
import sqlite3
import pandas as pd

app = FastAPI()

DB = "nifty100.db"


@app.get("/")
def home():
    return {
        "message": "Nifty100 Analytics API"
    }


@app.get("/companies")
def companies():

    conn = sqlite3.connect(DB)

    df = pd.read_sql(
        """
        SELECT
            id,
            company_name
        FROM companies
        """,
        conn
    )

    conn.close()

    return df.to_dict(
        orient="records"
    )


@app.get("/kpis")
def kpis():

    df = pd.read_csv(
        "output/kpi_metrics.csv"
    )

    return df.head(
        20
    ).to_dict(
        orient="records"
    )