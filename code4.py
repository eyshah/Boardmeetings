import csv

csv_read = csv.reader(open("boardmeetingnew.csv","r"), delimiter=",")

with open("boardmeetingnew.csv", "r") as new_nfile:
    csvreading = csv.DictReader(new_nfile)

    with open("new_meetingme2.csv", "w") as newest_nfile:
        fieldnames = ["First_name", "Last_name", "email"]

        csv_writing = csv.DictWriter(newest_nfile, fieldnames=fieldnames, delimiter="\t")

        for row in csvreading:
            csv_writing.writerow(row)


