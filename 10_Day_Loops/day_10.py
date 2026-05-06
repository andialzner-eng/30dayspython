# for i in range(1,11):
#     print(i)

# for i in range(10,0,-1):
#     print(i)   

# for i in range(1,8,1):
#     print(f"{i * "#"}")


# for i in range(1,8,1):
#     for j in range(4 ,8,1):
#         print(8 * "# ")

# for i in range(1,11,1):
#     print(f"{i} x {i} = {i * i}")

# list = ["Python", "Numpy", "Pandas", "Django", "Flask"]
# for i in list:
#     print(i)

# for i in range(0,101,2):
#     print(i)

# for i in range(1,101,2):
#     if i % 2 != 0:
#         print(i)

# sum = 0
# for i in range(1,101,1):
#     sum += i
# print(f"The sum of all numbers is {sum}")


# sum_even = 0
# sum_odd = 0

# for i in range(1,101,1):
#     if i % 2 == 0:
#         sum_even += i
#     else:
#         sum_odd += i
# print(f"The sum of all even numbers is {sum_even}.")
# print(f"The sum of all odd numbers is {sum_odd}.")

# fruit_list = ["banana", "orange", "mango", "lemon"]

# for i in range(len(fruit_list) -1, -1, -1):
#     print(fruit_list[i])


from countries_data import countries_data

languages = []
for country in countries_data:
    for language in country['languages']:
        if language not in languages:
            languages.append(language)
print(languages)

language_counts = {}

for country in countries_data:
    for language in country['languages']:
        if language in language_counts:
            language_counts[language] += 1
        else:
            language_counts[language] = 1

sorted_languages = sorted(language_counts.items(), key=lambda item: item[1], reverse=True)

print('Ten most spoken languages:')
print(sorted_languages[:10])

sorted_countries = sorted(countries_data, key=lambda country: country['population'], reverse=True)
print('Ten most populated countries:')
for country in sorted_countries[:10]:
    print(f"{country['name']}: {country['population']}")
    