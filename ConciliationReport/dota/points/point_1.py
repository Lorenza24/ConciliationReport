import pandas as pd

## Function to concatenate strings
def point_1(df):
    """
    Generate a new DataFrame with a masked card number.

    Parameters:
    df (pd.DataFrame): Input DataFrame containing card details.

    Returns:
    pd.DataFrame: A new DataFrame with the masked card number.
    """

    # Create an empty DataFrame to store the new column
    df_new = pd.DataFrame()

    # Construct the masked card number by combining the first six digits,
    # masking the middle six digits with 'XXXXXX', and appending the last four digits
    df_new["CARD_NUMBER"] = df["CARD_SIX_FIRST_DIGITS"].astype(str) + "XXXXXX" + df["CARD_FOUR_LAST_DIGITS"].astype(str)

    return df_new