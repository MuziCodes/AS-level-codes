loop = 3
NextNumber = 0
Biggest = int(input("Enter the first number "))
while loop != 1:
    NextNumber = int(input("Enter the next number "))
    if NextNumber > Biggest:
        Biggest = NextNumber
    loop -= 1
print(f"The largest number among the three is {Biggest}")
