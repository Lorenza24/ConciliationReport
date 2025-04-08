def get_card(row):
    """
    Determines the card brand based on the first digits of the card number.

    Parameters:
    row (pd.Series): A row from a DataFrame containing the column 'CARD_SIX_FIRST_DIGITS'.

    Returns:
    str: The card brand ('AMERICAN EXPRESS', 'MASTERCARD', 'VISA', or 'PENDIENTE' if unknown).
    """
    first_digits = str(row["CARD_SIX_FIRST_DIGITS"])[0:2]

    if first_digits in ['34', '37']:
        return 'AMERICAN EXPRESS'
    elif first_digits[0] in ['2', '5']:
        return 'MASTERCARD'
    elif first_digits[0] == '4':
        return 'VISA'
    else:
        return 'PENDIENTE'


# Function to determine the card brand for each row based on the payment method or card number
def get_brand(row):
    """
    Determines the card brand based on the payment method or the card number.

    Parameters:
    row (pd.Series): A row from a DataFrame containing the column 'PAY_METHOD'.

    Returns:
    str: The card brand ('MASTERCARD' if the payment method matches, otherwise determined by get_card()).
    """
    if row['PAY_METHOD'] in ['MASTER', 'MAESTRO', 'MASTERCARD', 'Master']:
        return "MASTERCARD"
    else:
        return get_card(row)


# Function to apply the brand determination logic to an entire DataFrame
def point_4(df):
    """
    Applies the get_brand function to each row in the DataFrame.

    Parameters:
    df_1 (pd.DataFrame): A DataFrame containing payment method and card number information.

    Returns:
    pd.Series: A series with the determined card brands for each row.
    """
    return df.apply(get_brand, axis=1)