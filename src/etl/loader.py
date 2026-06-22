import pandas as pd
import os

from src.etl.normaliser import (
    normalize_year,
    normalize_ticker
)

class ExcelLoader:


    def __init__(self,path):

        self.path = path



    def load_excel(self):

        df = pd.read_excel(self.path)

        return df



    def clean_columns(self,df):

        df.columns = (
            df.columns
            .str.lower()
            .str.strip()
            .str.replace(" ","_")
        )

        return df



    def normalize(self,df):

        if "year" in df.columns:
            df["year"] = (
                df["year"]
                .apply(normalize_year)
            )


        if "ticker" in df.columns:
            df["ticker"] = (
                df["ticker"]
                .apply(normalize_ticker)
            )


        return df



    def run(self):

        df = self.load_excel()

        df = self.clean_columns(df)

        df = self.normalize(df)


        return df



if __name__=="__main__":

    print(
        "Excel Loader Ready"
    )
import sqlite3


def get_connection():

    conn = sqlite3.connect(
        "nifty100.db"
    )

    conn.execute(
        "PRAGMA foreign_keys = ON"
    )

    return conn


def save_to_db(df, table):

    conn = get_connection()

    df.to_sql(
        table,
        conn,
        if_exists="append",
        index=False
    )

    conn.close()

