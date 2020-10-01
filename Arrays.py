name = []
gender = []
marks = []
for arrays in range(4):
    new_name = str(input("Please enter your name "))
    new_gender = str(input("Please enter your gender "))
    new_marks = int(input("Please enter your marks "))
    name.append(new_name)
    gender.append(new_gender)
    marks.append(new_marks)
for count in range(4):
    print("Your name is " + name[count])
    print("Your gender is " + gender[count])
    print("Your marks is " + str(marks[count]))
