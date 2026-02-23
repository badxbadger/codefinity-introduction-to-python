#Make grocery inventory
grocery_inventory = {
    "Milk": ("Dairy", 3.50, 8),
    "Eggs": ("Dairy", 5.50, 30),
    "Bread": ("Bakery", 2.99, 15),
    "Apples": ("Produce", 1.50, 50)
}

#Get the price of eggs
price_of_eggs = grocery_inventory["Eggs"][1]
print(price_of_eggs)
if price_of_eggs >5:
    print("Eggs are too expensive, reducing the price by $1.")

#Change the price of eggs

else:
    print("The price of Eggs is reasonable.")

#Update price of Eggs
grocery_inventory["Eggs"] = ("Dairy", 4.50, 30)
price_of_eggs = grocery_inventory["Eggs"][1]
print(price_of_eggs)

#Add tomatoes to dictionary
added_item = {"Tomatoes": ("Produce", 1.20, 30)}
grocery_inventory.update(added_item)
print("Inventory after adding Tomatoes:", grocery_inventory)

#Check the stock of Milk and stock, if needed
stock_of_milk = grocery_inventory["Milk"][2]
if stock_of_milk <10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
else:
    print("Milk has sufficient stock.")

#Add 20 units to "Milk"
grocery_inventory["Milk"] = ("Dairy", 3.50, 28)
print(grocery_inventory)

#Check price of "Apples"
apple_price = grocery_inventory["Apples"][1]
if apple_price >2:
    grocery_inventory.pop("Apples")
    print("Apples removed from inventory due to high price")

print("Updated inventory:", grocery_inventory)
