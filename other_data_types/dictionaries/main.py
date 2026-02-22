grocery_inventory = {
    "Milk":   (113, "Dairy"),
    "Eggs":   (116, "Dairy"),
    "Bread":  (117, "Bakery"),
    "Apples": (114, "Produce"),
}

#Retrieve "Bread" from dictionary and make bread_details

bread_details = grocery_inventory["Bread"]
print("Details of Bread:", bread_details)

#Add Cookies
grocery_inventory["Cookies"] = (143, "Bakery")
print("Inventory after adding Cookies:", grocery_inventory)

#Remove Eggs
grocery_inventory.pop("Eggs")
print("Inventory after removing Eggs:", grocery_inventory)
