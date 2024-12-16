import json
import os
from presentation_classes import IO


class FileProcessor:
    """
    A collection of processing layer functions that work with Json files
    """

    @staticmethod
    def read_employee_data_from_file(file_name: str, employee_data: list,
                                     employee_type):
        """
        This function reads data from a json file and loads it into a
        list of dictionary rows

        :param file_name: string data with name of file to read from
        :param employee_data: list of dictionary rows filled with file data
        :param employee_type: an reference to the Employee class
        :return: list
        """
        try:
            with open(file_name, "r") as file:
                list_of_dictionary_data = json.load(file)
                for employee in list_of_dictionary_data:
                    employee_object = employee_type()
                    employee_object.first_name = employee["FirstName"]
                    employee_object.last_name = employee["LastName"]
                    employee_object.review_date = employee["ReviewDate"]
                    employee_object.review_rating = employee["ReviewRating"]
                    employee_data.append(employee_object)
        except FileNotFoundError:
            raise FileNotFoundError(
                "Text file must exist before running this script!")
        except Exception:
            raise Exception("There was a non-specific error!")
        return employee_data

    @staticmethod
    def write_employee_data_to_file(file_name: str, employee_data: list):
        """
        This function writes data to a json file with data from a
        list of dictionary rows

        :param file_name: string data with name of file to write to
        :param employee_data: list of dictionary rows to be writen to the file

        :return: None
        """
        try:
            list_of_dictionary_data: list = []
            for employee in employee_data:
                employee_json: dict = {
                    "FirstName": employee.first_name,
                    "LastName": employee.last_name,
                    "ReviewDate": employee.review_date,
                    "ReviewRating": employee.review_rating
                }
                list_of_dictionary_data.append(employee_json)

            with open(file_name, "w") as file:
                json.dump(list_of_dictionary_data, file)
                print(f"The following was saved to file:")
                IO.output_employee_data(employee_data=employee_data)
        except TypeError:
            raise TypeError(
                "Please check that the data is a valid JSON format")
        except PermissionError:
            raise PermissionError(
                "Please check the data file's read/write permission")
        except Exception as e:
            print(e)
            # raise Exception("There was a non-specific error!")

    @staticmethod
    def file_check(file):
        """
        Checks that the file exists, and if it isn't present,
        it creates an empty file.
        """
        try:
            print(f"Checking for existing file {file}...")
            if (not os.path.exists(file)) or (os.path.getsize(
                    file) == 0):
                print(f"No existing file {file} found. File will be created.")
                with open(file, "w") as file:
                    file.write("[]")
            else:
                print(f"File {file} already exists!")
        finally:
            pass


if __name__ == "__main__":
    print(f"This is a dependent method. Please run main.py instead.")
