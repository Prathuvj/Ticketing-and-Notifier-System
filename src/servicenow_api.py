"""
ServiceNow API Module
Handles communication with the ServiceNow instance.
"""

import os
import requests
from typing import Dict, Any
from dotenv import load_dotenv
from slack_notifier import SlackNotifier

class ServiceNowAPI:
    def __init__(self):
        load_dotenv()
        self.instance = os.getenv('SNOW_INSTANCE')
        self.username = os.getenv('SNOW_USERNAME')
        self.password = os.getenv('SNOW_PASSWORD')
        # Remove any trailing slashes and construct the base URL
        self.base_url = f"{self.instance.rstrip('/')}/api/now"
        self.slack_notifier = SlackNotifier()
        
    def create_incident(self, anomaly: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new incident in ServiceNow."""
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        
        data = {
            "short_description": f"Anomaly detected: {anomaly['type']}",
            "description": f"Anomaly details:\n{anomaly['details']['message']}\nError count: {anomaly['details']['error_count']}",
            "impact": "2",  # Medium impact
            "urgency": "2",  # Medium urgency
            "category": "software",
            "subcategory": "application"
        }
        
        response = requests.post(
            f"{self.base_url}/table/incident",
            auth=(self.username, self.password),
            headers=headers,
            json=data
        )
        
        incident_data = response.json()
        
        # Send Slack notification
        if response.status_code == 201:  # Created
            self.slack_notifier.send_incident_alert(incident_data, self.instance)
        
        return incident_data
    
    def update_incident(self, incident_sys_id: str, update_data: Dict[str, Any]) -> Dict[str, Any]:
        """Update an existing incident in ServiceNow."""
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        
        response = requests.put(
            f"{self.base_url}/table/incident/{incident_sys_id}",
            auth=(self.username, self.password),
            headers=headers,
            json=update_data
        )
        
        return response.json() 