
from log import logger

import re

def validate_name(name):
    """
    Description : 
            This function validates first name by matching user input string with regex pattern.
    Parameters : 
            first_name : user input string
    Returns    :
            none
    """
    pattern = r"^[A-Z][a-z]{2,}$"
    result = re.match(pattern, name) is not None
    if result:
        logger.info("Name Accepted")
    else:
        logger.warning("Name not accepted: enter name with first letter as capital and minimum 3 characters.")

    
def validate_email(email):
    """
    Description : 
            This function validates email by matching user input string with regex pattern.
    Parameters : 
            email : user input email id
    Returns    :
            none
    """
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    result = re.match(pattern, email) is not None
    if result:
        logger.info("Email id Accepted")
    else:
        logger.warning("Email not accepted: enter valid email id")

