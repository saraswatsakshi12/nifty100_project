import pandas as pd

from src.etl.validator import DataValidator



def test_duplicate_pk():

    df = pd.DataFrame(
        {
        "company_id":[1,1],
        "year":[2024,2025]
        }
    )


    v = DataValidator(df)

    result = v.validate()


    assert "DQ-01" in [
        x["rule"]
        for x in result
    ]