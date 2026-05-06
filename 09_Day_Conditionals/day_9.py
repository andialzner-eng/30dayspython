#age = int(input("Enter your age: "))
#if age >= 18:
#    print("You are old enough to drive.")
#else:
#    print(f"You need {18 - age} more years to drive.")

#my_age = 25
#your_age = int(input("Enter your age: "))
#if my_age > your_age:
#    if my_age - your_age == 1:
#        print(f"I am {my_age - your_age} year older than you.")
#    else:        
#        print(f"I am {my_age - your_age} years older than you.")
#elif my_age < your_age:
#    if your_age - my_age == 1:
#        print(f"You are {your_age - my_age} year older than me.")
#    else:
#        print(f"You are {your_age - my_age} years older than me.")
#else:
#    print("We are the same age.")   


#a = int(input("Enter number a: "))
#b = int(input("Enter number b: "))  
#if a > b:
 #   print(f"{a} is greater than {b}.")
#elif a < b:
 #   print(f"{a} is smaller than {b}.")
#else:
#    print(f"{a} is equal to {b}.")

# score = int(input("Enter your score: "))
# if score >= 90 and score <= 100:
#     print("Your grade is A.")
# elif score >= 80 and score < 90:
#     print("Your grade is B.")
# elif score >= 70 and score < 80:
#     print("Your grade is C.")
# elif score >= 60 and score < 70:
#     print("Your grade is D.")
# elif score >= 0 and score < 60:
#     print("Your grade is F.")
# else:
#     print("Invalid score. Please enter a score between 0 and 100.")

# month = input("Enter the month: ")
# if month in ["September", "October", "November"]:
#     print("The season is Autumn.")
# elif month in ["December", "January", "February"]:
#     print("The season is Winter.")
# elif month in ["March", "April", "May"]:
#     print("The season is Spring.")
# elif month in ["June", "July", "August"]:
#     print("The season is Summer.")

# fruits = ["banana", "orange", "mango", "lemon"]
# new_fruit = input("Enter a new fruit: ")

# if new_fruit in fruits:
#     print("The fruit already exists in the list.")
# else:
#     fruits.append(new_fruit)
#     print("The fruit has been added to the list.")

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

if 'skills' in person:
    print(f"Middle skill: {person['skills'][len(person['skills'])//2]}")

if 'Python' in person['skills']:
    print("Python is a skill in the list.")

if "JavaScript" in person['skills'] and "React" in person['skills']:
    print("He is a front-end developer.")

if "Node" in person['skills'] and "MongoDB" in person['skills'] and "React" in person['skills']:
    print("He is a full-stack developer.")

else:
    print("unknown title")

if person['is_married'] and person['country'] == "Finland":
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.") 

    



