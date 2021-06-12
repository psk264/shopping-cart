import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import datetime
 

def send_email_receipt():
    load_dotenv()

    SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", default="OOPS, please set env var called 'SENDGRID_API_KEY'")
    SENDER_ADDRESS = os.getenv("SENDER_ADDRESS", default="OOPS, please set env var called 'SENDER_ADDRESS'")

    client = SendGridAPIClient(SENDGRID_API_KEY) #> <class 'sendgrid.sendgrid.SendGridAPIClient>
    print("CLIENT:", type(client))

    subject = "Your Receipt from the Green Grocery Store"

    html_content = "Hello World"
    print("HTML:", html_content)

    # FYI: we'll need to use our verified SENDER_ADDRESS as the `from_email` param
    # ... but we can customize the `to_emails` param to send to other addresses
    message = Mail(from_email=SENDER_ADDRESS, to_emails=SENDER_ADDRESS, subject=subject, html_content=html_content)

    try:
        response = client.send(message)

        print("RESPONSE:", type(response)) #> <class 'python_http_client.client.Response'>
        print(response.status_code) #> 202 indicates SUCCESS
        print(response.body)
        print(response.headers)

    except Exception as err:
        print(type(err))
        print(err)

def store_receipt_in_file(receipt_txt):
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


store_receipt_in_file("TEST")