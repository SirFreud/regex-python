import re


names_file = open("names.txt", encoding="utf-8")
data = names_file.read()
names_file.close()

# If you're matching at the beginning of a string, use 're.match'
# print(re.match(r'Love', data))
# If you're matching a string somewhere in the middle, use 're.search'
# print(re.search(r'Kenneth', data))

# I can also use regex to set string variables, like this:
last_name = r'Love'
first_name = r'Kenneth'
print(re.match(last_name, data))
print(re.search(first_name, data))
