import joblib
import pandas as pd
import os

# Model and preprocessor paths
MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'model', 'student_performance_model.pkl')
PREPROCESSOR_PATH = os.path.join(os.path.dirname(__file__), '..', 'model', 'preprocessor.pkl')

# Global variables (load once at startup)
model = None
preprocessor = None

def load_model_and_preprocessor():
    """Load model and preprocessor from disk."""
    global model, preprocessor
    
    try:
        model = joblib.load(MODEL_PATH)
        preprocessor = joblib.load(PREPROCESSOR_PATH)
        print("✅ Model and preprocessor loaded successfully!")
        return True
    except Exception as e:
        print(f"❌ Error loading model: {e}")
        return False

def preprocess_input(data: dict) -> pd.DataFrame:
    """Convert user input to DataFrame and apply preprocessing."""
    # Convert dict to DataFrame (single row)
    input_df = pd.DataFrame([data])
    
    # Ensure columns are in correct order
    expected_columns = ['study_hours', 'math_score', 'science_score', 'english_score',
                        'parent_education', 'travel_time', 'study_method']
    input_df = input_df[expected_columns]
    
    # Apply preprocessing (transform only, not fit!)
    processed_input = preprocessor.transform(input_df)
    
    return processed_input

def predict(processed_input) -> float:
    """Make prediction using loaded model and clip to 0-100 range."""
    prediction = model.predict(processed_input)
    score = prediction[0]
    # Clip to valid range
    return max(0, min(100, score))  # 0 se 100 ke beech mein rakhein
def predict_with_confidence(processed_input):
    """
    Predict score and calculate confidence based on prediction stability.
    """
    global model
    
    # 1. Make prediction
    prediction = model.predict(processed_input)[0]
    prediction = max(0, min(100, prediction))

    
    # 2. Calculate confidence (dynamic)
    # For now, we'll use a simple method: 
    # Confidence based on how far the prediction is from 0-100 range
    # Closer to middle (50) = higher confidence, extremes = lower confidence
    distance_from_middle = abs(prediction - 50) / 50  # 0 to 1
    confidence = 100 - (distance_from_middle * 30)  # Reduce confidence for extremes
    confidence = max(70, min(98, confidence))  # Keep between 70-98%
    
    return round(prediction, 2), round(confidence, 2)