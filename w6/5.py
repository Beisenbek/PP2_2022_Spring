import re

file = open('rawdata.txt','r')
text = file.read()

BINPattern = r'\nБИН.*(?P<BIN>\b[0-9]+)'
SMPattern = r'\nСмена.*(?P<SM>\b[0-9]+)'

BINText = re.search(BINPattern, text).group("BIN")
SMText = re.search(SMPattern, text).group("SM")

ItemPatternText = r'(?P<Name>.*)\n{1}(?P<Count>.*)x(?P<Price>.*)\n{1}(?P<Total1>.*)\n{1}Стоимость\n{1}(?P<Total2>.*)'
ItemPattern = re.compile(ItemPatternText)

for m in re.finditer(ItemPattern, text):
    ItemText1 = m.group("Name")
    ItemText2 = m.group("Count")
    ItemText3 = m.group("Price")
    ItemText4 = m.group("Total1")
    print(ItemText1.strip())
    print(ItemText2.strip())
    print(ItemText3.strip())
    print(ItemText4.strip())
    print("==========================")