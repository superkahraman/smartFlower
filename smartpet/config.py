# Settings and Special Functions for smartPET application
from colorama import Fore, Back, Style
from datetime import datetime

debug_level = False


def lp(mymessage):

    if debug_level != False:
        print(Fore.CYAN + ">>> ", end="")
        print(mymessage)
        print(Style.RESET_ALL, end="")

        with open("smartpet.log", "a") as log_file:
            log_message = str(mymessage)
            log_time = str(datetime.now())
            log_file.write("\n" + log_time + " " + log_message)
            log_file.close()
    else:
        return None
