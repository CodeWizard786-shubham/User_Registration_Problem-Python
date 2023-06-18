
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

    
