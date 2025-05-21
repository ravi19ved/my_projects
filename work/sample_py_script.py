# student_scores.py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def calculate_average(scores):
    total = 0
    for i in range(len(scores)):
        total += scores[i]
    average = total / len(scores)
    return average

def get_highest_score(score_list):
    highest = 0
    for score in score_list:
        if score > highest:
            highest = score
    return highest

def print_student_summary(student_scores):
    for student in student_scores:
        name = student['name']
        scores = student['scores']
        avg = calculate_average(scores)
        high = get_highest_score(scores)
        print("Student:", name)
        print("Average Score: ", avg)
        print("Highest Score: ", high)
        print("------")

students = [
    {'name': 'Alice', 'scores': [88, 92, 79]},
    {'name': 'Bob', 'scores': [90, 85, 80]},  # Notice the string here!
    {'name': 'Charlie', 'scores': [88, 86, 82]}  # No scores!
]

print_student_summary(students)