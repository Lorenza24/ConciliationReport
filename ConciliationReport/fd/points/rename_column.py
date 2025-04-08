def rename_column(comercio_df):
    """
    Rename and select specific columns from the input DataFrame.

    Parameters:
    comercio_df (pd.DataFrame): Input DataFrame containing 'COMERCIO' 
                                 and 'TIPO_COMERCIO' columns.

    Returns:
    pd.DataFrame: A new DataFrame with renamed and selected columns.
    """

    # Create a new column 'GTWT_MERCHANT_NUMBER' by copying values from 'COMERCIO'
    comercio_df["GTWT_MERCHANT_NUMBER"] = comercio_df["COMERCIO"]

    # Select only the required columns for the output DataFrame
    comercio_df2 = comercio_df[["GTWT_MERCHANT_NUMBER", "TIPO_COMERCIO"]]

    # Return the new DataFrame with selected columns
    return comercio_df2