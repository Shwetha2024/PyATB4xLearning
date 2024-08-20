#Grade Calculator:
# Write a program that calculates and displays the letter grade
# for a given numerical score (e.g., A, B, C, D, or F)
# based on the following grading scale:
#
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59

score = int(input("Enter the score secured\n"))
print(score)
if (90 <= score < 100):
    print("Your grade is A")
elif score >= 80 and score <= 89:
    grade = 'B'
    print("Your grade is", grade)
elif 70 <= score <= 79:
    grade = 'C'
    print("Your grade is", grade)
elif 60 <= score <= 69:
    grade = 'D'
    print("Your grade is", grade)
elif score >= 50 and score <= 59:
    grade = 'E'
    print("Your grade is", grade)
elif score >=100:
    grade = 'Topper'
    print("Your grade is", grade)
else:
    grade = 'F'
    print("Your grade is", grade)
