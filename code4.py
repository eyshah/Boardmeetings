import csv

csv_reader = csv.reader(open("boardmeetingnew.csv","r"), delimiter=",")

with open("boardmeetingnew.csv", "r") as new_nfile:
    csv_reader = csv.DictReader(new_nfile)

    with open("new_meetingme2_csv", "w") as newest_nfile:
        fieldnames =["First_name", "Last_name", "email"]

        csv_writer = csv.DictWriter(newest_nfile, fieldnames=fieldnames, delimiter="\t")

        for row in csv_reader:
            csv_writer.writerow(row)
