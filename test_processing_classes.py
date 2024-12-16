# -------------------------------------------------------------------------- #
# Title: Assignment08 - processing_classes Unit Testing
# Desc: Tests for the processing_classes module
# Change Log: (Who, When, What)
#   Jeremy Peters, 12/15/2024, Initial file creation
# -------------------------------------------------------------------------- #
import json
import unittest
from unittest.mock import patch, mock_open
from processing_classes import FileProcessor
from data_classes import Employee, FILE_NAME


class FileProcessingTest(unittest.TestCase):
    """
    These tests cover the file operations for reading, writing, and
    checking the existence of JSON files that store employee data.
    """
    @patch("os.path.exists")
    @patch("os.path.getsize")
    @patch("builtins.open", new_callable=mock_open, read_data="[]")
    def test_file_check_creates_file(
            self, mock_file, mock_getsize, mock_exists):
        """
        Test that the file_check method creates a new file when the
        specified file does not exist or is empty.

        Mocked Behavior:
            - `os.path.exists` returns False, simulating a non-existent file.
            - `os.path.getsize` returns 0, simulating an empty file.

        Expected Outcome:
            - A new file is created and initialized with an empty JSON array.
        """
        mock_exists.return_value = False
        mock_getsize.return_value = 0
        FileProcessor.file_check(FILE_NAME)
        mock_file.assert_called_with(FILE_NAME, "w")

    @patch("os.path.exists")
    @patch("os.path.getsize")
    def test_file_check_exists(self, mock_getsize, mock_exists):
        """
        Test that the file_check method does not create a file if it
        already exists and contains data.

        Mocked Behavior:
            - `os.path.exists` returns True, simulating an existing file.
            - `os.path.getsize` returns a non-zero value, simulating
               a file with data.

        Expected Outcome:
            - The file is not overwritten or recreated.
        """
        mock_exists.return_value = True
        mock_getsize.return_value = 100
        with patch("builtins.open", mock_open(read_data="[]")) as mock_file:
            FileProcessor.file_check(FILE_NAME)
            mock_file.assert_not_called()

    @patch("builtins.open", new_callable=mock_open, read_data='[{\
"FirstName": "Vic", "LastName": "Doe", "ReviewDate": "2024-01-01", \
"ReviewRating": 5}]')
    def test_read_employee_data_from_file(self, mock_file):
        """
        Tests that the read_employee_data_from_file method correctly
        reads employee data from a JSON file and converts it into
        Employee objects.

        Mocked Behavior:
            - A JSON file contains one employee record.

        Expected Outcome:
            - The method returns a list with one Employee object.
            - The Employee object's attributes match the data in the file.
        """
        employee_data = []
        result = FileProcessor.read_employee_data_from_file(
            FILE_NAME, employee_data, Employee)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].first_name, "Vic")
        self.assertEqual(result[0].review_rating, 5)



    # @patch("builtins.open", new_callable=mock_open)
    def test_write_employee_data_to_file(self):
        """
        Test that the write_employee_data_to_file method correctly
        writes employee data to a JSON file.

        Test Setup:
            - Create a list of Employee objects with sample data.

        Expected Outcome:
            - The file is written with JSON data matching the
              attributes of the Employee objects.
            - The data in the file matches the original Employee objects.
        """
        employee_data = [
            Employee("Vic", "Vu", "2024-01-01", 5),
            Employee("Bill", "Gates", "2024-01-01", 4),
            Employee("Steve", "Jobs", "2024-01-01", 4)
        ]

        # Call function to write sample data to a temporary file
        FileProcessor.write_employee_data_to_file(FILE_NAME, employee_data)

        with open(FILE_NAME, "r") as file:
            file_data = json.load(file)
            self.assertEqual(file_data[0]["FirstName"], "Vic")
            self.assertEqual(file_data[1]["LastName"], "Gates")
            self.assertEqual(file_data[0]["ReviewDate"], "2024-01-01")
            self.assertEqual(file_data[2]["ReviewRating"], 4)

if __name__ == "__main__":
    unittest.main()