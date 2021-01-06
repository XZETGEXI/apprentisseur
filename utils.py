import os
import time

from pprint import pprint



def tic(): return time.time()

def toc(start):
    end = time.time()
    msg = "TIME %.02f s" % (end - start)
    print(msg.center(w, "_"))
    return end



def logger(verbose = True):
    """ Logger initiation """
    
    W, H = os.get_terminal_size()
    def log(*arg):
        if verbose:
            print("_" * W)
            msgs = [*arg]
            for msg in msgs:
                print(str(msg).upper().rjust(W, "|"))
            print("‾" * W)
    return log



def file_selector_corrected(dir_path = None):
    """ File selector with numbered files, ignores folders """
    
    if not dir_path:
        current_dir = os.getcwd()
    elif not os.path.exists(dir_path):
        print("Invalid dir name")
        return dir_path
    else:
        current_dir = os.chdir(dir_path)
    
    file_list = [file for file in os.listdir(current_dir) if os.path.isfile(file)]
    
    if not file_list:
        print("Empty directory")
    
    for i, f in enumerate(file_list):
        print(str(i).rjust(3), "->", f)

    while True:
        try:
            user_input = int(input("Which file do you want? "))
            return file_list[user_input]
        except (ValueError, IndexError):
            print("Invalid input. Please try again.")
