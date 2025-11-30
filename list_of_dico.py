students = [
    {"name": "Taye", "School": "UI", "dept": "CSC"},
    {"name": "Kenny", "School": "Lautech", "dept": "BCH"},
    {"name": "idowu", "School": "OAU", "dept": "MTH"},


]
# print(students[1]["dept"])
for std in students:
    print(f"my name is {std["name"]} studying {std["dept"]} at {std["School"]}")
# del students[0]
# print(students)
students[1]["School"] = "Uniosun"
print(students) 