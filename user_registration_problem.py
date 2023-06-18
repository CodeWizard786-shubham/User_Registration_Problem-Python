
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
                        none 
                        prints message.
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
                        prints message.
                """
                pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
                result = re.match(pattern, email) is not None
                if result:
                        logger.info("Email id Accepted")
                else:
                        logger.warning("Email not accepted: enter valid email id")


        def validate_phone_number(phone_number):
                """
                Description : 
                        This function validates phone number by matching user input string with regex pattern.
                        The regex pattern accepts phone number with +,2 digit country code and 10 digit phone number starting with 6-9.
                Parameters : 
                        phone_number : user input phone number.
                Returns    :
                        none
                        prints message.
                """
                pattern = r"^\+[0-9]{2}\s[6-9]\d{9}$"
                result = re.match(pattern, phone_number)
                if result:
                        logger.info("Phone Number Accepted")
                else:
                        logger.warning("Phone Number not accepted: enter valid phone number with country code")

        
        def validate_password(password):
                """
                Description : 
                        This function validates password to have minimum 8 characters,atleast 1 uppercase letter,atleast 1 numeric number and only one special character.
                Parameters : 
                        password : user input string
                Returns    :
                        none
                        prints message.
                """
                pattern = r"^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()\-_=+{};:,<.>]).{8,}$"
                result = re.match(pattern, password)
                if result:
                        logger.info("Password Accepted")
                else:
                        logger.warning("Password not accepted: enter valid password with minimum 8 characters")