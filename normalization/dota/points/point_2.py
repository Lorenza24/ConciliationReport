import pandas as pd

def authorization_code(row):
    """
    Process the authorization code based on specific conditions.

    Parameters:
    row (pd.Series): A row from the DataFrame.

    Returns:
    str: An empty string if the conditions are met; otherwise, returns the original authorization code.
    """

    # Check if the authorization code is "000000" and the acquirer is "Cabal"
    if (row['CAPTURE_AUTHORIZATION_CODE'] in ["000000"]) and (row['CAPTURE_ACQUIRER'] in ["Cabal"]):
        return ""  # Return an empty string if both conditions are met
    else:
        return row['CAPTURE_AUTHORIZATION_CODE']  # Otherwise, return the original authorization code


def point_2(df):
    """
    Apply the authorization_code function to each row of the DataFrame.

    Parameters:
    df (pd.DataFrame): Input DataFrame containing transaction details.

    Returns:
    pd.DataFrame: A DataFrame with processed authorization codes.
    """

    # Apply the authorization_code function row-wise
    return df.apply(authorization_code, axis=0)