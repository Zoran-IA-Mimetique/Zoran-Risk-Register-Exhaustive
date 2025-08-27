# Zoran — Risk Register Exhaustive

[![CI](https://github.com/Zoran-IA-Mimetique/Zoran-Risk-Register-Exhaustive/actions/workflows/ci.yml/badge.svg)](https://github.com/Zoran-IA-Mimetique/Zoran-Risk-Register-Exhaustive/actions/workflows/ci.yml)

**Objectif :** fournir un **registre des risques exhaustif, validé et audit‑ready**, avec données d’exemple, validation de schéma, scoring **V(x)**, mise à jour Excel, **CLI** unifiée, **tests**, **CI**, et documentation (ISO 27005/27001, RGPD, AI Act).

## ⚡ Quickstart
```bash
python -m venv .venv && source .venv/bin/activate   # (Windows: .venv\Scripts\activate)
pip install -r requirements.txt

# 1) Valider un CSV (schéma & types)
python scripts/cli.py validate --csv data/risk_data_example.csv

# 2) Calculer les scores V(x) et enrichir le CSV
python scripts/cli.py scores --csv data/risk_data_example.csv --out out/risk_scores.csv

# 3) Mettre à jour le modèle Excel
python scripts/cli.py update-template \
  --excel templates/risk_register_template.xlsx \
  --csv out/risk_scores.csv --sheet Risks --header-row 1 --start-col 1 --include-headers
```

## 📂 Contenu
- `data/` → CSV **valide** et **invalide** pour tests.
- `config/config.yaml` → schéma requis + mapping vers V(x).
- `scripts/` → `transform_csv_to_dataframe.py` (validation), `calc_scores.py` (V(x)), `update_risk_register_template.py` (Excel), `vx.py` (fonction risque), `rgpd_tools.py` (pseudonymisation/TTL), `cli.py` (commande unifiée).
- `templates/risk_register_template.xlsx` → modèle Excel.
- `tests/` → tests **pytest** (validation & scoring).
- `.github/workflows/ci.yml` → **CI** (tests + audit deps).
- `docs/` → USAGE, RACI, checklist d’acceptation, V(x).

## 🔐 Conformité
- **RGPD** : pseudonymisation stable, masquage, TTL (scripts/rgpd_tools.py).
- **AI Act** : registres, explicabilité, traçabilité.
- **ISO 27005/27001** : structure du registre + processus.

## 🧮 V(x) — Fonction de risque
Voir `docs/Vx.md` et `scripts/vx.py`. Scores bornés **0–100**, avec seuils de décision CI/CD :
- V < 20 : surveiller
- 20 ≤ V < 40 : corriger en sprint
- 40 ≤ V < 60 : prioritaire
- V ≥ 60 : **bloquant**

## 🔚 Codes de sortie (CLI)
- `0` : succès
- `1` : échec logique (ex. aucun enregistrement)
- `2` : entrée invalide / schéma non conforme
- `3` : erreur runtime

## 📜 Licence
MIT — Contact : tabary01@gmail.com