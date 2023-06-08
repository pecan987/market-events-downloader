import pandas as pd
import gspread
import requests
import os
from oauth2client.service_account import ServiceAccountCredentials
from gspread_dataframe import set_with_dataframe
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Define the scope
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

# Get the service account key file path, sheet name, and CSV URL from environment variables
credentials_file = os.environ.get('CREDENTIALS_FILE')
sheet_name = os.environ.get('SHEET_NAME')
csv_url = os.environ.get('CSV_URL')

# Add your service account file
creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, scope)

# Authorize the clientsheet
client = gspread.authorize(creds)

# Get the instance of the Spreadsheet
sheet = client.open(sheet_name)

# Get the first sheet of the Spreadsheet
worksheet = sheet.get_worksheet(0)

# Download CSV file
res = requests.get(csv_url, allow_redirects=True)

# Decode content and convert to StringIO for pandas
from io import StringIO
data = pd.read_csv(StringIO(res.content.decode('utf-8')), skiprows=1)

# If the sheet is empty, append the data starting from the first cell
if len(worksheet.get_all_values()) == 0:
    set_with_dataframe(worksheet, data)
else:
    # Get the last filled row
    last_filled_row = len(worksheet.get_all_records(default_blank="")) + 1

    # Append the data after the last filled row
    set_with_dataframe(worksheet, data, row=last_filled_row + 1)