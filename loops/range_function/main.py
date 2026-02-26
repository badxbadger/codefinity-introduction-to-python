# List of products on promotion for each weekday
daily_promotions = ["Milk", "Eggs", "Bread", "Apples", "Oranges"]

# List of weekdays corresponding to the promotions
weekdays = ["monday", "tuesday", "wednesday", "thursday", "friday"]

#range(start, stop, step)

for day in range(5):
    promotion = daily_promotions[day]  # Access the promotion that corresponds to a weekday
    weekday = weekdays[day] # Access the corresponding weekday 
    print(f"{weekday}: promotion on {promotion}")