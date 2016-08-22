import re


names_file = open('names.txt')
data = names_file.read()
names_file.close()

# print(re.findall(r'[-\w\d+.]+@[-\w\d.]+', data))
# print(re.findall(r'\b[trehous]{9}\b', data, re.I))
# I am now going to try and leave '.gov' off of any emails
# Find a word boundary, an @, and then any  of chars
# print(re.findall(r'''
#     \b@[-\w\d.]*
#     [^govt\t]+
#     \b
# ''', data, re.VERBOSE | re.IGNORECASE))

print(re.findall(r'''
    \b[-\w]*, # Find a word boundary, 1+ hyphens or characters, and a comma
    \s # Find 1 whitespace
    [-\w ]+ # 1+ hyphens characters and explicit spaces
    [^\t\n] # Ignore tabs and newlines
''', data, re.VERBOSE)) # re.X is the shorthand for VERBOSE
# re.VERBOSE ignores all spaces within our regex string