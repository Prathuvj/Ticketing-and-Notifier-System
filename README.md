# Ticketing and Notifier System

A Python-based system that generates synthetic logs, detects anomalies, and creates ServiceNow tickets automatically with Slack notifications.

## Features

- Synthetic log generation with configurable anomaly rates
- Anomaly detection with customizable thresholds
- Automatic ServiceNow ticket creation
- Slack notifications for new incidents
- Environment-based configuration
- Comprehensive error handling

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ticketing-and-notifier-system.git
cd ticketing-and-notifier-system
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
   - Update the following variables in `.env`:
     ```env
     # ServiceNow Configuration
     SNOW_INSTANCE=your-instance.service-now.com
     SNOW_USERNAME=your-username
     SNOW_PASSWORD=your-password

     # Slack Configuration
     SLACK_WEBHOOK_URL=your-slack-webhook-url

     # Log Generation Configuration
     TOTAL_LOGS=100
     ANOMALOUS_LOGS=10
     ```

## Usage

Run the main script:
```bash
python src/main.py
```

The system will:
1. Generate synthetic logs based on configured parameters
2. Detect anomalies in the generated logs
3. Create ServiceNow tickets for detected anomalies
4. Send Slack notifications for new incidents

## Project Structure

```
ticketing-and-notifier-system/
│
├── logs/                      # Directory for generated logs
│   └── generated_logs_*.json  # Generated log files
│
├── src/                       # Source code
│   ├── __init__.py
│   ├── log_generator.py       # Log generation module
│   ├── anomaly_detector.py    # Anomaly detection module
│   ├── servicenow_api.py      # ServiceNow API integration
│   ├── slack_notifier.py      # Slack notification module
│   └── main.py                # Main application
│
├── .env                       # Environment variables
├── .env.example               # Example environment variables
├── .gitignore                 # Git ignore file
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

## Configuration

The system can be configured through environment variables in `.env`:

1. **ServiceNow Configuration**
   - `SNOW_INSTANCE`: Your ServiceNow instance URL
   - `SNOW_USERNAME`: ServiceNow username
   - `SNOW_PASSWORD`: ServiceNow password

2. **Slack Configuration**
   - `SLACK_WEBHOOK_URL`: Slack webhook URL for notifications

3. **Log Generation Configuration**
   - `TOTAL_LOGS`: Total number of logs to generate
   - `ANOMALOUS_LOGS`: Number of anomalous logs to include

## Log Generation

The system generates two types of logs:

1. **Normal Logs**
   - INFO or WARNING level
   - Success status
   - Code range 1000-1999

2. **Anomalous Logs**
   - ERROR or CRITICAL level
   - Failure status
   - Code range 2000-2999
   - Component-specific error messages

## Error Handling

The system includes comprehensive error handling for:
- ServiceNow API communication
- Slack notifications
- Log generation and anomaly detection
- File operations

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 