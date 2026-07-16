from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from .models import StudentPerformanceInput, PredictionResponse
from .utils import load_model_and_preprocessor, preprocess_input, predict_with_confidence

# Initialize FastAPI app
app = FastAPI(
    title="Student Performance Prediction API",
    description="Predicts overall performance based on student habits and scores",
    version="1.0.0"
)

# Enable CORS (so Streamlit can call this API)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, restrict to specific domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model at startup
@app.on_event("startup")
async def startup_event():
    """Load model when server starts."""
    success = load_model_and_preprocessor()
    if not success:
        raise Exception("Failed to load model or preprocessor")

# Root endpoint (health check)
@app.get("/")
def read_root():
    return {
        "message": "Student Performance Prediction API",
        "status": "running",
        "endpoints": {
            "/predict": "POST - predict overall score",
            "/health": "GET - health check"
        }
    }

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "healthy", "model_loaded": True}

# Prediction endpoint
@app.post("/predict", response_model=PredictionResponse)
def predict_score(student_data: StudentPerformanceInput):
    try:
        # Convert input to dict
        input_dict = student_data.dict()
        
        # Preprocess input
        processed_input = preprocess_input(input_dict)
        
        # Make prediction with confidence
        prediction, confidence = predict_with_confidence(processed_input)

        #  Return response
        return PredictionResponse(
            predicted_score=prediction,
            confidence_score=confidence,  # for Dynamic confidence 
            message="Prediction successful!",
            input_received=input_dict
        )
    
    except KeyError as e:
        raise HTTPException(status_code=400, detail=f"Missing required field: {str(e)}")
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")

# Run the app (if script is executed directly)
if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)