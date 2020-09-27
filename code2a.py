import csv

csvreadings = csv.reader(open("boardmeetingnew.csv", "r"), delimiter=",")

with open("new_meetingme.csv", "w") as new_nfile:
    csv_writing = csv.writer(new_nfile, delimiter="/")

    for row in csvreadings:
        csv_writing.writerow(row)
