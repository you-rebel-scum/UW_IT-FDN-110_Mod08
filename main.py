# -------------------------------------------------------------------------- #
# Title: Assignment08
# Desc: This assignments demonstrates how classes can be moved to individual
# application files and the inclusion of Unit Tests for code validation.
# Change Log: (Who, When, What)
#   Jeremy Peters, 12/03/2024, Initial file creation
#   Jeremy Peters, 12/09/2024, Splitting classes to individual files
# -------------------------------------------------------------------------- #
import datetime
from processing_classes import FileProcessor
from presentation_classes import IO

# Data -------------------------------------------- #
FILE_NAME: str = 'EmployeeRatings.json'

MENU: str = '''
---- Employee Ratings ------------------------------
  Select from the following menu:
    1. Show current employee rating data.
    2. Enter new employee rating data.
    3. Save data to a file.
    4. Exit the program.
--------------------------------------------------
'''

employees: list = []  # a table of employee data
menu_choice = ''


class Person:
    """
    A class representing person data.

    Properties:
    - first_name (str): The person's first name.
    - last_name (str): The person's last name.
    """

    def __init__(self, first_name: str = "", last_name: str = ""):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self):
        return self.__first_name.title()

    @first_name.setter
    def first_name(self, value: str):
        if value.isalpha() or value == "":
            self.__first_name = value
        else:
            raise ValueError("The first name should not contain numbers.")

    @property
    def last_name(self):
        return self.__last_name.title()

    @last_name.setter
    def last_name(self, value: str):
        if value.isalpha() or value == "":
            self.__last_name = value
        else:
            raise ValueError("The last name should not contain numbers.")

    def __str__(self):
        return f"{self.first_name},{self.last_name}"


class Employee(Person):
    """
    A class representing employee data.

    Properties:
    - first_name (str): The employee's first name.
    - last_name (str): The employee's last name.
    - review_date (date): The data of the employee review.
    - review_rating (int): Review rating of the employee's performance (1-5)
    """

    employee_first_name: str = str()
    employee_last_name: str = str()
    review_date: datetime.date = "1900-01-01"
    review_rating: int = 3

    def __init__(self, first_name: str = "", last_name: str = "",
                 review_date: str = "1900-01-01", review_rating: int = 3):

        super().__init__(first_name=first_name,last_name=last_name)
        self.employee_first_name = first_name
        self.employee_last_name = last_name
        self.review_date = review_date
        self.review_rating = review_rating

    @property
    def review_date(self):
        return self.__review_date

    @review_date.setter
    def review_date(self, value: str):
        try:
            datetime.date.fromisoformat(value)
            self.__review_date = value
        except ValueError:
            raise ValueError(f"Incorrect data format, should be YYYY-MM-DD")

    @property
    def review_rating(self):
        return self.__review_rating

    @review_rating.setter
    def review_rating(self, value: str):
        if value in (1, 2, 3, 4, 5):
            self.__review_rating = value
        else:
            raise ValueError(f"Please choose only values 1 through 5")

    def __str__(self):
        return (f"{self.first_name},{self.last_name},\
{self.review_date},{self.__review_rating}")


# Beginning of the main body of this script
employees = FileProcessor.read_employee_data_from_file(
    file_name=FILE_NAME, employee_data=employees, employee_type=Employee)

# Repeat the follow tasks
while True:
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":  # Display current data
        try:
            IO.output_employee_data(employee_data=employees)
        except Exception as e:
            IO.output_error_messages(e)
        continue

    elif menu_choice == "2":  # Get new data (and display the change)
        try:
            employees = IO.input_employee_data(
                employee_data=employees, employee_type=Employee)
            IO.output_employee_data(employee_data=employees)
        except Exception as e:
            IO.output_error_messages(e)
        continue

    elif menu_choice == "3":  # Save data in a file
        try:
            FileProcessor.write_employee_data_to_file(
                file_name=FILE_NAME, employee_data=employees)
            print(f"Data was saved to the {FILE_NAME} file.")
        except Exception as e:
            IO.output_error_messages(e)
        continue

    elif menu_choice == "4":  # End the program
        break  # out of the while loop
