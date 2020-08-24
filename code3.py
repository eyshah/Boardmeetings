import csv

csv_reader= csv.reader(open("boardmeetingnew.csv","r"), delimiter=",")

with open("boardmeetingnew.csv", "r") as new_nfile:
    csv_reader = csv.DictReader(new_nfile)

    for row in csv_reader:
        print(row["email"])

