"""
Log Generator Module
Generates synthetic log data for testing and development purposes.
"""

import json
import random
import datetime
import os
from typing import Dict, List
from dotenv import load_dotenv

class LogGenerator:
    def __init__(self):
        load_dotenv()
        self.log_levels = ['INFO', 'WARNING', 'ERROR', 'CRITICAL']
        self.components = ['System', 'Network', 'Database', 'Application', 'Security']
        self.error_messages = {
            'System': [
                'CPU usage exceeded threshold',
                'Memory allocation failed',
                'System service crashed'
            ],
            'Network': [
                'Connection timeout',
                'Packet loss detected',
                'DNS resolution failed'
            ],
            'Database': [
                'Query execution timeout',
                'Connection pool exhausted',
                'Deadlock detected'
            ],
            'Application': [
                'Null pointer exception',
                'Stack overflow error',
                'Invalid input format'
            ],
            'Security': [
                'Failed login attempts exceeded',
                'Suspicious activity detected',
                'Access denied'
            ]
        }
        
        # Get log generation parameters from environment
        self.total_logs = int(os.getenv('TOTAL_LOGS', 100))
        self.anomalous_logs = int(os.getenv('ANOMALOUS_LOGS', 10))
        
    def generate_normal_log(self) -> Dict:
        """Generate a normal log entry."""
        timestamp = datetime.datetime.now().isoformat()
        component = random.choice(self.components)
        return {
            'timestamp': timestamp,
            'level': random.choice(['INFO', 'WARNING']),
            'component': component,
            'message': f"Normal operation in {component} component",
            'details': {
                'status': 'success',
                'code': random.randint(1000, 1999)
            }
        }
    
    def generate_anomalous_log(self) -> Dict:
        """Generate an anomalous log entry."""
        timestamp = datetime.datetime.now().isoformat()
        component = random.choice(self.components)
        error_type = random.choice(['ERROR', 'CRITICAL'])
        error_message = random.choice(self.error_messages[component])
        
        return {
            'timestamp': timestamp,
            'level': error_type,
            'component': component,
            'message': error_message,
            'details': {
                'status': 'failure',
                'code': random.randint(2000, 2999),
                'error_type': error_type,
                'component': component
            }
        }
    
    def generate_logs(self, total_logs: int = None, anomalous_logs: int = None) -> List[Dict]:
        """
        Generate a specified number of logs with a controlled number of anomalies.
        
        Args:
            total_logs: Total number of logs to generate (optional, defaults to env value)
            anomalous_logs: Number of anomalous logs to include (optional, defaults to env value)
            
        Returns:
            List of log entries
        """
        # Use provided parameters or fall back to environment values
        total = total_logs if total_logs is not None else self.total_logs
        anomalous = anomalous_logs if anomalous_logs is not None else self.anomalous_logs
        
        if anomalous > total:
            raise ValueError("Number of anomalous logs cannot exceed total logs")
            
        # Generate anomalous logs
        logs = [self.generate_anomalous_log() for _ in range(anomalous)]
        
        # Generate normal logs
        logs.extend([self.generate_normal_log() for _ in range(total - anomalous)])
        
        # Shuffle the logs to mix normal and anomalous entries
        random.shuffle(logs)
        
        return logs
    
    def save_logs(self, logs: List[Dict], filename: str):
        """Save logs to a JSON file."""
        with open(filename, 'w') as f:
            json.dump(logs, f, indent=2) 