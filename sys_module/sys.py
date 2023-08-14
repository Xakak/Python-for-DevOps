import sys
import os

#Write a Python program that takes in a path as a command-line argument and prints out the contents of the file. 
# If the file does not exist, the program should print an error message to the standard error stream and exit 
# with a non-zero exit code.



if not os.path.exists(sys.argv[1]):
    print("Error:Provided path is invalid")
    sys.exit()
else:
    os.chdir(sys.argv[1])
    os.system("ls")



