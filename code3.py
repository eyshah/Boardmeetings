# imports the csv module
import csv

# reader variable created to open/read csv file hence the "r" included the delimiter in file
reader = csv.reader(open("boardmeetingnew.csv","r"), delimiter=",")

# Dictreader funtion treats csv as a object remembering the keys.
with open("boardmeetingnew.csv", "r") as new_nfile:
    reading = csv.DictReader(new_nfile)

    # for row in original file prints out only the emails"
    for row in reading:
        print(row["email"])