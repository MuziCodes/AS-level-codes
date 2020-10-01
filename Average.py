total = 0
value = 0
count = int(input("Enter the amount of numbers "))
for loop in range(count):
    value = int(input("Enter a value "))
    total += value
average = total / value
print(f"The average of {count} values is {average}")
