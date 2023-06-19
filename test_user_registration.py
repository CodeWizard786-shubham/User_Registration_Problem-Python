'''
@Author: shubham shirke
@Date: 2023-06-19 11:30:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-19 13:50:30
@Title : unit testing for each function. 
'''
import unittest

from user_registration_problem import UserRegistration

class UserRegistrationTest(unittest.TestCase):

    # validate name for pass test
    def test_validate_name_valid(self):
        name = "Test"
        result = UserRegistration.validate_name(name)
        self.assertTrue(result)

    # validate name for fail test
    def test_validate_name_invalid(self):
        name1 = "test"
        result = UserRegistration.validate_name(name1)
        self.assertFalse(result)

    # validate list of emails name for pass test
    def test_validate_email_valid(self):
        emails = ["test12@gmail.com","abc@yahoo.com","abc-100@yahoo.com","abc.100@yahoo.com","abc111@abc.com","abc-100@abc.net","abc.100@abc.com.au","abc@1.com","abc@gmail.com","abc+100@gmail.com"]
        for email in emails:
            result = UserRegistration.validate_email(email)
            self.assertTrue(result)

    # validate list of emails for fail test
    def test_validate_email_Invalid(self):
        emails = ["test12@gmail","abc123@gmail.a","abc@gmail.com.1a","abc@abc@gmail.com","abc@%*.com","abc()*@gmail.com","abc123@.com"]
        for email in emails:
            result = UserRegistration.validate_email(email)
            self.assertFalse(result)

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
