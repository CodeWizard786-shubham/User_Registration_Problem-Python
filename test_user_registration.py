'''
@Author: shubham shirke
@Date: 2023-06-19 13:30:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-19 14:15:30
@Title : Perform unit testing for each function in user registration. 
'''


import unittest

from user_registration_problem import UserRegistration

class UserRegistrationTest(unittest.TestCase):

    # validate name for pass test
    def test_validate_name_valid(self):
        name = "Shubham"
        result = UserRegistration.validate_name(name)
        self.assertTrue(result)

    # validate name for fail test
    def test_validate_name_invalid(self):
        name = "shubham"
        result = UserRegistration.validate_name(name)
        self.assertFalse(result)

    # validate email name for pass test
    def test_validate_email_valid(self):
        email = "test12@gmail.com"
        result = UserRegistration.validate_email(email)
        self.assertTrue(result)

    # validate email for fail test
    def test_validate_email_Invalid(self):
        email_1 = "test12@gmail"
        email_2 = "test12gmail.com"
        result1=UserRegistration.validate_email(email_1)
        self.assertFalse(result1)
        result2 = UserRegistration.validate_email(email_2)
        self.assertFalse(result2)

    # validate phone number for pass test
    def test_validate_phone_number_valid(self):
        phone_number = "+91 9876543210"
        result = UserRegistration.validate_email(phone_number)
        self.assertTrue(result)

    # validate phone number for fail test
    def test_validate_phone_number_valid(self):
        phone_number_1 = "+91 1876543210"
        phone_number_2 = "+9  9876543210"
        result1 = UserRegistration.validate_email(phone_number_1)
        self.assertFalse(result1)
        result2 = UserRegistration.validate_email(phone_number_2)
        self.assertFalse(result2)

    # validate password for pass test
    def test_validate_password_valid(self):
        password = "Testexample@123"
        result = UserRegistration.validate_email(password)
        self.assertFalse(result)

    # validate password for fail test
    def test_validate_password_valid(self):
        password_1 = "test@123"
        password_2 = "test123"
        result1 = UserRegistration.validate_email(password_1)
        self.assertFalse(result1)
        result2 = UserRegistration.validate_email(password_2)
        self.assertFalse(result2)
        


if __name__ == '__main__':
    unittest.main()
