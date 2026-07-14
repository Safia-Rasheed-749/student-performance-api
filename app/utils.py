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