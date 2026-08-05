#Using Ethereal Email
import datetime as dt
import pandas
import smtplib
import random
import os

my_name = os.environ.get("MY_EMAIL")
password = os.environ.get("MY_PASSWORD")

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
data = pandas.read_csv('birthdays.csv')
data_dictionary = data.to_dict('records')
print(data_dictionary)
now = dt.datetime.now()
today = (now.day,now.month)
for item in data_dictionary:
    NAME = item["name"]
    if (item["day"],item["month"]) == today:
        with open(f"./letter_templates/letter_{random.randint(1,3)}.txt","r") as letter:
            new_letter = letter.read()
            new_letter = new_letter.replace("[NAME]",NAME)

        with smtplib.SMTP("smtp.ethereal.email",587) as connection:
                connection.starttls()
                connection.login(user=my_name, password=password)
                connection.sendmail(from_addr=my_name,to_addrs=my_name,msg=f"Subject:Happy Birthday!\n\n{new_letter}".encode("utf-8"))



# import os and use it to get the Github repository secrets
#MY_EMAIL = os.environ.get("MY_EMAIL")
#MY_PASSWORD = os.environ.get("MY_PASSWORD")

