import re

text = "123abc"
pattern = "^\d+[a-z]*$"


r = re.search(pattern, text)

if(r != None):
    print(r.start())
else:
    print("not found!")

