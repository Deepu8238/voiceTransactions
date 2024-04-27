# Utility functions
# Add any utility functions needed for your application here
# app/utils.py

def format_transaction_data(transaction_data):
    """
    Formats transaction data for display or processing.

    Args:
        transaction_data: Transaction data to be formatted.

    Returns:
        Formatted transaction data.
    """
    formatted_data = ""
    for key, value in transaction_data.items():
        formatted_data += f"{key}: {value}\n"
    return formatted_data
