# always run the script in the terminal(python3 getpass_module.py) otherwise it will throw error

import getpass
import sys
# get username
my_user = getpass.getuser()
# set pass
my_pass = "hello12"
# takes in username and lowercase it
user = input("Enter your user name: ")
user.lower()
#if user is correct moves to next part
if user == my_user:
    pass
else:
    print("Invalid User")
    sys.exit()
# get pass without showing
password = getpass.getpass(prompt="Enter password:")
if password == my_pass:
    print("Success")
else:
    print("Invalid Password")
