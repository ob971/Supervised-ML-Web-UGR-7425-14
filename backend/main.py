"""
FastAPI Backend for ML Classification Application
Provides REST API endpoints for Logistic Regression and Decision Tree predictions
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import joblib
import numpy as np
import os
from typing import List

# Initialize FastAPI app
app = FastAPI(
    title="ML Classification API",
    description="API for Logistic Regression and Decision Tree predictions",
    version="1.0.0"
)

# Enable CORS for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://supervised-ml-web-ugr-7425-14.onrender.com",  # Frontend on Render
        "http://localhost:3000",  # Local development
        "*"  # Allow all for now (remove in production for better security)
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load models and scaler
MODEL_DIR = os.path.join(os.path.dirname(__file__), "models")

try:
    logistic_model = joblib.load(os.path.join(MODEL_DIR, "logistic_model.pkl"))
    decision_tree_model = joblib.load(os.path.join(MODEL_DIR, "decision_tree.pkl"))
    scaler = joblib.load(os.path.join(MODEL_DIR, "scaler.pkl"))
    print("Models loaded successfully!")
except FileNotFoundError as e:
    print(f"Warning: Model files not found. Please train models first. Error: {e}")
    logistic_model = None
    decision_tree_model = None
    scaler = None


# Pydantic models for request/response validation
class PredictionRequest(BaseModel):
    """Request model for predictions"""
    age: float = Field(..., description="Age of the patient", ge=0, le=120)
    glucose: float = Field(..., description="Glucose level", ge=0, le=500)
    bp: float = Field(..., description="Blood pressure", ge=0, le=200)
    skin_thickness: float = Field(..., description="Skin thickness", ge=0, le=100)
    insulin: float = Field(..., description="Insulin level", ge=0, le=1000)
    bmi: float = Field(..., description="Body Mass Index", ge=0, le=100)
    diabetes_pedigree: float = Field(..., description="Diabetes pedigree function", ge=0, le=3)
    pregnancies: float = Field(..., description="Number of pregnancies", ge=0, le=20)

    class Config:
        schema_extra = {
            "example": {
                "age": 29,
                "glucose": 85,
                "bp": 66,
                "skin_thickness": 29,
                "insulin": 0,
                "bmi": 26.6,
                "diabetes_pedigree": 0.351,
                "pregnancies": 0
            }
        }


class ModelPrediction(BaseModel):
    """Single model prediction result"""
    prediction: int = Field(..., description="Predicted class (0 or 1)")
    probability: float = Field(..., description="Prediction probability/confidence")
    model_name: str = Field(..., description="Name of the model")


class PredictionResponse(BaseModel):
    """Response model for predictions"""
    logistic_regression: ModelPrediction
    decision_tree: ModelPrediction
    input_features: dict


@app.get("/")
async def root():
    """Root endpoint - API information"""
    return {
        "message": "ML Classification API",
        "version": "1.0.0",
        "endpoints": {
            "/predict": "POST - Get predictions from both models",
            "/health": "GET - Check API health and model status",
            "/docs": "GET - API documentation"
        }
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    models_loaded = (
        logistic_model is not None and
        decision_tree_model is not None and
        scaler is not None
    )
    
    return {
        "status": "healthy" if models_loaded else "models_not_loaded",
        "models_loaded": models_loaded,
        "logistic_regression": logistic_model is not None,
        "decision_tree": decision_tree_model is not None,
        "scaler": scaler is not None
    }


@app.post("/predict", response_model=PredictionResponse)
async def predict(request: PredictionRequest):
    """
    Get predictions from both Logistic Regression and Decision Tree models
    
    Returns predictions, probabilities, and confidence scores from both models
    """
    if not all([logistic_model, decision_tree_model, scaler]):
        raise HTTPException(
            status_code=503,
            detail="Models not loaded. Please ensure model files exist in backend/models/"
        )
    
    try:
        # Prepare input features in the correct order
        feature_names = [
            'age', 'glucose', 'bp', 'skin_thickness', 
            'insulin', 'bmi', 'diabetes_pedigree', 'pregnancies'
        ]
        
        input_array = np.array([[
            request.age,
            request.glucose,
            request.bp,
            request.skin_thickness,
            request.insulin,
            request.bmi,
            request.diabetes_pedigree,
            request.pregnancies
        ]])
        
        # Logistic Regression prediction (requires scaling)
        X_scaled = scaler.transform(input_array)
        lr_prediction = int(logistic_model.predict(X_scaled)[0])
        lr_probability = float(logistic_model.predict_proba(X_scaled)[0][lr_prediction])
        
        # Decision Tree prediction (no scaling needed)
        dt_prediction = int(decision_tree_model.predict(input_array)[0])
        dt_probability = float(decision_tree_model.predict_proba(input_array)[0][dt_prediction])
        
        return PredictionResponse(
            logistic_regression=ModelPrediction(
                prediction=lr_prediction,
                probability=round(lr_probability, 4),
                model_name="Logistic Regression"
            ),
            decision_tree=ModelPrediction(
                prediction=dt_prediction,
                probability=round(dt_probability, 4),
                model_name="Decision Tree"
            ),
            input_features=request.dict()
        )
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Prediction error: {str(e)}"
        )


@app.post("/predict/batch")
async def predict_batch(requests: List[PredictionRequest]):
    """
    Batch prediction endpoint for multiple inputs
    """
    if not all([logistic_model, decision_tree_model, scaler]):
        raise HTTPException(
            status_code=503,
            detail="Models not loaded. Please ensure model files exist in backend/models/"
        )
    
    try:
        results = []
        
        for request in requests:
            # Prepare input features
            input_array = np.array([[
                request.age,
                request.glucose,
                request.bp,
                request.skin_thickness,
                request.insulin,
                request.bmi,
                request.diabetes_pedigree,
                request.pregnancies
            ]])
            
            # Logistic Regression prediction
            X_scaled = scaler.transform(input_array)
            lr_prediction = int(logistic_model.predict(X_scaled)[0])
            lr_probability = float(logistic_model.predict_proba(X_scaled)[0][lr_prediction])
            
            # Decision Tree prediction
            dt_prediction = int(decision_tree_model.predict(input_array)[0])
            dt_probability = float(decision_tree_model.predict_proba(input_array)[0][dt_prediction])
            
            results.append({
                "logistic_regression": {
                    "prediction": lr_prediction,
                    "probability": round(lr_probability, 4),
                    "model_name": "Logistic Regression"
                },
                "decision_tree": {
                    "prediction": dt_prediction,
                    "probability": round(dt_probability, 4),
                    "model_name": "Decision Tree"
                },
                "input_features": request.dict()
            })
        
        return {"results": results, "count": len(results)}
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Batch prediction error: {str(e)}"
        )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)

