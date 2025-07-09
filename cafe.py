# List of all the items on the café menu
menu = ["coffee", "tea", "sandwich", "cake"]

# Stock that is available for each item
stock = {
    "coffee": 20,
    "tea": 15,
    "sandwich": 10,
    "cake": 5
}

# Price for each of the items
price = {
    "coffee": 3.0,
    "tea": 2.5,
    "sandwich": 4.5,
    "cake": 3.5
}

# Calculate the total worth of the stock
total_stock = 0

for item in menu:
    item_value = stock[item] * price[item]
    total_stock += item_value

# Print the result
print("Total stock worth in the café: $", total_stock)