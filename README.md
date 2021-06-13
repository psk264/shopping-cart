# shopping-cart project assignment
## Prerequisite
* Anaconda 3.7+
* Python 3.7+
* Pip
* Git Bash

## Objective
This repository holds the code for the shopping-cart project.    
### This programs has following capabilities:
1. Read and store products data two ways: (i) list of dictionaries  (ii) google sheet for ease of scalability and maintainability 
2. Let the checkout clerk, view the list of all valid product IDs and enter the products IDs during checkout
3. Let Admin input the tax rate through environment variable.  By default it is set to 8.875%.
4. Generate receipt with list of selected products, quantity, price, subtotal, tax and total amount.  The receipt also shows the store name and website at top and prints a Thank you message in the bottom. Here is an example of approach 1:  <img src="https://user-images.githubusercontent.com/84349071/121815589-3f324180-cc45-11eb-90a2-cf70885e3861.png" alt="command-line-output" width="650" height="650"> 
OR for approach 2:
<img src="https://user-images.githubusercontent.com/84349071/121816481-e4e7af80-cc49-11eb-9894-143bdd292965.png" alt="command-line-output_price_per_lb" width="650" height="650">
5. Receipt is also stored in the file under receipts folder for easy viewing and printing ![receipt-price-per-pound-stored-in-file](https://user-images.githubusercontent.com/84349071/121815599-4bb69a00-cc45-11eb-9380-d5753f19eb05.png)
6. Receipt is also emailed to the customer at their email address  ![receipt-sent-via-email](https://user-images.githubusercontent.com/84349071/121815602-4fe2b780-cc45-11eb-93f7-093d39415f74.png)

### This program is implemented with 2 appraoches:
1. Approach 1 - Products data supports only price per item
2. Approach 2 - Products data supports both quantity with price per pound and price per item  
**NOTE:** Both approach support all the capabilities mentioned above. 

To launch the program in first mode with approach 1 using command line please use the script file [**_shopping-cart.py_**](https://github.com/psk264/shopping-cart/blob/main/shopping_cart.py) and to launch program in mode with approach 2 use the script file [**_shopping_cart_price_per_lb.py_**](https://github.com/psk264/shopping-cart/blob/main/shopping_cart_price_per_lb.py) in following instructions. 

## Third-party Packages
* [python-dotenv](https://pypi.org/project/python-dotenv/)
* [sendgrid](https://github.com/sendgrid/sendgrid-python)
* [gspread](https://github.com/burnash/gspread) 
* [oauth2client](https://pypi.org/project/oauth2client/)

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
