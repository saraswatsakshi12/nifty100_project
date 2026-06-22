from src.etl.normaliser import *


def test_year_integer():

    assert normalize_year(2025)==2025



def test_year_float():

    assert normalize_year("2025.0")==2025



def test_year_text():

    assert normalize_year("FY 2024")==2024



def test_year_none():

    assert normalize_year(None)==None



def test_ticker_lower():

    assert normalize_ticker("tcs")=="TCS"



def test_ticker_space():

    assert normalize_ticker("  infy ")=="INFY"



def test_ticker_upper():

    assert normalize_ticker("RELIANCE")=="RELIANCE"


def test_year_with_date():

    assert normalize_year("31-12-2023")==2023



def test_year_string():

    assert normalize_year("FY2022")==2022



def test_year_invalid():

    assert normalize_year("abc")==None



def test_year_empty():

    assert normalize_year("")==None



def test_ticker_none():

    assert normalize_ticker(None)==None



def test_ticker_numbers():

    assert normalize_ticker(123)=="123"



def test_ticker_special():

    assert normalize_ticker(" tcs@ ")=="TCS@"



def test_ticker_mixed():

    assert normalize_ticker("InFy")=="INFY"