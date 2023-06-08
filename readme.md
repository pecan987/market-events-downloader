# Google Sheets CSV Updater

This Python script downloads a CSV file from a given URL and appends the data to a specified Google Sheets document.

## Requirements

The script requires the following Python libraries:

- pandas
- gspread
- requests
- oauth2client
- gspread_dataframe
- python-dotenv

You can install these libraries using pip:

```bash
pip install pandas gspread requests oauth2client gspread-dataframe python-dotenv
```

## Setup

1. Create account credentials for a service account following the instructions [here](https://gspread.readthedocs.io/en/latest/oauth2.html#for-bots-using-service-account).
2. Save the credentials JSON file
3. Create spreadsheet in Google Sheets and share it with the email address from the service account credentials
4. Copy .env.dist to .env and set the environment variables in the file, or use OS environment variables

## Usage

```bash
python main.py
```

