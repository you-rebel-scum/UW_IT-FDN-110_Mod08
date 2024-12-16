# EmployeeRatings Application

## Overview

The **EmployeeRatings** application is a Python program designed to manage and track employee performance ratings. It allows users to:
1. Enter new employee rating data.
2. View existing employee rating data.
3. Save employee data to a JSON file for persistent storage.

The application provides a simple menu-driven interface for user interaction and ensures data integrity through input validation and structured processing.

---
## Features

- **Data Management**:
  - Stores employee information, including first name, last name, review date, and review rating (1–5 scale).
  - Handles data validation to ensure correct input formats.
  - Supports persistent data storage using JSON files.

- **User-Friendly Interface**:
  - Displays a menu with clear options for adding, viewing, saving, or exiting.
  - Outputs descriptive feedback for actions performed.

- **Error Handling**:
  - Handles input errors and displays user-friendly error messages.

---
## Installation

1. Clone the repository or download the source files.
2. Ensure you have Python 3.7+ installed on your system.
3. Install any required dependencies (if applicable).

---
## Usage

1. Run the application by executing `main.py`:
```
python main.py
```
2. Follow the menu prompts to interact with the application:
   - Option 1: Enter new employee rating data.
   - Option 2: View current employee rating data.
   - Option 3: Save data to a file.
   - Option 4: Exit the program.
3. Employee data is stored in the EmployeeRatings.json file for future use.

---
## File Structure
1. main.py:
   - The entry point of the application.
   - Manages program flow and user interaction.
2. presentation_classes.py:
   - Contains the IO class, responsible for user input and output, including:
     - Displaying menus.
     - Capturing user choices.
     - Displaying employee data and error messages.
3. processing_classes.py:
   - Defines the FileProcessor class for file-related operations:
     - Reading and writing employee data to/from a JSON file.
     - Ensuring file existence.
4. data_classes.py:
   - Contains the Person and Employee classes, which represent core data models with properties like first_name, last_name, review_date, and review_rating.

---
## Employee Ratings Guide
The employee rating system uses a scale of 1 to 5:
1. Not Meeting Expectations
2. Building
3. Solid
4. Strong
5. Leading

---
## Example Interaction
```
---- Employee Ratings ------------------------------
  Select from the following menu:
    1. Enter new employee rating data.
    2. Show current employee rating data.
    3. Save data to a file.
    4. Exit the program.
--------------------------------------------------

Enter your menu choice number: 1
What is the employee's first name? John
What is the employee's last name? Doe
What is their review date? 2024-12-01
What is their review rating? 5
```

---
## Error Handling
- **Invalid Data:**
  - Inputs are validated for data type and range. For example, entering a 
  non-integer for the review rating will trigger an error message.
- **File Issues:**
  - If the data file is missing, it is created automatically.

---

## Contributing
Contributions are welcome! Please feel free to fork the repository, create a new branch, and submit a pull request.

---
## Author
Developed by [Jeremy Peters](mailto:jdp277@uw.edu) as part of the UW IT 
Foundations 110 course.