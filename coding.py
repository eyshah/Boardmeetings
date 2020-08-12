import csv

with open ("C:/Users/Ayesha's laptop/PycharmProjects/try-22/boardmeetingnew.csv","r") as csv_rfile:
    csv_reader = csv.reader(csv_rfile)

    for line in csv_rfile:
        print(line)