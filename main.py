# ------- **Happy Birthday Email Sender**, by Douglas Mora
# ------- Questions? douglas-mora@outlook.com // github.com/Douglas-Mora


# ------- Modules needed:
import smtplib
import random
from datetime import datetime
import pandas

# ------- Using "now" to determine set month and day into a tuple:
today = datetime.now()
today_tuple = (today.month, today.day)

# ------- Email nada needed (see "readme.txt"):
sender_email = "example@gmail.com"
sender_email_password = "example_password"
SMTP = "smtp.gmail.com"
email_subject = "Happy birthday!"

# ------- Using pandas to read birthdays file:
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

# ------- Looking if tuple is into "birthdays_dict":
if (today_tuple) in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    # ------- Choosing random letter:
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    # ------- Updating the letter >> output:
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
    # ------- Picking up a quote:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    # ------- Calling methods to send email:
    with smtplib.SMTP(SMTP) as connection:
        connection.starttls()
        connection.login(sender_email, sender_email_password)
        connection.sendmail(from_addr=sender_email,
                            to_addrs=birthday_person["email"], msg=f"Subject:{email_subject}\n\n{contents}\n\n{'-'*20}\n{quote}")
