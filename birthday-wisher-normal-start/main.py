from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = "testtest@gmail.com"
PASSWORD = "123456789"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")

# birthday_dict = {
#     (birthday_month, birthday_day): data_row
# }
#new_dict = {new_key: new_value for (index,data_row) in data.iterrows()}
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
#birthdays_dict = {(data_row.month, data_row.day): data_row for (index,data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    file_path=f"letter_templates/letter_{random.randint(1,3)}.txt"
    birthday_person = birthdays_dict[today_tuple]
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    print(f"Subject:Happy Birthday!\n\n{contents}")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )