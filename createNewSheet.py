from googleapiclient.discovery import build
from authenticate import *



def addData(data,title):    
    try:
        # Authenticating with googleapiclient
        creds = authenticate()
        
        
        service = build('sheets', 'v4', credentials=creds)
        spreadsheet = {
            'properties': {
                'title': title
            }
        }
        # Creating a Google sheet
        spreadsheet = service.spreadsheets().create(body=spreadsheet,
                                                        fields='spreadsheetId') \
                .execute()

        # print(f"Spreadsheet ID: {(spreadsheet.get('spreadsheetId'))}")
        
        body = {
            
            'values': data.values.tolist()
        }
        
        range_name = "Sheet1"
        # Adding data to the spreadsheet
        result = service.spreadsheets().values().update(
                    spreadsheetId=spreadsheet.get('spreadsheetId'),
                    range=range_name,
                    valueInputOption="RAW",
                    body=body
                    ).execute()
        # print(result)
        return "Data Added successfully"
    except HttpError as error:
        print(f"An error occurred: {error}")
        return "An error occurred"