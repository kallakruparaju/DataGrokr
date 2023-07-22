original_list = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
seen = set()
new_list = []

for item in original_list:
    if item not in seen:
        seen.add(item)
        new_list.append(item)

print(new_list)
