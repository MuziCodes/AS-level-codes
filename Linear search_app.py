names = ["Muzammil", "Ibrahim", "", "Fredrick", "Zaytoon", "Ali"]
age = [17, 7, 34, 17, 10, 17]
search_name = str(input("What name do you want to search? "))
count = -1
found = False
index = 0
for i in range(6):
    count += 1
    if names[count] == search_name:
        found = True
        index = count
if found:
    print(f"Age: {age[index]}")
else:
    print("Name not found")