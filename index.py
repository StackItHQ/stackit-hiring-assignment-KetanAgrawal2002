import streamlit as st
import pandas as pd
from createNewSheet import *
from authenticate import *
from appendToSheet import *

# Set the title of the app
st.title("CSV File To Google Sheet")

# Create a file uploader widget
uploadedFile = st.file_uploader("Upload a CSV file", type=["csv"])
checkboxValue = st.checkbox("Add to Exisiting File")

# Use the value of the checkbox
if checkboxValue:
    linkToSheet = st.text_input("Enter a link to the sheet to upload")
    
    # Extract the Sheet Id from the link
    startIndex = linkToSheet.find("/d/") + 3  
    endIndex = linkToSheet.find("/edit")
    keyToSheet = linkToSheet[startIndex:endIndex]

    
    if uploadedFile is not None:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(uploadedFile)
        
        selectedColumns = st.multiselect("Select columns to add to sheet", df.columns.tolist())
        
        # Check if any columns are selected
        if selectedColumns:
            # Filter the DataFrame to display only the selected columns
            selectedDF = df[selectedColumns]
            st.write("Selected Data:")
            st.write(selectedDF)    
        else:
            st.warning("Please select at least one column to display.")
        
        if st.button("Append Data"):
            if selectedColumns:
                selectedDF.iloc[0]=selectedDF.columns
                st.write(appendData(keyToSheet,selectedDF))
            else:
                st.warning("Please select at least one column to add to Sheets.")
    
else:    
    customTitle = st.text_input("Enter a custom name for the sheet (optional)")
    # Check if a file has been uploaded
    if uploadedFile is not None:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(uploadedFile)
        title = customTitle.strip() if customTitle else uploadedFile.name
        selectedColumns = st.multiselect("Select columns to add to sheet", df.columns.tolist())
        
        # Check if any columns are selected
        if selectedColumns:
            # Filter the DataFrame to display only the selected columns
            selectedDF = df[selectedColumns]
            st.write("Selected columns:")
            st.write(selectedDF)    
        else:
            st.warning("Please select at least one column to display.")
        
        if st.button("Add Data"):
            if selectedColumns:
                selectedDF.iloc[0]=selectedDF.columns
                st.write(addData(selectedDF,title))
            else:
                st.warning("Please select at least one column to add to Sheets.")
                


st.write("---")

st.write("Crafted with ❤️ by Ketan Agrawal (20BIT0437)")
                
                
                
