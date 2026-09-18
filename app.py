import streamlit as st

# We import the functions you built in ui_components.py
from ui_components import (
    setup_page, 
    render_sidebar, 
    render_machine_grid, 
    render_copilot_panel, 
    render_learning_card
)

# 1. Draw the Header
setup_page()

# 2. Draw the Sidebar Switch
simulate_failure = render_sidebar()

# 3. Dummy Data (Fake data to test your frontend display)
if simulate_failure:
    machines = {
        "Machine 01": {"status": "NORMAL", "score": 5},
        "Machine 02": {"status": "NORMAL", "score": 8},
        "Machine 03": {"status": "CRITICAL", "score": 89},
        "Machine 04": {"status": "NORMAL", "score": 12},
    }
    m3_readings = {"temp": 91.5, "vib": 48.2, "press": 52.0}
    ai_message = "⚠️ Machine 03 shows high temperature and abnormal vibration! High risk of motor failure. Recommendation: Inspect immediately."
    is_anomaly = True
else:
    machines = {
        "Machine 01": {"status": "NORMAL", "score": 5},
        "Machine 02": {"status": "NORMAL", "score": 8},
        "Machine 03": {"status": "NORMAL", "score": 10},
        "Machine 04": {"status": "NORMAL", "score": 12},
    }
    m3_readings = {"temp": 65.0, "vib": 20.0, "press": 50.0}
    ai_message = "🟢 Machine 03 is running smoothly within normal limits."
    is_anomaly = False

# 4. Render all parts on screen
render_machine_grid(machines)
render_copilot_panel(m3_readings, ai_message, is_anomaly)
render_learning_card(is_anomaly)