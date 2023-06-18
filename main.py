'''
@Author: shubham shirke
@Date: 2023-06-18 11:30:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-18 18:15:30
@Title : Validate password in user registration problem to have minimum 8 characters with atleast 1 uppercase letter.
'''

from log import logger   
from user_registration_problem import UserRegistration as register

# main
def main():
    """
    Description : 
            This function provide the user interface for the user on console and pass input as argument to required functions.
    Parameters  :
            none
    Returns     :
            none
    """
    logger.info('Starting the program')
    print("--User Registration Validation System--")
    
    first_name = input("Enter first name: ")
    register.validate_name(first_name)
    
    last_name = input("Enter last name: ")
    register.validate_name(last_name)
    
    email = input("Enter email id: ")
    register.validate_email(email)
    
    phone_number = input("Enter Phone NUmber: ")
    register.validate_phone_number(phone_number)
    
    password = input("Enter Password: ")
    register.validate_password(password)



    logger.info('Program finished')



if __name__ == "__main__":
    main()



