import unittest
from unittest.mock import patch

from data_classes import Employee
from presentation_classes import IO


class TestIO(unittest.TestCase):
    """
    These tests verify the functionality of user input and output methods.
    """
    @patch("builtins.input", side_effect=["1"])
    def test_input_menu_choice_valid(self, mock_input):
        """
        Test the input_menu_choice method with a valid menu choice.
        The method should return the user's menu choice as a string.

        Mocked Input:
            - "1" (valid menu choice)

        Expected Output:
            - "1" (valid menu choice is returned)
        """
        self.assertEqual(IO.input_menu_choice(), "1")

    @patch("builtins.input", side_effect=["5"])
    @patch("presentation_classes.IO.output_error_messages")
    def test_input_menu_choice_invalid(self, mock_output, mock_input):
        """
        Test the input_menu_choice method with an invalid menu choice.

        The method should handle invalid input gracefully and call
        the output_error_messages method to display an error message.

        Mocked Input:
            - "5" (invalid menu choice)

        Expected Behavior:
            - The method should return "5".
            - output_error_messages should be called once to display an error.
        """
        self.assertEqual(IO.input_menu_choice(), "5")
        mock_output.assert_called_once()

    @patch("builtins.input", side_effect=["John", "Doe", "2023-12-01", "5"])
    def test_input_employee_data(self, mock_input):
        """
        Test the input_employee_data method for adding a new employee.

        This method gathers employee data from the user and appends it
        to the provided employee_data list as an Employee object.

        Mocked Input:
            - First name: "John"
            - Last name: "Doe"
            - Review date: "2023-12-01"
            - Review rating: "5"

        Expected Output:
            - The employee_data list should have one Employee object with
              the provided data.
        """
        employee_data = []
        result = IO.input_employee_data(employee_data, Employee)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].first_name, "John")
        self.assertEqual(result[0].review_rating, 5)

if __name__ == "__main__":
    unittest.main()