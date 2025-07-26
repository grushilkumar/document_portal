import sys
import traceback
from logger.custom_logger import CustomLogger

# Initialize the custom logger
logger = CustomLogger().get_logger("__file__")


# Custom exception class for DocumentPortal
class DocumentPortalException(Exception):
    """Custom exception for DocumentPortal errors."""
    def  __init__(self, error_message:str, error_details):
        _,_,exc_tb = error_details.exc_info()
        self.file_name = exc_tb.tb_frame.f_code.co_filename
        self.line_number = exc_tb.tb_lineno
        self.error_message = str(error_message)
        self.traceback_str = ''.join(traceback.format_exception(*error_details.exc_info()))



    def __str__(self):
        return f"""
        Error occurred in file {self.file_name} at line {self.line_number}: {self.error_message}\nTraceback:\n{self.traceback_str}
        """

if __name__ == "__main__":
    try:
        # Simulate an error
        a = 1 / 0
        print(a)
    except Exception as e:
        # Catch the exception and raise a custom DocumentPortalException
        app_exc = DocumentPortalException(str(e), sys)
        logger.error(app_exc)
        raise app_exc