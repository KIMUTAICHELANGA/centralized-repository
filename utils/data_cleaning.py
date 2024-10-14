import pandas as pd

def clean_data(data):
    """Cleans and normalizes the incoming data.
    
    Args:
        data (list): List of dictionaries representing raw data.

    Returns:
        pd.DataFrame: Cleaned data in DataFrame format.
    """
    # Convert to DataFrame for easier manipulation
    df = pd.DataFrame(data)

    # Example cleaning steps
    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Handle missing values (fill or drop)
    df.fillna('', inplace=True)  # Fill missing values with an empty string

    # Normalize column names (e.g., lowercase)
    df.columns = [col.lower().replace(' ', '_') for col in df.columns]

    return df

def normalize_text(text):
    """Normalize text data (e.g., lowercasing, stripping whitespace).
    
    Args:
        text (str): The text to normalize.

    Returns:
        str: Normalized text.
    """
    if isinstance(text, str):
        return text.strip().lower()
    return text
