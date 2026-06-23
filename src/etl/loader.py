import pandas as pd
import os
import sqlite3

from src.etl.normaliser import (
    normalize_year,
    normalize_ticker
)


DB = "nifty100.db"


class ExcelLoader:


    def __init__(self, path):

        self.path = path


    def load_excel(self):

        return pd.read_excel(
            self.path,
            header=1
        )


    def clean_columns(self, df):

        df.columns = (
            df.columns
            .str.lower()
            .str.strip()
            .str.replace(" ","_")
        )

        return df

    def normalize(self, df):

        if "year" in df.columns:
            df["year"] = df["year"].apply(
                normalize_year
            )

        if "ticker" in df.columns:
            df["ticker"] = df["ticker"].apply(
                normalize_ticker
            )

        return df


    def run(self):

        df = self.load_excel()

        df = self.clean_columns(df)

        df = self.normalize(df)

        return df



def get_connection():

    conn = sqlite3.connect(DB)

    conn.execute(
        "PRAGMA foreign_keys = ON"
    )

    return conn



def load_files():

    files = {

        "companies":"data/raw/companies.xlsx",
        "profitandloss":"data/raw/profitandloss.xlsx",
        "balancesheet":"data/raw/balancesheet.xlsx",
        "cashflow":"data/raw/cashflow.xlsx",
        "stock_prices":"data/raw/stock_prices.xlsx",
        "analysis":"data/raw/analysis.xlsx",
        "documents":"data/raw/documents.xlsx",
        "prosandcons":"data/raw/prosandcons.xlsx",
        "sectors":"data/raw/sectors.xlsx",
        "financial_ratios":"data/raw/financial_ratios.xlsx",
        "peer_groups":"data/raw/peer_groups.xlsx",
	"market_cap":"data/raw/market_cap.xlsx",
    }


    audit=[]

    conn=get_connection()


    for table,file in files.items():

        if os.path.exists(file):

            df = pd.read_excel(
    		 file,
   		 header=1
	    )

            df.to_sql(
                table,
                conn,
                if_exists="append",
                index=False
            )


            audit.append(
                {
                "table":table,
                "rows":len(df),
                "status":"loaded"
                }
            )

        else:

            audit.append(
                {
                "table":table,
                "rows":0,
                "status":"missing"
                }
            )


    conn.close()


    pd.DataFrame(audit).to_csv(
        "output/load_audit.csv",
        index=False
    )


    print("Load completed")



if __name__=="__main__":

    load_files()