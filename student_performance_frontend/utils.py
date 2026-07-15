import requests
import streamlit as st

# Backend API endpoint (Render URL)
API_URL = "https://student-performance-api-b8wn.onrender.com/predict"

def call_prediction_api(data):
    try:
        response = requests.post(API_URL, json=data)
        if response.status_code == 200:
            result = response.json()
            return result
        else:
            st.error(f"API Error: {response.status_code}")
            return None
    except Exception as e:
        st.error(f"Connection Error: {str(e)}")
        return None