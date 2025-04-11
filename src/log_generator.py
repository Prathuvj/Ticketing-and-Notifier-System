"""
Log Generator Module
Generates synthetic log data for testing and development purposes.
"""

import json
import random
import datetime
from typing import Dict, List

class LogGenerator:
    def __init__(self):
        self.log_levels = ['INFO', 'WARNING', 'ERROR', 'CRITICAL']
        self.components = ['System', 'Network', 'Database', 'Application', 'Security']
        
    def generate_log(self) -> Dict:
        """Generate a single log entry."""
        timestamp = datetime.datetime.now().isoformat()
        return {
            'timestamp': timestamp,
            'level': random.choice(self.log_levels),
            'component': random.choice(self.components),
            'message': f"Sample log message from {random.choice(self.components)} component",
            'details': {
                'status': random.choice(['success', 'failure']),
                'code': random.randint(1000, 9999)
            }
        }
    
    def generate_logs(self, count: int) -> List[Dict]:
        """Generate multiple log entries."""
        return [self.generate_log() for _ in range(count)]
    
    def save_logs(self, logs: List[Dict], filename: str):
        """Save logs to a JSON file."""
        with open(filename, 'w') as f:
            json.dump(logs, f, indent=2) 