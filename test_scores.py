from scripts.calc_scores import main as calc_main
import pandas as pd, os, tempfile

def test_scores_output():
    with tempfile.TemporaryDirectory() as td:
        out = os.path.join(td, 'scores.csv')
        calc_main('data/risk_data_example.csv', out)
        df = pd.read_csv(out)
        assert 'V_conf' in df.columns
        assert df['V_conf'].between(0,100).all()