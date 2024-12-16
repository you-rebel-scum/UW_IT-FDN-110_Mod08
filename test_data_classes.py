# -------------------------------------------------------------------------- #
# Title: Assignment08 - data_classes Unit Testing
# Desc: Tests for the data_classes module
# Change Log: (Who, When, What)
#   Jeremy Peters, 12/11/2024, Initial file creation
# -------------------------------------------------------------------------- #

import unittest
from data_classes import Person, Employee

class TestPerson(unittest.TestCase):
    """
    These tests validate the proper setting and validation of first
    and last names, as well as the string representation of a Person.
    """

    def test_valid_first_name_setter(self):
        """
        Test that the first_name property setter accepts valid names.

        Expected Outcome:
            - The first_name attribute is set correctly.
        """
        person = Person()
        person.first_name = "Vic"
        self.assertEqual(person.first_name, "Vic")

    def test_invalid_first_name(self):
        """
        Test that the first_name property setter raises a ValueError
        when given an invalid name (e.g., containing digits).

        Expected Outcome:
            - A ValueError is raised.
        """
        person = Person()
        with self.assertRaises(ValueError):
            person.first_name = "123Vic"

    def test_valid_last_name_setter(self):
        """
        Test that the last_name property setter accepts valid names.

        Expected Outcome:
            - The last_name attribute is set correctly.
        """
        person = Person()
        person.last_name = "Vu"
        self.assertEqual(person.last_name, "Vu")

    def test_invalid_last_name(self):
        """
        Test that the last_name property setter raises a ValueError
        when given an invalid name (e.g., containing digits).

        Expected Outcome:
            - A ValueError is raised.
        """
        person = Person()
        with self.assertRaises(ValueError):
            person.last_name = "456Vu"

    def test_person_str(self):
        """
        Test the string representation of a Person object.

        Expected Outcome:
            - The string representation matches the format 'FirstName,LastName'.
        """
        person = Person("Vic", "Vu")
        self.assertEqual(str(person), "Vic,Vu")

class TestEmployee(unittest.TestCase):
    """
    Unit tests for the Employee class in data_classes.py.

    These tests cover initialization, attribute validation, and
    string representation of an Employee, which extends Person.
    """

    def test_employee_init(self):
        """
        Test the initialization of an Employee object with valid attributes.

        Expected Outcome:
            - All attributes are correctly set upon initialization.
        """
        employee = Employee("Vic", "Vu", "2024-01-01", 5)
        self.assertEqual(employee.first_name, "Vic")
        self.assertEqual(employee.last_name, "Vu")
        self.assertEqual(employee.review_date, "2024-01-01")
        self.assertEqual(employee.review_rating, 5)

    def test_valid_review_date(self):
        """
        Test that the review_date property setter accepts valid dates.

        Expected Outcome:
            - The review_date attribute is set correctly.
        """
        employee = Employee()
        employee.review_date = "2024-01-01"
        self.assertEqual(employee.review_date, "2024-01-01")

    def test_invalid_review_date(self):
        """
        Test that the review_date property setter raises a ValueError
        when given an invalid date (not in 'YYYY-MM-DD' format).

        Expected Outcome:
            - A ValueError is raised.
        """
        employee = Employee()
        with self.assertRaises(ValueError):
            employee.review_date = "01-01-2024"

    def test_valid_review_rating(self):
        """
        Test that the review_rating property setter accepts valid ratings
        (integer values between 1 and 5).

        Expected Outcome:
            - The review_rating attribute is set correctly.
        """
        employee = Employee()
        employee.review_rating = 5
        self.assertEqual(employee.review_rating, 5)

    def test_invalid_review_rating(self):
        """
        Test that the review_rating property setter raises a ValueError
        when given an invalid rating (e.g., outside the range 1-5).

        Expected Outcome:
            - A ValueError is raised.
        """
        employee = Employee()
        with self.assertRaises(ValueError):
            employee.review_rating = 10

    def test_employee_str(self):
        """
        Test the string representation of an Employee object.

        Expected Outcome:
            - The string representation matches the format
              'FirstName,LastName,ReviewDate,ReviewRating'.
        """
        employee = Employee("Vic", "Vu", "2024-01-01", 5)
        self.assertEqual(str(employee), "Vic,Vu,2024-01-01,5")

if __name__ == "__main__":
    unittest.main()