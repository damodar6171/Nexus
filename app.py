import streamlit as st

# 1. Import UI Layout functions
from ui_components import (
    setup_page, 
    render_sidebar, 
    render_machine_grid, 
    render_copilot_panel, 
    render_learning_card
)

# 2. Import Machine Learning Model functions
from ml_engine import train_model, analyze_telemetry

# 3. Import AI Copilot & Learning functions
from ai_copilot import (
    get_copilot_diagnosis, 
    get_recommended_action, 
    get_personalized_lesson
)

# Set up page config and layout header
setup_page()

# Train/Load ML Model
@st.cache_resource
def load_ml_engine():
    return train_model()

model = load_ml_engine()

# Render Demo Sidebar Toggle
simulate_failure = render_sidebar()

# Define Sensor Data based on Toggle Switch
if simulate_failure:
    m3_readings = {"temp": 91.5, "vib": 48.2, "press": 52.0}
else:
    m3_readings = {"temp": 65.0, "vib": 20.0, "press": 50.0}

# Analyze Machine 03 using the ML Engine
is_anomaly, score = analyze_telemetry(
    model, 
    m3_readings["temp"], 
    m3_readings["vib"], 
    m3_readings["press"]
)

# Build Dynamic Machine Status Map
machines = {
    "Machine 01": {"status": "NORMAL", "score": 5},
    "Machine 02": {"status": "NORMAL", "score": 8},
    "Machine 03": {
        "status": "CRITICAL" if is_anomaly else "NORMAL", 
        "score": score
    },
    "Machine 04": {"status": "NORMAL", "score": 12},
}

# Generate AI Diagnosis from AI Copilot Engine
ai_message = get_copilot_diagnosis(
    m3_readings["temp"], 
    m3_readings["vib"], 
    m3_readings["press"], 
    is_anomaly
)

# Render Main Dashboard Components
render_machine_grid(machines)
render_copilot_panel(m3_readings, ai_message, is_anomaly)
render_learning_card(is_anomaly)
