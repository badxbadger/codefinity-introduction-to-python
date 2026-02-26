prices = [29.99, 45.50, 12.75, 38.20] # Product prices

discount_factor = (0.10, 0.20, 0.15, 0.05) #Discount rates for the Products

#for _____ in _____()
for cost in range(len(prices)):
    #Apply the different discounts using the range(len()) function
    prices[cost] -= prices[cost] * discount_factor[cost]
    print(f"Updated price for item {cost}: ${prices[cost]:.2f}")