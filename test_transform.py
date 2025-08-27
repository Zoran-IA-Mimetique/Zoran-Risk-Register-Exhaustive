from scripts.transform_csv_to_dataframe import transform_csv_to_dataframe
import pytest

def test_valid_csv():
    df = transform_csv_to_dataframe('data/risk_data_example.csv')
    assert 'Risk' in df.columns and len(df) >= 1

def test_invalid_csv_raises():
    with pytest.raises(Exception):
        transform_csv_to_dataframe('data/risk_data_invalid.csv')