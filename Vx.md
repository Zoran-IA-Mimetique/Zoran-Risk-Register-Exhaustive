# V(x) — Fonction de risque (0–100)

## Définition rapide
V(x) = 100 * Raw / (Raw + s) ; V_conf = V * (0.5 + 0.5*C)  
Raw = facteurs aggravants / facteurs atténuants (voir `scripts/vx.py`).

## Seuils de décision
<20: surveiller · 20–40: sprint · 40–60: prioritaire · ≥60: bloquant CI/CD