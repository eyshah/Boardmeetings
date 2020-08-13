import csv

csv_reader= csv.reader(open("boardmeetingnew.csv","r"), delimiter=",")

with open("new_meetingme_csv", "w") as new_nfile:
     csv_writer = csv.writer(new_nfile, delimiter="/")

     for line in csv_reader:
        csv_writer.writerow(line)

