'''
@Author: shubham shirke
@Date: 2023-06-18 11:30:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-18 13:50:30
@Title : Refactor User registration problem and perform unit testing. 
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
    # input first name
    first_name = input("Enter first name: ")
    register.validate_name(first_name)
    # input last name
    last_name = input("Enter last name: ")
    register.validate_name(last_name)
    # input email
    email = input("Enter email id: ")
    register.validate_email(email)
    # phone number
    phone_number = input("Enter Phone Number: ")
    register.validate_phone_number(phone_number)

    # input password
    print("Enter password")
    print("* minimum 8 characters")
    print("* atleast 1 uppercase")
    print("* atleast 1 digit")
    print("* one special character")
    password = input("Password: ")
    register.validate_password(password)



    logger.info('Program finished')



if __name__ == "__main__":
    main()



