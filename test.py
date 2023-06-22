from robotics import Robot
from validation import Validator
from main import url_formatter
import unittest

class TestMethods(unittest.TestCase):
    #This class runs unit tests on a series of self-made methods that I 
    # believe should be tested for correct behaviour

    #In a large-scale environment, we'd split these tests into their own seperate
    # test files pertaining to their own component i.e. validation.py would have a
    # test class called test_validation.py file that contains tests for methods in 
    # that class. For now, this is enough.

    # Also, we keep different cases within a single test, conventionally, we'd
    # seperate them and keep a single method for a single case, but again, this is 
    # sufficient for this small use case.

    def test_robot_age_calculator(self):
        # Test normal cases
        #   Test 1: Age after a day (0 expected)
        self.assertEqual(Robot.age_calculator("2000-01-01","2000-01-02"),0)
        #   Test 2: Age after a year (1 expected)
        self.assertEqual(Robot.age_calculator("2000-01-01","2001-01-01"),1)
        #   Test 3: Age 11 months (0 expected)
        self.assertEqual(Robot.age_calculator("2000-02-01","2001-01-01"),0)
        #   Test 4: Age after 364 days(0 expected)
        self.assertEqual(Robot.age_calculator("2000-02-04","2001-02-03"),0)

        #Test edge cases (Should not occur, but we should check correct behaviour)
        #   Test 5: Age with negative 1 days(-1 expected)
        self.assertEqual(Robot.age_calculator("2000-01-02","2000-01-01"),-1)
        #   Test 6: Age with negative 365 days(-1 expected)
        self.assertEqual(Robot.age_calculator("2000-01-01","1999-01-01"),-1)


    def test_robot_date_formatter(self):
        # Test 1: Basic string (No changes expected)
        self.assertEqual(Robot.date_formatter("2000-01-01"),"2000-01-01")

        # Test 2: String with extra characters ('()' removed to be expected)
        self.assertEqual(Robot.date_formatter("(2000-01-01)"),"2000-01-01")

        # Test 3: String with extra characters (No match expected, error expected)
        with self.assertRaises(AttributeError):
            self.assertEqual(Robot.date_formatter("200a-01-01"),None)
        
        # Test 4: String with extra characters (No match expected, error expected)
        with self.assertRaises(AttributeError):
            self.assertEqual(Robot.date_formatter("2000/01/01"),None)

    def test_validator_not_null(self):
        # Test 1: Basic input (Input object to be returned expected)
        self.assertEqual(Validator.not_null(1,"Integer"),1)
        
        # Test 2: Basic empty(Input object to be returned expected)
        self.assertEqual(Validator.not_null("","String"),"")

        # Test 3: Null object (Error expected)
        with self.assertRaises(Exception):
            self.assertEqual(Validator.not_null(None,"Integer"),"")

    def test_validator_check_age(self):
        # Test 1: Input of 1 (Input object to be returned expected)
        self.assertEqual(Validator.check_age(1,"Test"),1)
        
        # Test 2: Input of 0 (Input object to be returned expected)
        self.assertEqual(Validator.check_age(0,"Test"),0)

        # Test 3: Input of -1 (Error expected)
        with self.assertRaises(Exception):
            self.assertEqual(Validator.check_age(-1,"Test"),-1) 
        
        # Test 4: Input of 1.1 float (Error expected)
        with self.assertRaises(Exception):
            self.assertEqual(Validator.check_age(1.1,"Test"),1.1) 

        # Test 5: Input of -1.1 float (Error expected)
        with self.assertRaises(Exception):
            self.assertEqual(Validator.check_age(-1.1,"Test"),-1.1) 

    def test_main_url_formatter(self):
        #Test 1: Two string input (Concatenated string with replacement expected)
        self.assertEqual(url_formatter("test.com/","testing 00"),"test.com/testing_00")

        #Test 2: First emptry string input, second normal string (Concatenated string with replacement expected)
        self.assertEqual(url_formatter("","testing 00"),"testing_00")

        #Test 3: First normal string input, second empty string (Concatenated string with replacement expected)
        self.assertEqual(url_formatter("test.com/",""),"test.com/")

        #Test 4: Two emptry string inputs (Concatenated string with replacement expected)
        self.assertEqual(url_formatter("",""),"")

        #Test 5: No changes required strings (Same concatenated string input to be expected)
        self.assertEqual(url_formatter("test.com/","testing_00"),"test.com/testing_00")


if __name__ == '__main__':
    unittest.main()