import sys
# import logging
from src.logger import logging
"""defining custom exception handling MESSAGE TO BE DISPLAYED  by referring through official doocumentation for following the principle standard"""
def error_message_detail(error, error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message=f"ERROR OCCURED IN PTHON SCRIPT [{file_name}] line_number [{exc_tb.tb_lineno}] error_message[{str(error)}]"

    return error_message

    
"""CUSTOM EXCEPTION CLASS"""
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)


    def __str__(self):
        return self.error_message    
    

if __name__=="__main__":

    try:
        a=1/0
    except  Exception as e:
        logging.info("Divide by 0 error")
        raise CustomException(e,sys)


