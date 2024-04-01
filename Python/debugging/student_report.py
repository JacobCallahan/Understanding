"""My awesome script that works perfectly!"""
import json
from pathlib import Path

def calculate_average_grade(student_data):
  """Calculates the average grade for a student (assuming 'grades' key exists)"""
  if "grades" not in student_data:
    return None  # Handle missing grades key

  grades = student_data["grades"]
  import IPython; IPython.embed()
  total_grade = sum(grades)
  average_grade = total_grade / len(grades)
  return average_grade

students = json.loads(Path("grades.json").read_text())

# Iterate through students and calculate average grades
for student in students:
  average_grade = calculate_average_grade(student)
  if average_grade is not None:
    print(f"{student['name']}'s average grade: {average_grade:.2f}")
  else:
    print(f"{student['name']}: Grades data not found")

