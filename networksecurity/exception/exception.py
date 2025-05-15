import sys

class NetworkSecurityException(Exception):
    def __init__(self, error_message: Exception, error_detail: sys):
        self.error_message = error_message
        _,_,exc_tb = error_detail.exc_info()
        self.lineno = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return f"Error occurred in python script name [{self.file_name}] line number [{self.lineno}] error message [{str(self.error_message)}]"
    


# if __name__ == "__main__":
#     try:
#         a = 1/0
#         print("This will not be printed",a)
#     except Exception as e:
#         raise NetworkSecurityException(e, sys)