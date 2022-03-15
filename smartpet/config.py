# Settings and Special Functions for smartPET application
from colorama import Fore, Back, Style
from datetime import datetime

log_console = True
log_file = True

# This function writes colored debug message to Terminal


def xx(mymessage):
    if log_console == True:
        print(Fore.CYAN + ">>> ", end="")
        print(mymessage)
        print(Style.RESET_ALL, end="")
    if log_file == True:
        with open("smartpet.log", "a") as file_log:
            log_message = str(mymessage)
            log_time = str(datetime.now())
            file_log.write("\n" + log_time + " " + log_message)
            file_log.close()
    return None
