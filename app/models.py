from pydantic import BaseModel
from typing import Optional

class StudentPerformanceInput(BaseModel):
    """Request model for prediction endpoint."""
    study_hours: float
    math_score: float
    science_score: float
    english_score: float
    parent_education: str
    travel_time: str
    study_method: str

class PredictionResponse(BaseModel):
    """Response model for prediction endpoint."""
    predicted_score: float
    confidence_score: Optional[float] = None 
    message: str
    input_received: dict
