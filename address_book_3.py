import re


names_file = open('names.txt', encoding='utf-8')
data = names_file.read()
names_file.close()

line = re.compile(r'''
    ^(?P<name>(?P<last>[-\w ]*),\s(?P<first>[-\w ]+))\t # Find LastName, FirstName
    (?P<email>[-\w\d.+]+@[-\w\d.]+)\t # Email
    (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t # Phone number
    (?P<job>[\w\s]+,\s[\w\s.]+)\t? # Job & company
    (?P<twitter>@[\w\d]+)?$ # Twitter
''', re.X | re.MULTILINE)  # Can also do re.M

# print(line)
print(re.search(line, data).groupdict())
print(line.search(data).groupdict())

for match in line.finditer(data):
    print('{first} {last} <{email}>'.format(**match.groupdict()))