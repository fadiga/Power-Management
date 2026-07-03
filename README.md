# Power-Management

Application de **suivi de consommation et de solde d'électricité prépayée** avec graphiques.

Outil bureau pour enregistrer les soldes, les coupures et les reprises de courant, calculer la consommation et estimer l'autonomie restante.

## Fonctionnalités

- Enregistrement des opérations : solde, coupure, reprise, consommation
- Tableau de bord : consommation max, plus longue coupure, moyenne, jours restants estimés
- Graphiques de solde et de consommation (Highcharts)
- Relevés PDF (solde, consommation, historique complet)
- Alertes sur le tableau de bord
- Interface en français (gettext)

## Stack technique

- Python · PyQt4 · QtWebKit
- Peewee ORM · SQLite (`power_mg.db`)
- matplotlib · Jinja2 · Highcharts

## Installation

```bash
pip install peewee matplotlib
# PyQt4 + QtWebKit requis
python power_m/power_m.py
```

## Structure

```
Power-Management/
└── power_m/
    ├── power_m.py       # Point d'entrée
    ├── models.py
    ├── ui/              # Dashboard, relevés, graphiques
    ├── doclib/          # Génération PDF
    └── templates/       # Graphiques HTML
```

## Auteur

[Ibrahima Fadiga](https://github.com/fadiga) — Bamako, Mali
