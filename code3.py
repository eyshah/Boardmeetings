import csv

reader = csv.reader(open("boardmeetingnew.csv","r"), delimiter=",")

with open("boardmeetingnew.csv", "r") as new_nfile:
    reading = csv.DictReader(new_nfile)

    for row in reading:
        print(row["email"])