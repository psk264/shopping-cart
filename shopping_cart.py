# shopping_cart.py
import os
import pprint 
import datetime
from receipt_processing import store_receipt_in_file
from myfunctions import calculate_tax, to_usd 
from dotenv import load_dotenv
import product_data

load_dotenv()
# products = [
#     {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
#     {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
#     {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
#     {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
#     {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
#     {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
#     {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
#     {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
#     {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
#     {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
#     {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
#     {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
#     {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
#     {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
#     {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
#     {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
#     {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
#     {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
#     {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
#     {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
# ] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017
 
# Access products database using google sheet: https://docs.google.com/spreadsheets/d/1zwpGSvJO1o2ssPLwKQWEiLlWLK97ahRn3TMHq5sAwSU/edit#gid=1414917048
products =  product_data.get_list_products()

# TODO: write some Python code here to produce the desired output
min_id ="1"
max_id = "0"

for p in products:
    if int(p["id"])<int(min_id) : min_id = p["id"]
    elif int(p["id"])>int(max_id): max_id = p["id"]

print(min_id, max_id)

selected_ids = []
# 1) Capture products ids until we're done (use infite while loop)
# selected_id = input("Please select a valid product id or DONE: ")
# while selected_id !=  "DONE":
#     selected_id = input("Please select a valid product id or DONE: ")
#     selected_ids.append(selected_id)
# print(selected_ids)

while True:
    selected_id = input(f"Please select a valid product id between {min_id} & {max_id} or DONE: ")
    selected_id = selected_id.upper()
    try:
        if selected_id == "DONE":
            break
        elif (int(selected_id) <1 or int(selected_id) > len(products)):
            print("Hey, are you sure that product identifier is correct? Please try again!") 
        else:
            selected_ids.append(selected_id)
        print("You entered:", selected_id)
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

# print("WE HAVE REACHED THE END OF THE LOOP")
# print(selected_ids)

# 2) Perform product look ups to determine what the product name and price are
# selected_ids = ['1', '2', '3', '4', '1', '2', '3']
# look up the corresponding product!
# or maybe display the selected products later
max_len = 0  #this could be use to make the spacing between the product name and price dynamic.

print("SELECTED PRODUCTS:")
for selected_id in selected_ids:
    matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
    matching_products = matching_products[0]
    if(max_len < len(matching_products["name"])):
        max_len = len(matching_products["name"])
    print(f"{selected_id:<5}{str(matching_products['name']):<65} {str(to_usd(float(matching_products['price']))):>10}")
    # print(selected_id, " ", matching_products["name"], to_usd(int(matching_products["price"])))

    
#print(max_len) #this could be use to make the spacing between the product name and price dynamic.

subtotal = 0.0
# 3) Printing Receipt on console:
print("----------------------------------------------------------------------------------")
print(f"{'GREEN FOODS GROCERY':^80}")
print(f"{'WWW.GREEN-FOODS-GROCERY.COM':^80}")
print("----------------------------------------------------------------------------------")
current_date = datetime.datetime.now()
print("CHECKOUT AT:", current_date.strftime("%Y-%m-%d %I:%M %p"))
print("----------------------------------------------------------------------------------")
print("SELECTED PRODUCTS:")
print(f"{'ID':<5}{'Product Name':<65} {'Price':>10}")
if(len(selected_ids)>0):
    for selected_id in selected_ids:
        matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
        matching_products = matching_products[0]
        print(f"{selected_id:<5}{str(matching_products['name']):<65} {str(to_usd(float(matching_products['price']))):>10}")
        subtotal = subtotal + float(matching_products["price"])
else:
    print("0. No items entered.")
print("-----------------------------------------------------------------------------------")
print(f"SUBTOTAL:, {str(to_usd(subtotal)):>70}")
tax = calculate_tax(subtotal)
print(f"TAX (set as environment var {str(float(os.getenv('TAX_RATE'))*100)}%) {str(to_usd(tax)):>46}")
print(f"TOTAL:{str(to_usd(subtotal+tax)):>75}")
print("-----------------------------------------------------------------------------------")
print(f"{'THANKS, SEE YOU AGAIN SOON!':^80}")
print("-----------------------------------------------------------------------------------")

#Defining string object to send to the custom function store_receipt_in_file()
#.. using the same strings as above

receipt_text = f""" ----------------------------------------------------------------------------------\n
                {'GREEN FOODS GROCERY':^80}\n
                {'WWW.GREEN-FOODS-GROCERY.COM':^80}\n
                ----------------------------------------------------------------------------------\n
                CHECKOUT AT: {current_date.strftime("%Y-%m-%d %I:%M %p")}\n
                ----------------------------------------------------------------------------------\n
                SELECTED PRODUCTS:\n
                {'ID':<5}{'Product Name':<65} {'Price':>10}\n
                
                """

store_receipt_in_file(receipt_text)
