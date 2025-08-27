# Guide d'utilisation

1. Installer les dépendances : `pip install -r requirements.txt`
2. Valider : `python scripts/cli.py validate --csv data/risk_data_example.csv`
3. Scorer : `python scripts/cli.py scores --csv data/risk_data_example.csv --out out/risk_scores.csv`
4. Excel : `python scripts/cli.py update-template --excel templates/risk_register_template.xlsx --csv out/risk_scores.csv --sheet Risks --header-row 1 --start-col 1 --include-headers`