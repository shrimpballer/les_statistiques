# les_statistiques

**les_statistiques** est une bibliothèque Python pour le calcul des statistiques descriptives sur des séries de données numériques (et chaînes de caractères par leur longueur). Elle propose des outils pour calculer les effectifs, fréquences, fréquences cumulées, etc.

## Fonctionnalités

- Calcul des effectifs (nombre d’occurrences de chaque valeur)
- Calcul des effectifs cumulés
- Calcul des fréquences et fréquences cumulées
- Gestion des erreurs de type pour garantir l’intégrité des données

## Installation

Clonez ce dépôt puis importez les modules dans vos scripts Python :

```bash
gh repo clone shrimpballer/les_statistiques
cd les_statistiques
```

## Utilisation

### Exemple de base

```python
from outils.frequences import Frequences

data = [1, 2, 3, 5, 1, 2, 3, 5, 1, 5]
freq = Frequences(data)

# Fréquences simples
print(freq.frequences())  # [0.3, 0.2, 0.2, 0.3]

# Fréquences cumulées
print(freq.frequence_cumulee(mode=1))  # [0.3, 0.5, 0.7, 1.0]

# Fréquences cumulées formatées
print(freq.frequence_cumulee(mode="str"))  # 0.3 -> 0.5 -> 0.7 -> 1.0
```

### Gestion des erreurs

Les méthodes lèvent des exceptions si la série contient des types non pris en charge ou si l’effectif total est nul.

## Structure du projet

```py
les_statistiques/
│
├── statistiques.py         # Classe de base
├── outils/
│   ├── effectifs.py        # Calcul des effectifs
│   └── frequences.py       # Calcul des fréquences
└── README.md
```

## Infos

- Inspiré par des exercices de statistiques classiques.

