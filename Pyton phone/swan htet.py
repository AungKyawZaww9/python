# title
title = "|| Grading System for Universities ||"
title_length = len(title) + 30
new_length = title.rjust(title_length)
print(new_length)

# subtitle
subtitle = "< WELCOME TO GRADE.iT >"
subtitle_length = len(subtitle) + 37
new_length = subtitle.rjust(subtitle_length)
print(new_length)

# subtitle 2
subtitle2 = "(Swan's Creation)"
subtitle2_length = len(subtitle2) + 78
new_length = subtitle2.rjust(subtitle2_length)
print(new_length)

# major selection box
print("\nSELECT from the following...\n [1] Electronics and Communication\n [2] Information Technology\n ")

major = ['0', '1', '2']

major = input("Select Major: ")  # Display Major Input

# For First major
while major == '1':  # User Inputs 1

    if major == '1':

        years = ['0', '1', '2', '6']

        year = input("Input Year\n(EXIT CODE is 0)  : ")  # Display Year Input


        def main():

            while years == '1' or '2' or '6':

                if year == "1" or year == "First":

                    name = input("Enter Student Name: ")
                    roll_no = input("Input Roll No: ")
                    sub1 = int(input("Input [Myanmar] mark: "))
                    sub2 = int(input("Input [English] mark: "))
                    sub3 = int(input("Input [Maths] mark: "))  # FOR THESIS CHANGE TO STR. THESIS REMARKS
                    sub4 = int(
                        input("Input [Chemistry] mark: "))  # and for calculation, only print two lines and avg. of two
                    sub5 = int(input("Input [Physics] mark: "))
                    sub6 = int(input("Input [subject_name] mark: "))

                    marks = [sub1, sub2, sub3, sub4, sub5, sub6]

                    def calcAvg(sub1, sub2, sub3, sub4, sub5, sub6):
                        average = (sub1 + sub2 + sub3 + sub4 + sub5 + sub6) / 6  # for Thesis, change to 2
                        return average

                    def grade(mark):
                        if mark < 20:
                            return "E"
                        elif 20 <= mark < 40:
                            return "D"
                        elif 40 <= mark < 60:
                            return "C"
                        elif 60 <= mark < 80:
                            return "B"
                        elif 80 <= mark <= 100:
                            return "A"

                    print("\n\t- DATA COLLECTION DONE -\n\nGENERATING RESULT.... \n")  # output msg 1
                    print("\n\nStudent Name: " + name)
                    print("Roll number: " + roll_no)
                    print("\nMarks\tGrade")
                    print(str(sub1) + "\t\t  " + grade(sub1),
                          str(sub2) + "\t\t  " + grade(sub2),
                          str(sub3) + "\t\t  " + grade(sub3),
                          str(sub4) + "\t\t  " + grade(sub4),
                          str(sub5) + "\t\t  " + grade(sub5),
                          str(sub6) + "\t\t  " + grade(sub6), sep="\n")
                    print("\nAverage Grade is", grade(calcAvg(sub1, sub2, sub3, sub4, sub5, sub6)))

                    if grade(calcAvg(sub1, sub2, sub3, sub4, sub5, sub6)) == "A":
                        print("-- EXCELLENT! --")
                    elif grade(calcAvg(sub1, sub2, sub3, sub4, sub5, sub6)) == "B":
                        print("-- OK --")
                    elif grade(calcAvg(sub1, sub2, sub3, sub4, sub5, sub6)) == "C":
                        print("-- PASS --")
                    elif grade(calcAvg(sub1, sub2, sub3, sub4, sub5, sub6)) == "D":
                        print("-- DON'T NEGLECT YOUR STUDIES LAH! --")

                    print("\n *** THANK YOU FOR USING GRADE.iT! ***\n\n")


                elif year == "2" or year == "Second":

                    name = input("Enter Student Name: ")
                    roll_no = input("Input Roll No: ")
                    sub1 = int(input("Input [Myanmar] mark: "))
                    sub2 = int(input("Input [English] mark: "))
                    sub3 = int(input("Input [Subject_name] mark: "))  # FOR THESIS CHANGE TO STR. THESIS REMARKS
                    sub4 = int(input( "Input[Subject_name] mark: "))    # change calc. to only two
                    sub5 = int(input("Input [Subject_name]: "))
                    sub6 = int(input("Input [subject_name] mark: "))

                    marks = [sub1, sub2, sub3, sub4, sub5, sub6]

                    def calcAvg(sub1, sub2, sub3, sub4, sub5, sub6):
                        average = (sub1 + sub2 + sub3 + sub4 + sub5 + sub6) / 6  # for Thesis, change to 2
                        return average

                    def grade(mark):
                        if mark < 20:
                            return "E"
                        elif 20 <= mark < 40:
                            return "D"
                        elif 40 <= mark < 60:
                            return "C"
                        elif 60 <= mark < 80:
                            return "B"
                        elif 80 <= mark <= 100:
                            return "A"

                    print("\n\t- DATA COLLECTION DONE -\n\nGENERATING RESULT.... \n")  # output msg 1
                    print("\n\nStudent Name: " + name)
                    print("Roll number: " + roll_no)
                    print("\nMarks\tGrade")

                    print(str(sub1) + "\t\t  " + grade(sub1),
                          str(sub2) + "\t\t  " + grade(sub2),
                          str(sub3) + "\t\t  " + grade(sub3),
                          str(sub4) + "\t\t  " + grade(sub4),
                          str(sub5) + "\t\t  " + grade(sub5),
                          str(sub6) + "\t\t  " + grade(sub6), sep="\n")

                    print("\nAverage Grade is", grade(calcAvg(sub1, sub2, sub3, sub4, sub5, sub6)))

                    if grade(calcAvg(sub1, sub2, sub3, sub4, sub5, sub6)) == "A":
                        print("-- EXCELLENT! --")
                    elif grade(calcAvg(sub1, sub2, sub3, sub4, sub5, sub6)) == "B":
                        print("-- OK --")
                    elif grade(calcAvg(sub1, sub2, sub3, sub4, sub5, sub6)) == "C":
                        print("-- PASS --")
                    elif grade(calcAvg(sub1, sub2, sub3, sub4, sub5, sub6)) == "D":
                        print("-- DON'T NEGLECT YOUR STUDIES LAH! --")

                    print("\n *** THANK YOU FOR USING GRADE.iT! ***\n\n")



                elif year == "6" or year == "Final":

                    name = input("Enter Student Name: ")
                    roll_no = input("Input Roll No: ")
                    sub1 = int(input("Input [Subject_name] mark: "))
                    sub2 = int(input("Input [Subject_name] mark: "))
                    sub3 = str(input("Input [THESIS] Remark: ")) + "\n"  # FOR THESIS CHANGE TO STR. THESIS REMARKS

                    marks = [sub1, sub2, sub3]

                    def calcAvg(sub1, sub2):
                        average = (sub1 + sub2) / 2  # for Thesis, change to 2
                        return average

                    def grade(mark):
                        if mark < 20:
                            return "E"
                        elif 20 <= mark < 40:
                            return "D"
                        elif 40 <= mark < 60:
                            return "C"
                        elif 60 <= mark < 80:
                            return "B"
                        elif 80 <= mark <= 100:
                            return "A"

                    print("\n\t- DATA COLLECTION DONE -\n\nGENERATING RESULT.... \n")  # output msg 1
                    print("\n\nStudent Name: " + name)
                    print("Roll number: " + roll_no)
                    print("\nMarks\tGrade")
                    print(str(sub1) + "\t\t  " + grade(sub1),
                          str(sub2) + "\t\t  " + grade(sub2),
                          "\nRemark:\n\t\t" + str(sub3), sep="\n")

                    print("\nAverage Grade is", grade(calcAvg(sub1, sub2)))

                    if grade(calcAvg(sub1, sub2)) == "A":
                        print("-- EXCELLENT! --")
                    elif grade(calcAvg(sub1, sub2)) == "B":
                        print("-- OK --")
                    elif grade(calcAvg(sub1, sub2)) == "C":
                        print("-- PASS --")
                    elif grade(calcAvg(sub1, sub2)) == "D":
                        print("-- DON'T NEGLECT YOUR STUDIES LAH! --")

                    print("\n *** THANK YOU FOR USING GRADE.iT! ***\n\n")

                elif year > "6":
                    print("\n(ERROR OCCURRED >>> PLEASE TYPE AGAIN)\n")
                break


        try:
            if year == '0':
                print("\n>> END OF PROGRAMME <<\n(SEE YOU AGAIN, 再见!!!)")
                break
        except:
            year = input('HEADACHE')

        main()
