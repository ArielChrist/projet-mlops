# Projet MLOps

Ce projet implémente un modèle de prédiction avec une API pour faire des prédictions.

## Installation

1. Cloner le dépôt
2. Installer les dépendances :
```bash
pip install -r requirements.txt
```

## Entraînement du modèle

Pour entraîner le modèle :
```bash
python -m src.models.main
```

## Préparation pour l'API

Avant de lancer l'API, vous devez sauvegarder le modèle et le pipeline :
```bash
python -m src.models.save_model
```

## Lancement de l'API

Pour lancer l'API :
```bash
python run_api.py
```

L'API sera disponible à l'adresse http://localhost:8000

## Utilisation de l'API

### Vérifier l'état de l'API
```bash
curl http://localhost:8000/health
```

### Faire une prédiction
```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"features": {"feature1": value1, "feature2": value2, ...}}'
```

### Documentation de l'API

La documentation interactive de l'API est disponible à l'adresse :
- http://localhost:8000/docs (Swagger UI)
- http://localhost:8000/redoc (ReDoc)