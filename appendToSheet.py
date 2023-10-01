from googleapiclient.discovery import build
from authenticate import *



def appendData(keyToSheet,data):    
    try:
        # Authenticating with googleapiclient
        creds = authenticate()
        
        
        service = build('sheets', 'v4', credentials=creds)
        
        body = {
            
            'values': data.values.tolist()
        }        
        range_name = "Sheet1"
        
        # Appending data to exesting spreadsheet
        result = service.spreadsheets().values().append(spreadsheetId=keyToSheet, 
                                                        range=range_name,
                                                        valueInputOption='RAW',
                                                        body=body).execute()
        # print(result)
        return "Data Added successfully"
    
    except HttpError as error:
        print(f"An error occurred: {error}")
        return error