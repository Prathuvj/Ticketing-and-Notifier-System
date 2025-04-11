"""
Slack Notifier Module
Handles sending notifications to Slack via webhook.
"""

import os
import requests
from typing import Dict, Any
from dotenv import load_dotenv

class SlackNotifier:
    def __init__(self):
        load_dotenv()
        self.webhook_url = os.getenv('SLACK_WEBHOOK_URL')
        
    def send_incident_alert(self, incident_data: Dict[str, Any], snow_url: str) -> bool:
        """
        Send an alert to Slack about a new ServiceNow incident.
        
        Args:
            incident_data: The incident data from ServiceNow
            snow_url: The ServiceNow instance URL
            
        Returns:
            bool: True if the message was sent successfully, False otherwise
        """
        if not self.webhook_url:
            print("Warning: SLACK_WEBHOOK_URL not set in .env file")
            return False
            
        incident_number = incident_data.get('result', {}).get('number', 'UNKNOWN')
        incident_sys_id = incident_data.get('result', {}).get('sys_id', '')
        short_description = incident_data.get('result', {}).get('short_description', 'No description')
        
        # Construct the ServiceNow incident URL
        incident_url = f"{snow_url}/nav_to.do?uri=incident.do?sys_id={incident_sys_id}"
        
        # Create the Slack message
        message = {
            "blocks": [
                {
                    "type": "header",
                    "text": {
                        "type": "plain_text",
                        "text": "🚨 New ServiceNow Incident Created",
                        "emoji": True
                    }
                },
                {
                    "type": "section",
                    "fields": [
                        {
                            "type": "mrkdwn",
                            "text": f"*Incident Number:*\n{incident_number}"
                        },
                        {
                            "type": "mrkdwn",
                            "text": f"*Description:*\n{short_description}"
                        }
                    ]
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"*<{incident_url}|View Incident in ServiceNow>*"
                    }
                }
            ]
        }
        
        try:
            response = requests.post(
                self.webhook_url,
                json=message,
                headers={'Content-Type': 'application/json'}
            )
            response.raise_for_status()
            return True
        except Exception as e:
            print(f"Failed to send Slack notification: {str(e)}")
            return False 