# -------------------------------------------------------------------------- #
# Title: Assignment08
# Desc: This assignments demonstrates how classes can be moved to individual
# application files and the inclusion of Unit Tests for code validation.
# Change Log: (Who, When, What)
#   Jeremy Peters, 12/03/2024, Initial file creation
#   Jeremy Peters, 12/09/2024, Splitting classes to individual files
# -------------------------------------------------------------------------- #
from data_classes import Employee, FILE_NAME, MENU
from processing_classes import FileProcessor
from presentation_classes import IO

employees: list = []  # a table of employee data
menu_choice = ''

# Check if file exists and if not, create empty file
FileProcessor.file_check(file=FILE_NAME)

# Beginning of the main body of this script
employees = FileProcessor.read_employee_data_from_file(
    file_name=FILE_NAME, employee_data=employees, employee_type=Employee)

# Repeat the follow tasks
while True:
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":  # Get new data (and display the change)
        try:
            employees = IO.input_employee_data(
                employee_data=employees, employee_type=Employee)
            IO.output_employee_data(employee_data=employees)
        except Exception as e:
            IO.output_error_messages(e)
        continue

    elif menu_choice == "2":  # Display current data
        try:
            employees = IO.input_employee_data(employee_data=employees, employee_type=Employee)
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
