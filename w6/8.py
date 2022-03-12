import re

text = "abbb"
pattern = "ab{2,3}"

r = re.search(pattern, text)

if(r != None):
    print('match')
else:
    print("not match")

