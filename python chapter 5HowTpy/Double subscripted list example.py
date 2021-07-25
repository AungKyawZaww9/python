def printgrades(grades):
    students = len(grades)
    exams = len(grades[0])

    print("The list is")
    print(" ")

    for i in range(exams):
        print("[%d]" % i)

    for i in range(students):
        print("grades[%d] " % i)
        for j in range(exams):
            print( grades[i][j] )

def minimum(grades):
    lowscore = 100
    for studentexams in grades:
        for score in studentexams:
            if score < lowscore:
                lowscore = score
        return lowscore

def maximum(grades):
    highscore = 0
    for studentexams in grades:
        for score in studentexams:
            if score > highscore:
                highscore = score
        return highscore

def average(setofgrades):
    total = 0.0
    for grade in setofgrades:
        total += grade
    return total / len(setofgrades)

grades = [  [ 77, 68, 86, 73 ],
            [ 96, 87, 89, 81 ],
            [ 70, 90, 86, 81 ] ]
printgrades(grades)
print("\n\nLowest grade: ", minimum(grades))
print("\nHighest grade: ", maximum(grades))

for i in range(len(grades)):
    print("Average for student", i, "is", average(grades[i]))