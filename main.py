##################### Hard Starting Project ######################
from  datetime import datetime
import pandas
import random
import smtplib


my_email = "officialvishal19388@gmail.com"
password = "my_psw_demo"

today = datetime.now()
today_tuple = (today.month,today.day)

data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row["month"],data_row["day"]):data_row for (index,data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com",port=587) as connections:
        connections.starttls()
        connections.login(my_email,password=password)
        connections.sendmail(
            from_addr= my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday! \n\n{contents}"
        )
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with
# the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)



