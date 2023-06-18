'''
@Author: shubham shirke
@Date: 2023-06-18 11:30:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-18 13:40:30
@Title : Validate last name in user registration problem.
'''

from log import logger   
import user_registration_problem as register

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
    print("--User Registration Validation System--")
    first_name= input("Enter first name: ")
    register.validate_name(first_name)
    last_name= input("Enter last name: ")
    register.validate_name(last_name)


if __name__ == "__main__":
    main()



