import csv

with open("C:/Users/Ayesha's laptop/Documents/Boardmeeting2.csv", "r") as csv_rfile:
    csv_reader = csv.reader(csv_rfile)

    for line in csv_rfile:
        print(line)