# for Second Major
while major == '2':
    if major == '2':

        years = ['0', '1', '2', '6']

        year = input("Input Year\n(EXIT CODE is 0)  : ")  # Display Year Input


        def main():

            while years == '1' or '2' or '6':

                if year == "1" or year == "First":

                    name = input("Enter Student Name: ")
                    roll_no = input("Input Roll No: ")
                    sub1 = int(input("Input [Myanmar] mark: "))
                    sub2 = int(input("Input [English] mark: "))
                    sub3 = int(input("Input [Maths] mark: "))
                    sub4 = int(input("Input [Chemistry] mark: "))
                    sub5 = int(input("Input [Physics] mark: "))
                    sub6 = int(input("Input [subject_name] mark: "))

                    marks = [sub1, sub2, sub3, sub4, sub5, sub6]

                    def calcAvg(sub1, sub2, sub3, sub4, sub5, sub6):
                        average = (sub1 + sub2 + sub3 + sub4 + sub5 + sub6) / 6  # for Thesis, change to 2
                        return average

                    def grade(mark):
                        if mark < 20:
                            return "E"
                        elif 20 <= mark < 40:
                            return "D"
                        elif 40 <= mark < 60:
                            return "C"
                        elif 60 <= mark < 80:
                            return "B"
                        elif 80 <= mark <= 100:
                            return "A"

                    print("\n\t- DATA COLLECTION DONE -\n\nGENERATING RESULT.... \n")  # output msg 1
                    print("\n\nStudent Name: " + name)
                    print("Roll number: " + roll_no)
                    print("\nMarks\tGrade")
                    print(str(sub1) + "\t\t  " + grade(sub1),
                          str(sub2) + "\t\t  " + grade(sub2),
                          str(sub3) + "\t\t  " + grade(sub3),
                          str(sub4) + "\t\t  " + grade(sub4),
                          str(sub5) + "\t\t  " + grade(sub5),
                          str(sub6) + "\t\t  " + grade(sub6), sep="\n")
                    print("\nAverage Grade is", grade(calcAvg(sub1, sub2, sub3, sub4, sub5, sub6)))

                    if grade(calcAvg(sub1, sub2, sub3, sub4, sub5, sub6)) == "A":
                        print("-- EXCELLENT! --")
                    elif grade(calcAvg(sub1, sub2, sub3, sub4, sub5, sub6)) == "B":
                        print("-- OK --")
                    elif grade(calcAvg(sub1, sub2, sub3, sub4, sub5, sub6)) == "C":
                        print("-- PASS --")
                    elif grade(calcAvg(sub1, sub2, sub3, sub4, sub5, sub6)) == "D":
                        print("-- DON'T NEGLECT YOUR STUDIES LAH! --")

                    print("\n *** THANK YOU FOR USING GRADE.iT! ***\n\n")


                elif year == "2" or year == "Second":

                    name = input("Enter Student Name: ")
                    roll_no = input("Input Roll No: ")
                    sub1 = int(input("Input [Myanmar] mark: "))
                    sub2 = int(input("Input [English] mark: "))
                    sub3 = int(input("Input [Subject_name] mark: "))
                    sub4 = int(input("Input[Subject_name] mark: "))
                    sub5 = int(input("Input [Subject_name]: "))
                    sub6 = int(input("Input [subject_name] mark: "))

                    marks = [sub1, sub2, sub3, sub4, sub5, sub6]

                    def calcAvg(sub1, sub2, sub3, sub4, sub5, sub6):
                        average = (sub1 + sub2 + sub3 + sub4 + sub5 + sub6) / 6  # for Thesis, change to 2
                        return average

                    def grade(mark):
                        if mark < 20:
                            return "E"
                        elif 20 <= mark < 40:
                            return "D"
                        elif 40 <= mark < 60:
                            return "C"
                        elif 60 <= mark < 80:
                            return "B"
                        elif 80 <= mark <= 100:
                            return "A"

                    print("\n\t- DATA COLLECTION DONE -\n\nGENERATING RESULT.... \n")  # output msg 1
                    print("\n\nStudent Name: " + name)
                    print("Roll number: " + roll_no)
                    print("\nMarks\tGrade")

                    print(str(sub1) + "\t\t  " + grade(sub1),
                          str(sub2) + "\t\t  " + grade(sub2),
                          str(sub3) + "\t\t  " + grade(sub3),
                          str(sub4) + "\t\t  " + grade(sub4),
                          str(sub5) + "\t\t  " + grade(sub5),
                          str(sub6) + "\t\t  " + grade(sub6), sep="\n")

                    print("\nAverage Grade is", grade(calcAvg(sub1, sub2, sub3, sub4, sub5, sub6)))

                    if grade(calcAvg(sub1, sub2, sub3, sub4, sub5, sub6)) == "A":
                        print("-- EXCELLENT! --")
                    elif grade(calcAvg(sub1, sub2, sub3, sub4, sub5, sub6)) == "B":
                        print("-- OK --")
                    elif grade(calcAvg(sub1, sub2, sub3, sub4, sub5, sub6)) == "C":
                        print("-- PASS --")
                    elif grade(calcAvg(sub1, sub2, sub3, sub4, sub5, sub6)) == "D":
                        print("-- DON'T NEGLECT YOUR STUDIES LAH! --")

                    print("\n *** THANK YOU FOR USING GRADE.iT! ***\n\n")



                elif year == "6" or year == "Final":

                    name = input("Enter Student Name: ")
                    roll_no = input("Input Roll No: ")
                    sub1 = int(input("Input [Subject_name] mark: "))
                    sub2 = int(input("Input [Subject_name] mark: "))
                    sub3 = str(input("Input [THESIS] Remark: ")) + "\n"  # FOR THESIS CHANGE TO STR. THESIS REMARKS

                    marks = [sub1, sub2, sub3]

                    def calcAvg(sub1, sub2):
                        average = (sub1 + sub2) / 2  # for Thesis, change to 2
                        return average

                    def grade(mark):
                        if mark < 20:
                            return "E"
                        elif 20 <= mark < 40:
                            return "D"
                        elif 40 <= mark < 60:
                            return "C"
                        elif 60 <= mark < 80:
                            return "B"
                        elif 80 <= mark <= 100:
                            return "A"

                    print("\n\t- DATA COLLECTION DONE -\n\nGENERATING RESULT.... \n")  # output msg 1
                    print("\n\nStudent Name: " + name)
                    print("Roll number: " + roll_no)
                    print("\nMarks\tGrade")
                    print(str(sub1) + "\t\t  " + grade(sub1),
                          str(sub2) + "\t\t  " + grade(sub2),
                          "\nRemark:\n\t\t" + str(sub3), sep="\n")
                    # seperate because () does not allow more than 80 chars

                    print("\nAverage Grade is", grade(calcAvg(sub1, sub2)))

                    if grade(calcAvg(sub1, sub2)) == "A":
                        print("-- EXCELLENT! --")
                    elif grade(calcAvg(sub1, sub2)) == "B":
                        print("-- OK --")
                    elif grade(calcAvg(sub1, sub2)) == "C":
                        print("-- PASS --")
                    elif grade(calcAvg(sub1, sub2)) == "D":
                        print("-- DON'T NEGLECT YOUR STUDIES LAH! --")

                    print("\n *** THANK YOU FOR USING GRADE.iT! ***\n\n")

                elif year > "6":
                    print("\n(ERROR OCCURRED >>> PLEASE TYPE AGAIN)\n")
                break


        try:
            if year == '0':
                print("\n>> END OF PROGRAMME <<\n(SEE YOU AGAIN, 再见!!!)")
                break
        except:
            year = input('HEADACHE')

        main()