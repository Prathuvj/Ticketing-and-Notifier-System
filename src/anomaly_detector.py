"""
Anomaly Detector Module
Detects anomalies in log data and generates alerts.
"""

import json
from typing import Dict, List, Any
from datetime import datetime

class AnomalyDetector:
    def __init__(self):
        self.error_threshold = 5  # Number of errors to trigger an alert
        self.time_window = 300  # 5 minutes in seconds
        
    def load_logs(self, filename: str) -> List[Dict]:
        """Load logs from a JSON file."""
        with open(filename, 'r') as f:
            return json.load(f)
    
    def detect_anomalies(self, logs: List[Dict]) -> List[Dict]:
        """Detect anomalies in the log data."""
        anomalies = []
        error_count = 0
        last_timestamp = None
        
        for log in logs:
            current_timestamp = datetime.fromisoformat(log['timestamp'])
            
            if last_timestamp is not None:
                time_diff = (current_timestamp - last_timestamp).total_seconds()
                if time_diff > self.time_window:
                    error_count = 0
            
            if log['level'] in ['ERROR', 'CRITICAL']:
                error_count += 1
                
                if error_count >= self.error_threshold:
                    anomalies.append({
                        'timestamp': log['timestamp'],
                        'type': 'error_threshold_exceeded',
                        'details': {
                            'error_count': error_count,
                            'component': log['component'],
                            'message': f"Error threshold exceeded in {log['component']}"
                        }
                    })
            
            last_timestamp = current_timestamp
        
        return anomalies
    
    def save_anomalies(self, anomalies: List[Dict], filename: str):
        """Save detected anomalies to a JSON file."""
        with open(filename, 'w') as f:
            json.dump(anomalies, f, indent=2) 