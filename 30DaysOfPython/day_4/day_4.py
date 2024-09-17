string_1 = 'Thirty ' + 'Days ' + 'Of ' + 'Python'

string_2 = 'Coding ' + 'For ' + 'All'

company = 'Coding For All'

print(company)

print('Length =', len(company))

print(company.upper())

print(company.lower())

print(company.capitalize())
print(company.title())
print(company.swapcase())

print(company[7:])

print(company.find('Coding'))

print(company.replace('Coding', 'Python'))

phrase = "Python for Everyone"
print(phrase.replace('Everyone', 'All'))

print(company.split())

companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(', '))

print(company[0])
print(len(company) - 1)
print(company[10])

phrase_1 = "Python For Everyone"
acronym_1 = ''.join([word[0] for word in phrase_1.split()])
print(acronym_1)

phrase_2 = "Coding For All"
acronym_2 = ''.join([word[0] for word in phrase_2.split()])
print(acronym_2)

print(company.index('C'))

print(company.index('F'))

company_people = "Coding For All People"
print(company_people.rfind('l'))

sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))

print(sentence.rindex('because'))

start = sentence.find('because')
end = sentence.rfind('because') + len('because')
print(sentence[start:end])

print(company.startswith('Coding'))

print(company.endswith('coding'))

padded_string = '   Coding For All      '
print(padded_string.strip())

print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(python_libraries))

print("I am enjoying this challenge.\nI just wonder what is next.")

print("Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")

radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")

a, b = 8, 6
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")