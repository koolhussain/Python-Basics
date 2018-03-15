import csv

with open('Ambulatory Surgical Measures-Facility.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    
    all_center = []
    
    for row in readCSV:
        center = row[0]

        all_center.append(center)

print(all_center)
