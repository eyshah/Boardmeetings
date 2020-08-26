import csv

with open("boardmeetingnew.csv", "r") as new:
    reader = csv.reader(new)

    email = 0

    for line in reader:
        print(line)

        if email > 5:
            break

        email += 1
