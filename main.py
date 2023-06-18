'''
@Author: shubham shirke
@Date: 2023-06-18 11:30:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-18 12:50:30
@Title : Validate first name in user registration problem.
'''

from log import logger
import user_registration_problem as register

# main
def main():
    print("--User Registration Validation System--")
    first_name= input("Enter first name: ")
    register.validate_name(first_name)
    

if __name__ == "__main__":
    main()



