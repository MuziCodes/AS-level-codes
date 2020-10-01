search_value = int(input("Enter search value "))
found = False
values = [1, 2, 3, 4, 5, 6]
count = -1
index = 0
for i in range(6):
    count += 1
    if values[count] == search_value:
        found = True
        index = count
if found:
    print(f"Value found at location {index+1}")
else:
    print("Not found")
