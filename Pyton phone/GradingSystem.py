print("\n\n\n\t\t\t\t\t\t\t\t\tGrading System for University")

print("\nThis program is supposed to collect student information and marks and then to print corresponding grades")
print("\n\t\t\t\t\t\t\t\t\t\tCreated by Henry\n")

year = input("Enter Year: ")
if year == "first":
    name = input("Enter Student Name: ")
    roll_no = input("Enter Roll No: ")
    myanmar = input("Enter Myanmar mark: ")
    english = input("Enter English mark: ")
    math = input("Enter Math mark: ")
    physics = input("Enter Physics mark: ")
    chemistry = input("Enter Chemistry mark: ")
    major = input("Enter IT mark: ")

    marks = [myanmar, english, math, physics, chemistry, major]
    grades_name = ["myanmar", "english", "mathamatic", "physics", "chemistry", "major_IT"]
    grades = [0,1,2,3,4,5]

    for i in range(0, 6, 1):
        mark = marks[i]
        mark = int(mark)
        if 80 < mark <= 100:
            grades[i] = 'A'
        elif 60 < mark <= 80:
            grades[i] = 'B'
        elif 40 < mark <= 60:
            grades[i] = 'C'
        elif 20 < mark <= 40:
            grades[i] = 'D'
        else:
            grades[i] = 'E'
        i+=1

    print("\n\n\nStudent Name: "+ name)
    print("Roll number: "+ roll_no)
    print("Grades:")
    for i in range(0, 6, 1):
        print(grades_name[i] +" \t " + grades[i])

    print("\n\nThat's all for one student")
