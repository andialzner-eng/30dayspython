print("Thrity" + " " + "Days" + " " + "Of" + " " + "Python")
print("Coding" + " " + "For" + " " + "All")

company = "Coding For All"
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company[0:6])
print("Coding" in company)
print(company.replace("Coding", "Python"))
print("Coding for everyone".replace("Coding", "Python"))
print("Python for all".replace("all", "everyone"))
print(company.split()) 
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(","))
print(company[0])
print(company[10])
print("python for everyone"[0] + "python for everyone"[7] + "python for everyone"[11])
print(company.find("C"))
print(company.find("F"))
print(company.rfind("l"))

sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.find("because"))
print(sentence.rfind("because"))
print(sentence[sentence.find("because"):sentence.rfind("because") + len("because")])
substring = "Coding"
print(company.index(substring))
print(company.rindex(substring))
print(company.strip(" "))
print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier())

libraries = ["Django", "Flask", "Bottle", "Pyramid", "Falcon"]
print("#".join(libraries))
print("""I am enjoying this challenge.\nI just wonder what is next.""")
print("Name\t\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")

radius = 10
area = 3.14 * radius ** 2
print("radius = {}".format(radius))
print("area = {:.2f}".format(area))
print("The area of a circle with radius {} is {} meters square.".format(radius, int(area)))

a = 8
b = 6

print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')