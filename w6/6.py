import csv

rows = [
    ["name", "surname", "gpa"],
    ["Marat", "Omarov", "3.5"],
    ["Marat2", "Omarov2", "2.5"],
]

with open('file.csv','w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rows)