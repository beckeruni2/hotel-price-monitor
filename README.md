# Hotel Price Monitor

This project is an AI agent that monitors hotel room prices for changes. It retrieves current prices from specified hotel websites and notifies users if there are any price drops.

## Project Structure

```
hotel-price-monitor
├── src
│   ├── main.py          # Entry point of the application
│   ├── agents
│   │   └── price_monitor.py  # Contains the PriceMonitor class
│   ├── utils
│   │   └── scraper.py   # Responsible for scraping hotel prices
│   └── data
│       └── __init__.py  # Marks the data directory as a package
├── requirements.txt      # Lists project dependencies
├── .gitignore            # Specifies files to ignore in Git
└── README.md             # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd hotel-price-monitor
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python src/main.py
   ```

## Usage

- The application will start monitoring hotel room prices based on the configurations set in `main.py`.
- Users will receive notifications when there are price drops for the specified hotels.

## AS of Now
- User gets a daily email with minimal information (using cron)

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.