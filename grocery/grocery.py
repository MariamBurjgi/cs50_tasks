from collections import Counter

grocery_list = []
while True:
    try:
        item = input().strip().title()
        grocery_list.append(item)
    except EOFError:
        break

# count the items and sort them alphabetically
item_counts = Counter(grocery_list)
sorted_items = sorted(item_counts.items(), key=lambda x: x[0])

# output the grocery list
for item, count in sorted_items:
    print(f"{count} {item.upper()}")

