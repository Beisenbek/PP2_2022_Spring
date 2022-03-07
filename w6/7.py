import re
import csv

file = open('rawdata.txt','r')
text = file.read()

BINPattern = r'\nБИН.*(?P<BIN>\b[0-9]+)'
SMPattern = r'\nСмена.*(?P<SM>\b[0-9]+)'

BINText = re.search(BINPattern, text).group("BIN")
SMText = re.search(SMPattern, text).group("SM")

ItemPatternText = r'(?P<Name>.*)\n{1}(?P<Count>.*)x(?P<Price>.*)\n{1}(?P<Total1>.*)\n{1}Стоимость\n{1}(?P<Total2>.*)'
ItemPattern = re.compile(ItemPatternText)

rows = [["Name","Count", "Price", "Total1"]]

for m in re.finditer(ItemPattern, text):
    rows.append([m.group("Name"),m.group("Count"),m.group("Price"),m.group("Total1")])

with open('data.csv','w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rows)