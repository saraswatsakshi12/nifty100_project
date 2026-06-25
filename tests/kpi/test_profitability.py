from src.analytics.ratios import calculate_ratios


def test_ratio_generation():

    df = calculate_ratios()

    assert len(df) > 0


def test_columns_exist():

    df = calculate_ratios()

    assert "npm" in df.columns
    assert "opm" in df.columns
    assert "roe" in df.columns
    assert "roce" in df.columns