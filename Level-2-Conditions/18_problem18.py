# Write a program to read the marks of a student and print the grade (A/B/C/D/Fail).

total_marks = 45

if total_marks >= 33:
    if total_marks >= 90:
        print("A grade")
    elif total_marks >= 70:
        print("B grade")
    elif total_marks >= 50:
        print("C grade")
    elif total_marks >= 33:
        print("D grade")
elif total_marks < 33:
    print("Fail")
else:
    print("Result not declared")
