<<<<<<< HEAD
lst = list()
lst = [1, 2, 3, 4, 5]
len_lst = len(lst)
first_item = lst[0]
middle_item = lst[len_lst // 2]
last_item = lst[-1]
mixed_data_types = ["Andi", 34, 1.67, "married", "Reiherweg 1", "Germany"]
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies)
print(len(it_companies))
it_companies[0] = "Meta"
print(it_companies)
print(it_companies[0], it_companies[-1], it_companies[len(it_companies) // 2])
=======
it_companies = ["Google", "Apple", "Facebook", "Amazon", "Microsoft"]
print(", ".join(it_companies))
print("Google" in it_companies)

it_companies.sort()
print(it_companies)

it_companies.reverse()
print(it_companies)
print(it_companies[0:3])
print(it_companies[-1:-4:-1])
print(it_companies[len(it_companies) // 2])

it_companies.remove(it_companies[0])
it_companies.pop()
it_companies.pop(len(it_companies) // 2)
print(it_companies)

it_companies.clear()
print(it_companies)

del it_companies

front_end = ["HTML", "CSS", "JS", "React", "Redux"]
back_end = ["Node", "Express", "MongoDB"]
full_stack = front_end + back_end
print(full_stack)

full_stack.insert(5, "Python")
full_stack.insert(6, "SQL")
print(full_stack)

age = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
age.sort()
print(age)
print("Min age:", min(age))
print("Max age:", max(age))  
print("Median age:", sum(age) / len(age))
print("Range of ages:", max(age) - min(age))
deviation_min = abs(min(age) - sum(age) / len(age))
print("Deviation from min age:", deviation_min)
deviation_max = abs(max(age) - sum(age) / len(age))
print("Deviation from max age:", deviation_max)

countries = ["China", "Russia", "USA", "Finland", "Sweden", "Norway", "Denmark"]

countries_part_1 = countries[:len(countries) // 2]
countries_part_2 = countries[len(countries) // 2:]
print("Countries Part 1:", countries_part_1)
print("Countries Part 2:", countries_part_2)    

cn, ru, us, *baltics = countries
print("CN:", cn)
print("RU:", ru)
print("US:", us)
print("Baltic Countries:", baltics)



>>>>>>> f36f3e7 (Tag 5 fertig)

