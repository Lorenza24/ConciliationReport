def card_type(row):
    """
    Determine the card type based on authorization and acquirer details.

    Parameters:
    row (pd.Series): A row from the DataFrame containing transaction details.

    Returns:
    str: A standardized card type based on predefined conditions.
    """

    # Check if any of the relevant fields indicate Mastercard, Firstdata, or Diners
    if (row['CAPTURE_AUTHORIZATION_CODE'] in ["Mastercard", "Firstdata", "Diners"]) or \
       (row['PURCHASE_ACQUIRER'] in ["Mastercard", "Firstdata", "Diners"]) or \
       (row['AUTH_ACQUIRER'] in ["Mastercard", "Firstdata", "Diners"]):
        return "FD"

    # Check if any of the relevant fields indicate Visa
    elif (row['CAPTURE_AUTHORIZATION_CODE'] in ["Visa"]) or \
         (row['PURCHASE_ACQUIRER'] in ["Visa"]) or \
         (row['AUTH_ACQUIRER'] in ["Visa"]):
        return "PRISMA"

    # If no conditions match, return a concatenated uppercase string of all relevant fields
    else:
        return str(row['CAPTURE_AUTHORIZATION_CODE']).upper() + \
               str(row['PURCHASE_ACQUIRER']).upper() + \
               str(row['AUTH_ACQUIRER']).upper()


def point_3(df):
    """
    Apply the card_type function to each row of the DataFrame.

    Parameters:
    df (pd.DataFrame): Input DataFrame containing transaction details.

    Returns:
    pd.Series: A series containing the determined card type for each row.
    """

    # Apply the card_type function row-wise
    return df.apply(card_type, axis=1)