# Grading system
print("TMO grading system")
def std_grade(score, total):
       grade = (score / total * 100)
       if score >= 70:
               grade = "A"
       elif score >= 60:
               grade = "B"
       elif score >= 50:
               grade = "C"
       elif score >= 45:
               grade = "D"
       elif score >= 40:
               grade = "E"
       else: grade = "F" 
       return(f"You scored {score} out of {total} which is grade {grade}")

print(std_grade(20, 100))
print(std_grade(60, 120))
print(std_grade(40, 100))




