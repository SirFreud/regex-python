import re


names_file = open('names.txt')
data = names_file.read()
names_file.close()

print(re.findall(r'\w*, \w+', data))
print(re.findall(r'\(?\d{3}\)?-?\s?\d{3}-?\d{4}', data))
