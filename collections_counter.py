from collections import Counter

#shoe inventory 

total_shoe_count = int(input())
shoe_inventory = input().split()

shoe_inventory_dict = Counter(shoe_inventory)


total_customers = int(input())

total_revenue = 0

for i in range(1, total_customers+1) :
    req_size, paid_price = input().split()

    if shoe_inventory_dict[req_size] > 0:
        shoe_inventory_dict[req_size] = shoe_inventory_dict[req_size] - 1
        total_revenue += int(paid_price)

print(total_revenue)
