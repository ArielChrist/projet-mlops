import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import joblib
import pandas as pd
import uvicorn
from fastapi import FastAPI, HTTPException
from schemas.schemas import features, Target


app = FastAPI(
    title="API de Prédiction",
    description="API pour faire des prédictions avec le modèle entraîné",
    version="1.0.0"
)


MODEL_PATH = os.path.join(os.path.dirname(__file__), '../../models/model.joblib')
PIPELINE_PATH = os.path.join(os.path.dirname(__file__), '../../models/pipeline.joblib')


try:
    model = joblib.load(MODEL_PATH)
    pipeline = joblib.load(PIPELINE_PATH)
except FileNotFoundError:
    model = None
    pipeline = None

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API de prédiction"}

@app.post("/predict", response_model=Target)
def prediction(input_data: features):
    """
    Faire une prédiction avec le modèle
    
    Args:
        input_data: Données d'entrée pour la prédiction
        
    Returns:
        Prédiction du modèle
    """
    if model is None or pipeline is None:
        raise HTTPException(status_code=500, detail="Le modèle ou le pipeline n'est pas chargé")
    
    try:
        input_df = pd.DataFrame([input_data.features])
        
        processed_data = pipeline.transform(input_df)
        
        prediction = model.predict(processed_data)[0]
        
        return Target(prediction=float(prediction))
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erreur lors de la prédiction: {str(e)}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)