import re


names_file = open('names.txt', encoding='utf-8')
data = names_file.read()
names_file.close()

line = re.search(r'''
    ^(?P<name>[-\w ]*,\s[-\w ]+)\t # Find LastName, FirstName
    (?P<email>[-\w\d.+]+@[-\w\d.]+)\t # Email
    (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t # Phone number
    (?P<job>[\w\s]+,\s[\w\s.]+)\t? # Job & company
    (?P<twitter>@[\w\d]+)?$ # Twitter
''', data, re.X | re.MULTILINE) # Can also do re.M

print(line)
print(line.groupdict())
