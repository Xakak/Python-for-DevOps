import re
#1 symbol
#1 Capital
#4 small
#6 numbers

""" pattern = re.compile("^[^A-Za-z0-9]{1}[A-Z]{1}[a-z]{5}[0-9]{6}$")
n = input("Enter the phrase you want to search pattern in: ")

print(pattern.search(n))
 """

#password length should meet a standaed length:
""" pattern = re.compile("^.{10}$")
password = input("Enter a 10 digits key: ")
if pattern.search(password):
   print(f"{password} is Valid.")
else:
   print(f"Key length is {len(password)},therefore invalid.")
 """
#valid email checker:
""" pattern = re.compile("^[a-zA-Z0-9\.\-_]+@{1}[a-zA-Z0-9]+\.{1}[a-zA-Z]{3}$")
email = input("Enter your email: ")
print(pattern.search(email))
 """



