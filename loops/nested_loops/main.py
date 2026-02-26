produce = ["Tomatoes", "Lettuce"]
dairy = ["Milk", "Cheese"]

# Combine into a list called "Groceries"
groceries = [produce, dairy]
print("Groceries:")
for section in groceries:
    for item in section:
        print("Item name:", item)
    