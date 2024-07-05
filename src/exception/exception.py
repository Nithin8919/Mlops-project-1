import sys

class customexception(Exception):
    def __init__(self, error_message, error_details: sys):
        self.error_message = error_message
        _, _, exc_tb = error_details.exc_info()  # Get the traceback object exc_info = execution info tb = trace back
        self.lineno = exc_tb.tb_lineno  # Get the line number where the exception occurred
        self.file_name = exc_tb.tb_frame.f_code.co_filename  # Get the file name where the exception occurred

    def __str__(self):
        # Format the custom error message
        return "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
            self.file_name, self.lineno, str(self.error_message))

if __name__ == "__main__":
    try:
        a = 1 / 0  # This will raise a ZeroDivisionError
    except Exception as e:
        raise customexception(e, sys)  # Raise the custom exception with the error message and sys module
