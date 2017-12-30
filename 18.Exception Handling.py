import csv

with  open('exampleCSV.txt') as CSVfile:
    readCSV = csv.reader(CSVfile, delimiter=',')

    dates = []
    colors = []
    
    for row in readCSV:
        color = row[3]
        date = row[0]

        dates.append(date)
        colors.append(color)

    print(dates)
    print(colors)

    try:
        whatcolor = input('What color you wanna wish to know?')
        coldex = colors.index(whatcolor.lower())

        theDate = dates[coldex]

        print('the date of',whatcolor,'is',theDate)

    except Exception as e:
        print(e)

    print('continue')
        
        
