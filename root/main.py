# from books.utils import database
"""
the file that we are runnin right now should not contain any relative paths as resolution of relative paths require 
us to go to the parent dir and the main file does not have any parent in the package

so,
    MAIN RUNNING SCRIPT FILE SHOULD NOT HAVE ANY RELATIVE IMPORTS ....
    AND ALL THE FILES THAT ARE USING RELATIVE IMPORTS SHOULD ALSO NOT HAVE ANY IMPORT THAT TAKES THEM TO THE ROOT DIR...

"""
from books import books
print("This is main.py")