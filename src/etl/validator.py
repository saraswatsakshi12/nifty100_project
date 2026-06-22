import pandas as pd
import os


OUTPUT_FILE = "output/validation_failures.csv"



class DataValidator:


    def __init__(self, dataframe):

        self.df = dataframe
        self.failures = []



    def add_failure(
        self,
        rule,
        message,
        severity
    ):

        self.failures.append(
            {
                "rule": rule,
                "message": message,
                "severity": severity
            }
        )



    # DQ-01 Primary key uniqueness

    def dq01_pk_unique(self):

        if "company_id" in self.df:

            if self.df["company_id"].duplicated().any():

                self.add_failure(
                    "DQ-01",
                    "Duplicate company_id",
                    "CRITICAL"
                )



    # DQ-02 company-year uniqueness

    def dq02_company_year_pk(self):

        if {"company_id","year"}.issubset(self.df.columns):

            dup = self.df.duplicated(
                ["company_id","year"]
            ).any()

            if dup:

                self.add_failure(
                    "DQ-02",
                    "Duplicate company year",
                    "CRITICAL"
                )



    # DQ-03 FK integrity

    def dq03_fk_check(self):

        if self.df.isnull().any().any():

            self.add_failure(
                "DQ-03",
                "Foreign key missing values",
                "CRITICAL"
            )



    # DQ-04 Balance sheet check

    def dq04_balance(self):

        if {
            "assets",
            "liabilities"
        }.issubset(self.df.columns):

            diff = abs(
                self.df.assets -
                self.df.liabilities
            )

            if (diff > 0).any():

                self.add_failure(
                    "DQ-04",
                    "Balance sheet mismatch",
                    "WARNING"
                )



    # DQ-05 OPM check

    def dq05_opm(self):

        if "opm" in self.df:

            if self.df.opm.isnull().any():

                self.add_failure(
                    "DQ-05",
                    "OPM missing",
                    "WARNING"
                )



    # DQ-06 Sales positive

    def dq06_sales(self):

        if "sales" in self.df:

            if (self.df.sales < 0).any():

                self.add_failure(
                    "DQ-06",
                    "Negative sales",
                    "WARNING"
                )



    # DQ-07 to DQ-16 placeholder checks


    def dq07_to_dq16(self):

        rules = [
            "DQ-07 EPS sign check",
            "DQ-08 Tax rate check",
            "DQ-09 Net cash check",
            "DQ-10 Dividend check",
            "DQ-11 URL validation",
            "DQ-12 Coverage check",
            "DQ-13 Sector validation",
            "DQ-14 Ratio validation",
            "DQ-15 Price validation",
            "DQ-16 Record completeness"
        ]


        for rule in rules:

            pass



    def validate(self):

        self.dq01_pk_unique()
        self.dq02_company_year_pk()
        self.dq03_fk_check()
        self.dq04_balance()
        self.dq05_opm()
        self.dq06_sales()
        self.dq07_to_dq16()


        return self.failures



    def save_report(self):

        df = pd.DataFrame(
            self.failures
        )


        df.to_csv(
            OUTPUT_FILE,
            index=False
        )


        print(
            "Validation report created"
        )



if __name__=="__main__":


    sample = pd.DataFrame(
        {
        "company_id":[1,1],
        "year":[2024,2024],
        "sales":[100,-20]
        }
    )


    validator = DataValidator(sample)


    validator.validate()

    validator.save_report()