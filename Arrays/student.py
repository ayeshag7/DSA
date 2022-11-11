"""
Problem Statement:

Using numpy, create an array to store roll-number and marks of four students for
three different. Then write functions for each of the following tasks:
a. Roll number of the students who scored highest marks in each subject?
b. In which subject each student got highest marks?
c. Roll number of the students who scored lowest marks in each subject?
d. In which subject each student got lowest marks?
e. Average marks of each student.
f. Roll number of the student who has highest average?
g. Roll number of the student who has lowest average?
h. Roll number and total marks of each student.

"""



import numpy as np


def create_scoreboard():
    scoreboard = np.array([[None, None, None, None],
                          [None, None, None, None],
                          [None, None, None, None],
                          [None, None, None, None]])
    i = 0
    while i < 4:
        try:
            roll_no = int(input("Enter student's roll no: "))
            scoreboard[i][0] = roll_no
            i += 1
        except ValueError:
            print("Invalid Input. Try again!")
            roll_no = int(input("Enter student's roll no: "))
            scoreboard[i][0] = roll_no
            i += 1

    print(" ")

    j = 0
    k = 1
    s = 1
    while j < 4:
        try:
            score = int(input(f"Enter marks for student {j+1} for subject {s}: "))
        except ValueError:
            print("Invalid Input. Try again!")
            score = int(input(f"Enter marks for student {j + 1} for subject {s}: "))
        scoreboard[j][k] = score
        k += 1
        s += 1
        if k > 3:
            j += 1
            k = 1
            s = 1
            print(" ")
            continue

    return scoreboard


# Subject in which each student got the highest marks.
def highest_scored_subject(scoreboard):
    for i in scoreboard:
        highest = i[1]
        subject = 1
        for j in range(2, len(i)):
            if i[j] > highest:
                highest = i[j]
                subject = j
        print(f"Roll No {i[0]} got highest mark in subject {subject}.")


# Roll number of the students who scored the highest marks in each subject.
def highest_scorer_in_each_subject(scoreboard):
    for i in range(1, len(scoreboard[0])):
        highest = 0
        roll_no = None
        for j in range(0, len(scoreboard)):
            if scoreboard[j][i] > highest:
                highest = scoreboard[j][i]
                roll_no = scoreboard[j][0]
        print(f"Roll No. {roll_no} scored highest in subject {i}")


# Subject in which each student got the lowest marks.
def lowest_scored_subject(scoreboard):
    for i in scoreboard:
        lowest = i[1]
        subject = 1
        for j in range(2, len(i)):
            if i[j] < lowest:
                lowest = i[j]
                subject = j
        print(f"Roll No {i[0]} got lowest mark in subject {subject}.")


# Roll number of the students who scored the lowest marks in each subject.
def lowest_scorer_in_each_subject(scoreboard):
    for i in range(1, len(scoreboard[0])):
        lowest = scoreboard[0][i]
        roll_no = scoreboard[0][0]
        for j in range(0, len(scoreboard)):
            if scoreboard[j][i] < lowest:
                lowest = scoreboard[j][i]
                roll_no = scoreboard[j][0]
        print(f"Roll No. {roll_no} scored lowest in subject {i}")


# Average marks of each student.
def average_marks(scoreboard):
    for i in scoreboard:
        average_sum = 0
        for j in range(1, len(i)):
            average_sum += i[j]
        print(f"Roll No {i[0]}'s average: {average_sum/3}")


# Roll number of the student who has the highest average.
def highest_average(scoreboard):
    roll_no = None
    highest = 0
    for i in scoreboard:
        average_sum = 0
        for j in range(1, len(i)):
            average_sum += i[j]
        if average_sum/3 > highest:
            highest = average_sum/3
            roll_no = i[0]
    return roll_no


# Roll number of the student who has the lowest average.
def lowest_average(scoreboard):
    roll_no = None
    lowest = sum(scoreboard[0][1:])
    for i in scoreboard:
        average_sum = 0
        for j in range(2, len(i)):
            average_sum += i[j]
        if average_sum/3 < lowest:
            lowest = average_sum/3
            roll_no = i[0]
    return roll_no


# Roll number and total marks of each student.
def total_marks(scoreboard):
    for i in scoreboard:
        student_total = 0
        for j in range(1, len(i)):
            student_total += i[j]
        print(f"Roll No: {i[0]}, Total: {student_total}")


arr = create_scoreboard()
print(arr)
print(" ")
