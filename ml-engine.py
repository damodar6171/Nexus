import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest

def generate_base_data(num_samples=300):
    """Generates normal baseline sensor telemetry."""
    np.random.seed(42)
    return pd.DataFrame({
        'temperature': np.random.normal(loc=65.0, scale=3.0, size=num_samples),
        'vibration':   np.random.normal(loc=20.0, scale=2.0, size=num_samples),
        'pressure':    np.random.normal(loc=50.0, scale=4.0, size=num_samples)
    })

def train_model():
    """Trains the Isolation Forest algorithm on baseline normal data."""
    df_train = generate_base_data()
    model = IsolationForest(n_estimators=100, contamination=0.05, random_state=42)
    model.fit(df_train[['temperature', 'vibration', 'pressure']])
    return model

def analyze_telemetry(model, temp, vib, press):
    """Calculates live anomaly decisions and 0-100% anomaly severity scores."""
    live_data = pd.DataFrame([[temp, vib, press]], columns=['temperature', 'vibration', 'pressure'])
    prediction = model.predict(live_data)[0]
    is_anomaly = True if prediction == -1 else False
    
    raw_score = model.decision_function(live_data)[0]
    anomaly_pct = int(np.clip((0.15 - raw_score) * 200, 0, 100))
    
    return is_anomaly, anomaly_pct

# Unit Test Block
if __name__ == "__main__":
    print("🤖 Training Isolation Forest Model...")
    trained_model = train_model()
    print("✅ Model Trained Successfully!\n")
    
    print("Test 1 (Normal Data):", analyze_telemetry(trained_model, 65.2, 20.1, 49.8))
    print("Test 2 (Failure Spike):", analyze_telemetry(trained_model, 92.1, 48.5, 51.0))