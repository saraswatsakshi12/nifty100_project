import pandas as pd
import sqlite3

DB = "nifty100.db"


def get_connection():
    return sqlite3.connect(DB)


def calculate_ratios():

    conn = get_connection()

    pnl = pd.read_sql(
        "SELECT * FROM profitandloss",
        conn
    )

    bs = pd.read_sql(
        "SELECT * FROM balancesheet",
        conn
    )

    df = pnl.merge(
        bs,
        on=["company_id", "year"],
        how="left"
    )

    # Net Profit Margin
    df["npm"] = df.apply(
        lambda x:
        (x["net_profit"] / x["sales"] * 100)
        if x["sales"] not in [0, None]
        else None,
        axis=1
    )

    # Operating Profit Margin
    df["opm"] = df.apply(
        lambda x:
        (x["operating_profit"] / x["sales"] * 100)
        if x["sales"] not in [0, None]
        else None,
        axis=1
    )

    # Return on Equity
    df["roe"] = df.apply(
        lambda x:
        (
            x["net_profit"]
            /
            (x["equity_capital"] + x["reserves"])
            * 100
        )
        if (
            x["equity_capital"] + x["reserves"]
        ) > 0
        else None,
        axis=1
    )

    # EBIT
    df["ebit"] = (
        df["operating_profit"]
        - df["depreciation"]
    )

    # ROCE
    df["roce"] = df.apply(
        lambda x:
        (
            x["ebit"]
            /
            (
                x["equity_capital"]
                + x["reserves"]
                + x["borrowings"]
            )
            * 100
        )
        if (
            x["equity_capital"]
            + x["reserves"]
            + x["borrowings"]
        ) > 0
        else None,
        axis=1
    )

    result = df[
        [
            "company_id",
            "year",
            "npm",
            "opm",
            "roe",
            "roce"
        ]
    ]

    print(result.head())

    conn.close()

    return result


if __name__ == "__main__":
    calculate_ratios()