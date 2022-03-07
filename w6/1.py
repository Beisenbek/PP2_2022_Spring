import re

text = "1abc"
pattern = "^[0-9]+[a-z]*$"

r = re.search(pattern, text)

if(r != None):
    print(r.start())
else:
    print("not found!")

