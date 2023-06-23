from log import logger

import re

class UserRegistration:    

        def validate_name(name):
                """
                Description : 
                        This function validates first name by matching user input string with regex pattern.
                Parameters : 
                        first_name : user input string
                Returns    :
                        True : if pattern matches
                        False : pattern does not match
                """
                pattern = r"^[A-Z][a-z]{2,}$"
                result = re.match(pattern, name) is not None
                if result:
                        logger.info("Name Accepted")
                        return True
                else:
                        logger.warning("Name not accepted: enter name with first letter as capital and minimum 3 characters.")
                        return False

    
        def validate_email(email):
                """
                Description : 
                        This function validates email by matching user input string with regex pattern.
                Parameters : 
                        email : user input email id
                Returns    :
                        True : if pattern matches
                        False : pattern does not match
                """
                pattern = r'^[a-zA-Z0-9\+-]+(\.[a-zA-Z0-9]+)*@[a-zA-Z0-9]+([.][a-zA-Z]{2,3}){1,2}$'
                result = re.match(pattern, email) is not None
                if result:
                        logger.info(f"{email} id Accepted")
                        return True
                else:
                        logger.info(f"{email} not accepted: enter valid email id")
                        return False


        def validate_phone_number(phone_number):
                """
                Description : 
                        This function validates phone number by matching user input string with regex pattern.
                        The regex pattern accepts phone number with +,2 digit country code and 10 digit phone number starting with 6-9.
                Parameters : 
                        phone_number : user input phone number.
                Returns    :
                        True : if pattern matches
                        False : pattern does not match
                """
                pattern = r"^\+[0-9]{2}\s[6-9]\d{9}$"
                result = re.match(pattern, phone_number)
                if result:
                        logger.info("Phone Number Accepted")
                        return True
                else:
                        logger.warning("Phone Number not accepted: enter valid phone number with country code")
                        return False

        
        def validate_password(password):
                """
                Description : 
                        This function validates password to have minimum 8 characters,atleast 1 uppercase letter,atleast 1 numeric number and only one special character.
                Parameters : 
                        password : user input string
                Returns    :
                        True : if pattern matches
                        False : pattern does not match
                """
                pattern = r'^(?=.*[0-9])(?=.*[A-Z])(?=.*[~!@#$%^&*_])(?!.*[~!@#$%^&*_].*[~!@#$%^&*_]).{8,}$'
                result = re.match(pattern, password)
                if result:
                        logger.info("Password Accepted")
                        return True
                else:
                        logger.warning("Password not accepted: enter valid password with minimum 8 characters,atleast one digit and only one special character.")
                        return False