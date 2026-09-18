# ai_copilot.py

def get_copilot_diagnosis(temp, vib, press, is_anomaly):
    """Generates human-readable diagnosis from sensor data."""
    if not is_anomaly:
        return "Optimal Performance: Machine is operating well within standard parameters."
    
    # Analyze root causes
    causes = []
    if temp > 80:
        causes.append("Thermal dissipation failure")
    if vib > 35:
        causes.append("Mechanical imbalance or bearing wear")
        
    diagnosis = f"""
    ### AI Copilot Diagnostic
    Status: Critical Deviation Detected
    
    Primary Stressors: {', '.join(causes)}
    
    Suggested Operator Action: 
    Perform a manual inspection of the drive shaft and cooling system before approving further cycles.
    """
    return diagnosis


def get_recommended_action(is_anomaly):
    """Generates the Human-in-the-Loop decision prompt for the buttons."""
    if is_anomaly:
        return {
            "title": "Human Operator Decision Required",
            "recommendation": "Recommendation: Stop Machine 03 immediately for safety inspection.",
            "approve_label": "Approve Shutdown",
            "reject_label": "Reject and Override Alert"
        }
    return {
        "title": "System Status Normal",
        "recommendation": "No operator action required at this time.",
        "approve_label": "Acknowledge",
        "reject_label": "N/A"
    }


def get_personalized_lesson(vib_level):
    """Returns a short micro-learning module based on failure type."""
    if vib_level > 35:
        return {
            "title": "Module: Understanding Mechanical Vibration",
            "content": """
            What caused this alert?
            Simultaneous heat and vibration spikes typically indicate race degradation in rolling-element bearings.
            
            Action Protocol: Check oil viscosity and inspect for debris.
            Safety First: Always complete Lockout/Tagout (LOTO) before opening the casing.
            """,
            "question": "What is the most common cause of sudden vibration spikes with high heat?",
            "options": ["Bearing friction and wear", "Software update required", "Low network latency"],
            "correct_answer": "Bearing friction and wear"
        }
    return None
    # Quick test run:
#print(get_copilot_diagnosis(91.5, 48.2, 52.0, is_anomaly=True))
#print(get_recommended_action(is_anomaly=True))
#print(get_personalized_lesson(48.2))