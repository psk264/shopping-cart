import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import datetime
import smtplib
 
# Following custom function (NOT COMPLETE) is to send the email receipt via email 
# .. using SendGrid's Python Library: https://github.com/sendgrid/sendgrid-python
# SendGrid blocked my account so I was unable to complete this part of code 
# .. but I used SMTP as a workaround, seen below. 

def send_email_receipt_sendgrid():
    load_dotenv()

    SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", default="OOPS, please set env var called 'SENDGRID_API_KEY'")
    SENDER_ADDRESS = os.getenv("SENDER_ADDRESS", default="OOPS, please set env var called 'SENDER_ADDRESS'")
    CUSTOMER_ADDRESS = input("Please enter customer's email address", default=SENDER_ADDRESS)
    client = SendGridAPIClient(SENDGRID_API_KEY) #> <class 'sendgrid.sendgrid.SendGridAPIClient>
    print("CLIENT:", type(client))

    subject = "Your Receipt from the Green Grocery Store"

    html_content = "Hello World"
    print("HTML:", html_content)

    # FYI: we'll need to use our verified SENDER_ADDRESS as the `from_email` param
    # ... but we can customize the `to_emails` param to send to other addresses
    message = Mail(from_email=SENDER_ADDRESS, to_emails=CUSTOMER_ADDRESS, subject=subject, html_content=html_content)

    try:
        response = client.send(message)

        print("RESPONSE:", type(response)) #> <class 'python_http_client.client.Response'>
        print(response.status_code) #> 202 indicates SUCCESS
        print(response.body)
        print(response.headers)

    except Exception as err:
        print(type(err))
        print(err)

#
#!/usr/bin/python3
# ---------------------------------------------------------------------- #
# Following custom function is to send the receipt via email (gmail smtp)
# ... Reference: https://www.tutorialspoint.com/send-mail-from-your-gmail-account-using-python
# ... This code block requires a gmail account without 2-factor authentication
# ... Also, less secure access enabled as mentioned in above article
# ---------------------------------------------------------------------- #

def send_email_receipt_smtp(receipt_text):
    load_dotenv()
    SENDER_ADDRESS = os.getenv("GMAIL_SENDER", default="OOPS, please set env var called 'SENDER_ADDRESS'")
    SENDER_AUTH = os.getenv("GMAIL_AUTH")
    EMAIL_SERVER = os.getenv("EMAIL_SERVER_SMTP")
    CUSTOMER_ADDRESS=SENDER_ADDRESS #Send default value in case of empty customer email address
    CUSTOMER_ADDRESS = input("Please enter customer's email address: ")

    while len(CUSTOMER_ADDRESS)>0:
        if("@" not in CUSTOMER_ADDRESS and "." not in CUSTOMER_ADDRESS):
            print("Sorry, you entered invalid email address")
            print("Please review and print the receipt instead. A copy of receipt is stored in receipts directory")
            return
        else:
            break

    sender = SENDER_ADDRESS
    receivers = [CUSTOMER_ADDRESS]

    message = """Subject: Receipt -  GREEN FOODS GROCERY""" + receipt_text

    try:
        smtpObj = smtplib.SMTP(EMAIL_SERVER, 587)
        smtpObj.starttls() #enable security
        smtpObj.login(SENDER_ADDRESS, SENDER_AUTH) #login with mail_id and password
        smtpObj.sendmail(sender, receivers, message)         
        print("Successfully sent email")
    except Exception as SMTPException:
        print("Error: unable to send email")

# ---------------------------------------------------------------------- #
# Following custom function is to write the receipt in the file
# ... the file is stored under receipts\ directory with file name
# ... based on the system timestamp
# ---------------------------------------------------------------------- #
def store_receipt_in_file(receipt_txt):
    if(len(receipt_txt)>0):
        dir_name = "receipts"
        try:
            os.mkdir("receipts")        
        except FileExistsError:
            print("Direcotry \'receipts\' already exists!")

        current_date = datetime.datetime.now()
        file_name =  dir_name + "\\"+ current_date.strftime("%Y-%m-%d-%H-%M-%S-%f"+".txt")
        print(file_name) 

        with open(file_name, "w") as file:
            file.write(receipt_txt)
    else:
        print("Sorry, receipt file cannot be save! No receipt text found.")
        exit()