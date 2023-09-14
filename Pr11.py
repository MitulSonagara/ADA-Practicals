def fractional_knapsack(items, capacity):
    for item in items:
        item['ratio'] = item['value'] / item['weight']

    items.sort(key=lambda x: x['ratio'], reverse=True)

    total_value = 0
    knapsack = []

    for item in items:
        if capacity >= item['weight']:
            total_value += item['value']
            capacity -= item['weight']
            knapsack.append({'item': item['item'], 'weight': item['weight'], 'percentage': 100})
        else:
            fraction = capacity / item['weight']
            total_value += fraction * item['value']
            knapsack.append({'item': item['item'], 'weight': fraction * item['weight'], 'percentage': fraction * 100})
            break

    return total_value, knapsack

# Input the number of items and capacity
num_items = int(input("Enter the number of items: "))
capacity = float(input("Enter the capacity of the knapsack: "))

# Input item details from the user
items = []
for i in range(1, num_items + 1):
    item_name = f'Item {i}'  # Changed item1 to item 1
    item_weight = float(input(f"Enter weight of {item_name}: "))
    item_value = float(input(f"Enter value of {item_name}: "))
    items.append({'item': item_name, 'weight': item_weight, 'value': item_value})

total_value, knapsack = fractional_knapsack(items, capacity)

print("\nItems in knapsack:")
for item in knapsack:
    print(f"{item['item']} - Weight: {item['weight']} ({item['percentage']}%)")

print("Remaining knapsack capacity:", capacity)
print("Total value:", total_value)