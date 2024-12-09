import smtplib

my_email = "testtestest@gmail.com"
password = "abcd123()"

# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(
#     from_addr = my_email,
#     to_addrs="fountoulimaria11@gmail.com",
#     msg="Subject:Hello \n\nThis is the body of my email"
# )
# connection.close()

##=================================

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr = my_email,
#         to_addrs="testtest@gmail.com",
#         msg="Subject:Hello \n\nThis is the body of my email"
#     )


import datetime as dt
import random

# now = dt.datetime.now()
# year = now.year
# print(now)
# print(type(now))
# print(year)
# print(type(year))
#
# month=now.month
# day_of_week= now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4)
# print(date_of_birth)







now = dt.datetime.now()
weekday=now.weekday()
if weekday==0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)
    # connection = smtplib.SMTP("")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendemail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"subject: monday motivation \n\n{quote}")
