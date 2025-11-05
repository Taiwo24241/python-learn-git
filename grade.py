# Grading system
print("TMO grading system")
def std_grade(score, total):
       grade = (score / total * 100)
       if grade >= 70:
               grade = "A"
       elif grade >= 60:
               grade = "B"
       elif grade >= 50:
               grade = "C"
       elif grade >= 45:
               grade = "D"
       elif grade >= 40:
               grade = "E"
       else: grade = "F" 
       return(f"You scored {score} out of {total} which is grade {grade}")

print(std_grade(20, 100))
print(std_grade(60, 120))
print(std_grade(40, 100))




