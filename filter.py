import pandas as pd
import streamlit as st


def filter(selectedDf):
    selectedColumns = st.multiselect("Select columns on which you need to apply filter", selectedDf.columns.tolist())
    if selectedColumns:
        filterMap = {}
        for value in selectedColumns:
            filterValue = st.text_input(f"Input for {value}:(this is Case Sensitive filter)")
            # Check if all characters in the string are digits
            filterValue.strip()
            if filterValue.isdigit():
                # Convert the string to an integer
                filterValue = int(filterValue)
            filterMap[value] = filterValue
            
            
            
        queryItems = []

        for key, value in filterMap.items():
            if isinstance(value, int):
                queryItems.append(f"{key} == {value}")
            else:
                queryItems.append(f"{key} == '{value}'")

        queryString = " and ".join(queryItems)
        
        # Create the query string based on the filter dictionary
        # queryString = " and ".join([f"{key} == '{value}'" for key, value in filterMap.items()])
        st.write(queryString)

        # Apply the query to filter the DataFrame
        filteredDF = selectedDf.query(queryString)
        # filteredDF = pd.DataFrame()
        return filteredDF
            
        
               
    else:
        st.warning("Please select at least one column to display.")
        


        