import pandas as pd
import datetime as dt

def add_day(column):
    """
    Add one day to the 'MOV_CREATED_DATE' column and format the new date.

    Parameters:
    column (pd.DataFrame): DataFrame containing the 'MOV_CREATED_DATE' column.

    Returns:
    pd.Series: A series with updated 'MOV_CREATION_DATE' values in 'YYYY-MM-DD' format.
    """

    # Convert 'MOV_CREATED_DATE' to datetime format
    column["MOV_CREATED_DATE"] = pd.to_datetime(column["MOV_CREATED_DATE"])

    # Define a lambda function to add one day to the 'MOV_CREATED_DATE' column
    sum_day = lambda x: x["MOV_CREATED_DATE"] + pd.Timedelta(days=1)

    # Apply the lambda function to update the column
    column["MOV_CREATION_DATE"] = column.apply(sum_day, axis=1)

    # Format 'MOV_CREATED_DATE' as a string in 'YYYY-MM-DD' format and store it in 'MOV_CREATION_DATE'
    column["MOV_CREATION_DATE"] = column["MOV_CREATION_DATE"].dt.strftime('%Y-%m-%d')

    # Return only the 'MOV_CREATION_DATE' column as a Series
    return column["MOV_CREATION_DATE"]


def point_6(df):
    """
    Apply the add_day function to the DataFrame.

    Parameters:
    df (pd.DataFrame): Input DataFrame containing transaction dates.

    Returns:
    pd.Series: A series with updated 'MOV_CREATION_DATE' values.
    """

    return add_day(df)  # Call add_day function on the DataFrame