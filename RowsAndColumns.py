rows = int(input("Enter the Rows as a whole number "))
columns = int(input("Enter the columns as a whole number "))
printed_string = input("Enter the text to be repeated ")
for count in range(rows):
    print(printed_string * columns)
