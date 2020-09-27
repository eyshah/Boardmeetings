import csv

with open("boardmeetingnew.csv", "r") as emails_info:
    reader_variable = csv.reader(emails_info)

    email = 0

    for line in reader_variable:
        print(line)

        if email > 5:
            break

        email += 1
