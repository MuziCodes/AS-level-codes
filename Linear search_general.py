size = int(input("How large is your list? "))
List = []
print("Enter the numbers in the list, one by one, ")
for i in range(size):
    new_value = int(input("Enter here: "))
    List.append(new_value)
count = -1
found = False
search_term = int(input("Enter the value you want to search "))
for i in range(size):
    count += 1
    if List[count] == search_term:
        found = True
if found:
    print(f'Found at {count+1}')
else:
    print("Not found")
