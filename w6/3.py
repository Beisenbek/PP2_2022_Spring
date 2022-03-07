import re

file = open('rawdata.txt','r')
text = file.read()

BINPattern = r'\nБИН.*(?P<BIN>\b[0-9]+)'
SMPattern = r'\nСмена.*(?P<SM>\b[0-9]+)'

BINText = re.search(BINPattern, text).group("BIN")
SMText = re.search(SMPattern, text).group("SM")

print(BINText)
print(SMText)
