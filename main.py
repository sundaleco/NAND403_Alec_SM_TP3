
import importlib
import ui
importlib.reload(ui)

import os 
import sys

a_path = os.path.abspath(__file__)
a_folder_path = os.path.dirname(a_path)
sys.path.append(a_folder_path)

def main():

    global widget
    
    try:
        widget.close()
    except:
        pass

    widget = ui.ProgramUI()
    widget.show()

main()        

