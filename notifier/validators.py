import re


def is_valid_email(email):
    """
    Validate email format using Regular Expression.
    Returns True if valid, otherwise False.
    """

    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

    return re.fullmatch(pattern, email) is not None