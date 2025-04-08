import pandas as pd
import datetime as dt

def find_info(row):
    """
    Find the first non-null and non-empty merchant number in the given row.

    Parameters:
    row (pd.Series): A row from the DataFrame.

    Returns:
    str: The first non-null and non-empty merchant number found, 
         or an empty string if none are found.
    """

    # Iterate over the specified columns in the given priority order
    for col in ['PURCHASE_MERCHANT_NUMBER', 
                'CAPTURE_MERCHANT_NUMBER', 
                'AUTH_MERCHANT_NUMBER']:
        
        # Check if the value is not null and not an empty string
        if pd.notnull(row[col]) and row[col] != '':
            return row[col]  # Return the first valid value found

    return ''  # Return an empty string if all values are null or empty


def point_5(df):
    """
    Apply the find_info function to each row of the DataFrame 
    and convert the result to integer type.

    Parameters:
    df (pd.DataFrame): Input DataFrame containing merchant number columns.

    Returns:
    pd.Series: A Series with the first found merchant number for each row, 
               converted to integer type.
    """

    # Apply the find_info function row-wise and convert the result to integer
    return df.apply(find_info, axis=1).astype(int)