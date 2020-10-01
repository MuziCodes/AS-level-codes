BiggestSoFar = int(input("Enter your first number "))
for count in range(2):  # change 2 to 5 if you want to find largest of 5 numbers
    NextNumber = int(input("Enter your next number "))
    if NextNumber > BiggestSoFar:
        BiggestSoFar = NextNumber
print(f'The biggest number is {BiggestSoFar}')
