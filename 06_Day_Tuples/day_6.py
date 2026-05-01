empty_tpl = ()
brothers = ("John", "Michael", "David")
sisters = ("Sarah", "Emily", "Jessica")
siblings = brothers + sisters
print(siblings)
print(len(siblings))

family_members = siblings + ("Mom", "Dad")
print(family_members)

siblings = family_members[0:6]
print(siblings)
parents = family_members[6:8]
print(parents)

fruits = ("apple", "banana", "cherry")
vegetables = ("carrot", "broccoli", "spinach")
animal_products = ("milk", "cheese", "yogurt")
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)
food_stuff_lt = list(food_stuff_tp)
food_stuff_lt.pop(len(food_stuff_lt) // 2)
print(food_stuff_lt)

food_stuff_lt = food_stuff_lt[3:-3]
print(food_stuff_lt)
del food_stuff_lt

nordic_countries = ("Denmark", "Finland", "Iceland", "Norway", "Sweden")
print(nordic_countries)
print(f"Estonia is a nordic country: {'Estonia' in nordic_countries}")
print(f"Iceland is a nordic country: {'Iceland' in nordic_countries}")


