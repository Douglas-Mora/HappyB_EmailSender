# ----------------- **Happy Birthday Email Sender**, by Douglas Mora
# ----------------- Questions? douglas-mora@outlook.com // github.com/Douglas-Mora
# ----------------- The idea? It was taken from Dr. Angela Yu's Udemy's course...:
# ----------------- 100 Days of Code - The Complete Python Pro Bootcamp for 2021



The purpose of this piece of code is, from a list of persons' birthdays ("birthdays.csv"), it will 
validate, each day, if there are persons on their birthday, then it will send greeting emails to them.
One out of three sample txt letters would be picked up and updated with the person's name, then the
letter will be included as if the email's body. It also adds random quotes at the end of the email,
taken from "quotes.txt" file.

To run and test the code you´ll need to update in 4 places:
 1) Make your own list of birthdays into the "birthdays.csv" file.
 2) "sender_email", with your own email, from where emails will be sent.
 3) "sender_email_password".
 4) "SMTP" [Simple Mail Transfer Protocol], as per your email's domain.
     This address is needed to match your email provider, for instance:
      - For a "@gmail.com" email, SMTP will be "smtp.gmail.com".
      - For a "@yahoo.com": "smtp.mail.yahoo.com".
      - For a "@outlook.com": "smtp-mail.outlook.com".


Important!
As per email providers' security configuration, for the code to work, you will need to sign-in into your
email and make it allows less secure apps. For instance, in case of gmail, steps as of April 2021 would be:
- "Manage your Google Account"
  - "Security"
    - "Signing into Google"
      - "User your phone to sign in" [this needs to be "off"]
      - "2-step Verification" [this needs to be "off"]
    - "Less secure app access" [this needs to be turned "On"]


At the end, the email should look like so:

Subject: Happy birthday!

Dear Emma,

Happy birthday!

All the best for the year!

Douglas

--------------------
"Success is liking yourself, liking what you do, and liking how you do it." - Maya Angelou
