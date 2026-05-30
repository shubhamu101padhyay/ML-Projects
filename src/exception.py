import sys
from src.logger import logging  # Agar logging use karna ho toh

def error_message_detail(error, error_detail: sys):
    # FIX 1: exc.tb ko exc_tb kiya (underscore use hoga)
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    
    # FIX 2: [{0}] ka bracket sahi kiya
    error_message = "Error Occurred in python script [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error, error_detail: sys):
        # FIX 3: super().__init__ mein 'error' pass hoga, 'error_message' nahi
        super().__init__(error)
        self.error_message = error_message_detail(error, error_detail=error_detail)

    def __str__(self):
        return self.error_message
