dog = {}
dog = {"name": "Buddy", "color": "brown", "breed": "Golden Retriever", "age": 5} 
print(dog)

student = {"first name": "Andi", "last name": "Garcia", "gender": "Male", "age": 25, "marital status": "Single", "skills": ["Python", "JavaScript"], "country": "Spain", "city": "Madrid", "address": "123 Main Street"}
print(student)
print(len(student))

skills = student["skills"]
print(skills)
print(type(skills))

student["skills"].append("HTML")
print(student["skills"])

print(student.keys())
print(student.values())
print(student.items())
del student["marital status"]
print(student)

del student


