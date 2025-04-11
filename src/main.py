"""
Main Application Module
Coordinates the log generation, anomaly detection, and ServiceNow ticket creation.
"""

import os
from datetime import datetime
from log_generator import LogGenerator
from anomaly_detector import AnomalyDetector
from servicenow_api import ServiceNowAPI

def main():
    # Initialize components
    log_generator = LogGenerator()
    anomaly_detector = AnomalyDetector()
    snow_api = ServiceNowAPI()
    
    # Create logs directory if it doesn't exist
    os.makedirs('logs', exist_ok=True)
    
    # Generate logs
    logs = log_generator.generate_logs(100)
    log_filename = f"logs/generated_logs_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    log_generator.save_logs(logs, log_filename)
    
    # Detect anomalies
    anomalies = anomaly_detector.detect_anomalies(logs)
    
    if anomalies:
        print(f"Detected {len(anomalies)} anomalies")
        
        # Create ServiceNow tickets for each anomaly
        for anomaly in anomalies:
            try:
                response = snow_api.create_incident(anomaly)
                print(f"Created ServiceNow incident: {response['result']['number']}")
            except Exception as e:
                print(f"Failed to create ServiceNow incident: {str(e)}")
    else:
        print("No anomalies detected")

if __name__ == "__main__":
    main() 