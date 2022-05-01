import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')


def get_sale_data():
    '''
    Get sales figures input from the user
    '''
    print('Please enter input from the user\nData should be six numbers, seperated by commas\nExample: 10, 20, 30, 40, 50, 60\n')

    data_str = input('Enter your data here: ')

    sales_data = data_str.split(',')
    validate_data(sales_data)


def validate_data(values):
    '''
    Inside the try, converts all string values into integers.
    Raise ValueError if strings cannot be converted into an int,
    Or if there aren'texcatly 6 values
    '''
    try:
        if len(values) != 6:
            raise ValueError(
                f'Exactly 6 values required, you provided {len(values)}')
    except ValueError as err:
        print(f'Invalid data: {err}, please try again')


get_sale_data()
