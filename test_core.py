
import pytest, pandas as pd
from scripts.transform_csv_to_dataframe import transform_csv_to_dataframe
from scripts.vx import compute_vx

def test_valid_csv():
    df=transform_csv_to_dataframe('data/risk_data_example.csv')
    assert 'Risk' in df.columns

def test_invalid_csv():
    with pytest.raises(Exception): transform_csv_to_dataframe('data/risk_data_invalid.csv')

def test_vx_computation():
    params={'p':0.5,'I':5,'E':5,'X':5,'v':5,'R':5,'H':5,'D':5,'K':5,'C':0.5,'s':50}
    res=compute_vx(params)
    assert 0<=res['V_conf']<=100
