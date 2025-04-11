# ServiceNow Ticketing System

A Python-based system that generates synthetic logs, detects anomalies, and creates ServiceNow tickets automatically.

## Features

- Synthetic log generation
- Anomaly detection
- Automatic ServiceNow ticket creation
- Configurable thresholds and parameters

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/servicenow-ticketing-system.git
cd servicenow-ticketing-system
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:
   - Copy `.env.example` to `.env`
   - Update the ServiceNow credentials in `.env`

## Usage

Run the main script:
```bash
python src/main.py
```

## Project Structure

```
servicenow-ticketing-system/
│
├── logs/                      # Directory for generated logs
│   └── generated_logs.json
│
├── src/                       # Source code
│   ├── __init__.py
│   ├── log_generator.py       # Log generation module
│   ├── anomaly_detector.py    # Anomaly detection module
│   ├── servicenow_api.py      # ServiceNow API integration
│   └── main.py                # Main application
│
├── .env                       # Environment variables
├── .gitignore                 # Git ignore file
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

## Configuration

The system can be configured through:

1. Environment variables in `.env`
2. Parameters in the respective modules
3. Anomaly detection thresholds

## License

This project is licensed under the MIT License - see the LICENSE file for details. 