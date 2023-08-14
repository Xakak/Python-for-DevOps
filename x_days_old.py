# find if something is X days old:
import timedelta
import os
import datetime

current_date = datetime.datetime.now()
# X days:
max_age = 10
directory = "/home/rayan/Pictures"
for dirpath, dir, files in os.walk(directory):
    for file in files:
        # print(file)
        file_path = os.path.join(dirpath, file)
        stat = os.stat(file_path)
        c_time = stat.st_ctime
        file_c_time = datetime.datetime.fromtimestamp(c_time)
        days = (current_date - file_c_time).days

        # print(days)
        if days > max_age:
            print(f"{file_path} is {days} days old.")

            

        




        