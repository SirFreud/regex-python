import re


names_file = open('names.txt', encoding='utf-8')
data = names_file.read()
names_file.close()

print(re.findall(r'''
    ^([-\w ]*,\s[-\w ]+)\t # Find LastName, FirstName
    ([-\w\d.+]+@[-\w\d.]+)\t # Email
    (\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t # Phone number
    ([\w\s]+,\s[\w\s.]+)\t? # Job & company
    (@[\w\d]+)?$ # Twitter
''', data, re.X | re.MULTILINE)) # Can also do re.M
