import csv

with open("C:/Users/Ayesha's laptop/PycharmProjects/try-22/boardmeetingnew.csv", "r") as csv_rfile:
    csv_reader = csv.reader(csv_rfile)

    with open("new_meeting_csv", "w") as new_nfile:
        csv_writer = csv.writer(new_nfile, delimiter="/")

        for line in csv_reader:
            csv_writer.writerow(line)
