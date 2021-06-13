# shopping-cart project assignment
## Prerequisite
* Anaconda 3.7+
* Python 3.7+
* Pip
* Git Bash

## Objective
This repository holds the code for the shopping-cart project.    
### This programs has following capabilities:
1. Read and store products data two ways: <br> 
   (i) list of dictionaries  
   (ii) google sheet for ease of scalability and maintainability 
2. Let the checkout clerk, view the list of all valid product IDs and enter the products IDs during checkout
3. Let Admin input the tax rate through environment variable stored in .env file.  By default it is set to 8.75%. To update the tax rate during runtime use command: 
4. Generate receipt with list of selected products, quantity, price, subtotal, tax and total amount.  The receipt also shows the store name and website at top and prints a thank you message in the bottom. <br> Here is an example of approach 1: <br>  <img src="https://user-images.githubusercontent.com/84349071/121815589-3f324180-cc45-11eb-90a2-cf70885e3861.png" alt="command-line-output" width="650" height="650"> <br>
and for approach 2: <br> <img src="https://user-images.githubusercontent.com/84349071/121816481-e4e7af80-cc49-11eb-9894-143bdd292965.png" alt="command-line-output_price_per_lb" width="650" height="650">
5. Receipt is also stored in the file under receipts folder for easy viewing and printing ![receipt-price-per-pound-stored-in-file](https://user-images.githubusercontent.com/84349071/121815599-4bb69a00-cc45-11eb-9380-d5753f19eb05.png)
6. Receipt is also emailed to the customer at their email address ![receipt-sent-via-email](https://user-images.githubusercontent.com/84349071/121815602-4fe2b780-cc45-11eb-93f7-093d39415f74.png)

### This program is implemented with 2 appraoches:
1. Approach 1 - Products data supports only price per item
2. Approach 2 - Products data supports both quantity with price per pound and price per item  
**NOTE:** Both approach support all the capabilities mentioned above. 

To launch the program in first mode with approach 1 using command line please use the script file [**_shopping-cart.py_**](https://github.com/psk264/shopping-cart/blob/main/shopping_cart.py) and to launch program in mode with approach 2 use the script file [**_shopping_cart_price_per_lb.py_**](https://github.com/psk264/shopping-cart/blob/main/shopping_cart_price_per_lb.py) in following instructions. 

## Packages
* [python-dotenv](https://pypi.org/project/python-dotenv/)
* [sendgrid](https://github.com/sendgrid/sendgrid-python)
* [gspread](https://github.com/burnash/gspread) 
* [oauth2client](https://pypi.org/project/oauth2client/)
* [smtplib](https://docs.python.org/3/library/smtplib.html)

## Setup
In in the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file to specify following information:

    TAX_RATE=0.0875
    SENDGRID_API_KEY="<key>"
    SENDER_ADDRESS="<email-id>"
    GOOGLE_SHEET_ID=<sheet-id>
    SHEET_NAME="<name-of-the-products-tab>"
    SHEET_PRICE_PER_LB="<name-of-the-products-price-per-lb>"
    EMAIL_SERVER_SMTP="smtp.gmail.com"
    GMAIL_SENDER="<gmail-email-id>"
    GMAIL_AUTH="<gmail-password>"

**NOTE:**
* **Email Receipt Configuration**: I was unable to test sending email receipt using SendGrid due to account suspension. So alternatively I used SMTP server approach using Gmail SMTP. <br> To use GMail SMTP, follow the steps:
  1. Login to gmail account 
  2. Go to Accounts Settings -> Security -> Scroll down to find "Less secure app access" and turn it ON.<br> ![image](https://user-images.githubusercontent.com/84349071/121819638-3862f900-cc5c-11eb-8721-2c647170a0fb.png)
  3. In .env file, update ```GMAIL_SENDER``` with your gmail email id and ```GMAIL_AUTH``` with gmail password
  
  **Note:** 
  * To configure SendGrid, following the instructions on Professor Rossetti's README on [sendgrid](https://github.com/prof-rossetti/intro-to-python/blob/main/notes/python/packages/sendgrid.md) 
  * After account enrollment, get the API key
  * In .env file, update ```SENDER_ADDRESS``` with your email id used to register for SendGrid account and ```SENDGRID_API_KEY``` with API key value from above step
 
* **Google Sheet Configuration**
  1. Follow the instructions on Professor Rossetti's README on [gspread](https://github.com/prof-rossetti/intro-to-python/blob/main/notes/python/packages/gspread.md) to create a project in GCP and create the ```auth\google-credentials.json``` file
  2. Note the client-email from google-credentials.json file
  3. For products data, create a copy of the google sheet: https://docs.google.com/spreadsheets/d/1zwpGSvJO1o2ssPLwKQWEiLlWLK97ahRn3TMHq5sAwSU/ into your drive.  Note the program uses sheet name to process products information.   
  4. Update the sharing permission on the google sheet, grant edit access to the client-email copied in step 2
  5. Get the sheet ID from the URL. For example, for my google sheet, ID=1zwpGSvJO1o2ssPLwKQWEiLlWLK97ahRn3TMHq5sAwSU
  6. In .env file, update ```GOOGLE_SHEET_ID``` with the ID value 
  7. Note the sheet name for products data and in .env file update ```SHEET_NAME``` with sheet name
  8. Note the sheet name for products data with quantity + price per lb and in .env file update ```SHEET_PRICE_PER_LB``` with sheet name

 


## Instructions
1. Use git client to clone or download this remote repository, [shopping-cart](https://github.com/psk264/shopping-cart), on your local machine.  Note the location where it is cloned or downloaded
2. Use command line application to navigate to the location where this repository was cloned or downloaded.  Ensure that ``<base>`` from conda initialization is shown on cmd line.  If ``<base>`` is not shown then, before proceeding, run command:<br/>
```conda init bash```
3. Since this code uses specific packages like python-dotenv, it is recommended to create a new project specific anaconda virtual environment. Here we create virtual environment name "shopping-cart-env" using following command.  To create a environment with a different name, simply replace rpc-game-env with desired name:<br/>
``` conda create -n shopping-cart-env python=3.8```
4. Activate the Anaconda environment "shopping-cart-env" using the command:<br/>
```conda activate shopping-cart-env```
5. After virtual environment is active i.e. ``<shopping-cart-env>`` is shown on command-line, then install the third-party package python-dotenv on this virtual environment using command:<br/>
 ```pip install -r requirements.txt```<br/>
**NOTE:** The requirements.txt file is already provided in the repository.
6. After the setup is complete, depending on your preference on appraoches mentioned above, start the program using one of the following commands:<br/>
Products price per item only:  ```python shopping-cart.py```   
Products price per pound and per item:  ```python shopping_cart_price_per_lb.py```  <br/>  

## Additional Information
* This repository uses google sheet to store the products data: https://docs.google.com/spreadsheets/d/1zwpGSvJO1o2ssPLwKQWEiLlWLK97ahRn3TMHq5sAwSU/
* Program has 2 approaches to store data 
  1. List of dictionaries
  2. Google Sheet
* Program has 2 approaches to send receipt 
