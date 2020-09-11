# Author: Bakhtiar Reza bmr5782@psu.edu
# Collaborator:


def getGradePoint(L):
  if(L == "A"):
    return 4.0
  elif(L == "A-"):
    return 3.67
  elif(L == "B+"):
    return 3.33
  elif(L == "B"):
    return 3.0
  elif(L == "B-"):
    return 2.67
  elif(L == "C+"):
    return 2.33
  elif(L == "C"):
    return 2.0
  elif(L == "D"):
    return 1.0
  else:
    return 0.0

if __name__ == "__main__":
  course1letter = input("Enter your course 1 letter grade: ")
  course1letter = getGradePoint(course1letter)
  course1credit = input("Enter your course 1 credit: ")
  course1credit = float(course1credit)
  print(f"Grade point for course 1 is: {course1letter}")
  course2letter = input("Enter your course 2 letter grade: ")
  course2letter = getGradePoint(course2letter)
  course2credit = input("Enter your course 2 credit: ")
  course2credit = float(course2credit)
  print(f"Grade point for course 2 is: {course2letter}")
  course3letter = input("Enter your course 3 letter grade: ")
  course3letter = getGradePoint(course3letter)
  course3credit = input("Enter your course 3 credit: ")
  course3credit = float(course3credit)
  print(f"Grade point for course 3 is: {course3letter}")

  print(f"Your GPA is: {((course1letter*course1credit)+(course2letter*course2credit)+(course3letter*course3credit))/(course1credit+course2credit+course3credit)}")