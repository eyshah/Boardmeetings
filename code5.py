# imports the csv module
import csv
# created a reader_variable for the opened up csv file
with open("boardmeetingnew.csv", "r") as emails_info:
    reader_variable = csv.reader(emails_info)

    # created a variable email giving number "0" as csv file has many rows
    email = 0

    for line in reader_variable:
        print(line)

        """
        if & break statement - if email "varaible" bigger than 5 braek 
        or self loop and add 1 each time to varaible 
        until it gets bigger than 5 and then break stop the loop.
        """
        if email > 5:
            break

        email += 1
