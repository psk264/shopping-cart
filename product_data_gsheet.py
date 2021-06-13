#! Adopted from Professor Rossetti
# Reference: https://github.com/prof-rossetti/intro-to-python/blob/main/notes/python/packages/gspread.md

import os
from dotenv import load_dotenv
import gspread
from oauth2client.service_account import ServiceAccountCredentials

load_dotenv()

DOCUMENT_ID = os.getenv("GOOGLE_SHEET_ID", default="OOPS")
SHEET_NAME = os.getenv("SHEET_NAME", default="Products-2021")
SHEET_NAME_LB = os.getenv("SHEET_PRICE_PER_LB", default = "Products-2021")
#
# AUTHORIZATION
#
# see: https://gspread.readthedocs.io/en/latest/api.html#gspread.authorize
# ... and FYI there is also a newer, more high level way to do this (see the docs)

# an OS-agnostic (Windows-safe) way to reference the "auth/google-credentials.json" filepath:
CREDENTIALS_FILEPATH = os.path.join(os.path.dirname(__file__), "auth", "google-credentials.json")

AUTH_SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets", #> Allows read/write access to the user's sheets and their properties.
    "https://www.googleapis.com/auth/drive.file" #> Per-file access to files created or opened by the app.
]

credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILEPATH, AUTH_SCOPE)
# print("CREDS:", type(credentials)) #> <class 'oauth2client.service_account.ServiceAccountCredentials'>

client = gspread.authorize(credentials)
# print("CLIENT:", type(client)) #> <class 'gspread.client.Client'>

#
# READ SHEET VALUES
#
# see: https://gspread.readthedocs.io/en/latest/api.html#client
# ...  https://gspread.readthedocs.io/en/latest/api.html#gspread.models.Spreadsheet
# ...  https://gspread.readthedocs.io/en/latest/api.html#gspread.models.Worksheet

# print("-----------------")
# print("READING DOCUMENT...")

doc = client.open_by_key(DOCUMENT_ID)
# print("DOC:", type(doc), doc.title) #> <class 'gspread.models.Spreadsheet'>

sheet = doc.worksheet(SHEET_NAME)
# print("SHEET:", type(sheet), sheet.title)#> <class 'gspread.models.Worksheet'>

def get_list_products():
    rows = sheet.get_all_records()
    # print("ROWS:", type(rows)) #> <class 'list'>
    
    # for row in rows:
    #     print(row) #> <class 'dict'>
    return rows

def get_list_products_lb():
    sheet = doc.worksheet(SHEET_NAME_LB)
    rows = sheet.get_all_records()
    return rows
#
# WRITE VALUES TO GOOGLE SHEET
#
# see: https://gspread.readthedocs.io/en/latest/api.html#gspread.models.Worksheet.insert_row
def add_new_product():
    print("-----------------")
    print("NEW ROW...")
    rows = get_list_products()
    auto_incremented_id = len(rows) + 1 # TODO: should change this to be one greater than the current maximum id value

    new_row = {
        "id": auto_incremented_id,
        "name": f"Product {auto_incremented_id} (created from my python app)",
        "department": "snacks",
        "price": 4.99,
        "availability_date": "2021-02-17"
    }
    print(new_row)

    print("-----------------")
    print("WRITING VALUES TO DOCUMENT...")

    # the sheet's insert_row() method wants our data to be in this format (see docs):
    new_values = list(new_row.values()) #> [13, 'Product 13', 'snacks', 4.99, '2019-01-01']

    # the sheet's insert_row() method wants us to pass the row number where this will be inserted (see docs):
    next_row_number = len(rows) + 2 # number of records, plus a header row, plus one

    response = sheet.insert_row(new_values, next_row_number)

    print("RESPONSE:", type(response)) #> dict
    print(response) #> {'spreadsheetId': '____', 'updatedRange': "'Products-2021'!A9:E9", 'updatedRows': 1, 'updatedColumns': 5, 'updatedCells': 5}

