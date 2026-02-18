# Current inventory on shelf
shelf = ("apples", "oranges", "bananas", "apples", "grapes", "bananas", "apples")

#apples
apple_count = shelf.count("apples")
print("Number of Apples:", apple_count)

#bananas
banana_index = shelf.index("bananas")
print("First Banana Index:", banana_index)

#Apple Restock
if apple_count <5:
  print("Apples need to be restocked.")
else:
  print("Apples are sufficiently stocked.")

#Grapes
grape_count = shelf.count("grapes")
if grape_count <= 1:
  print("Grapes need to be restocked.")
else:
  print("Grapes are sufficiently stocked.")

#Oranges
orange_index = shelf.index("oranges")
if orange_index not in shelf:
  print("Oranges are at index:", orange_index)
else:
  print("Oranges are out of stock.")