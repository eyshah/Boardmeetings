# Imports the csv module
import csv

# opens the csv file to "r" read function
with open("C:/Users/Ayesha's laptop/PycharmProjects/try-22/boardmeetingnew.csv","r") as csv_rfile:

    # Variable created to store the file in
    to_extract = csv.reader(csv_rfile)

    # final command will print the rows as an output from the "csv_rfile"
    for row in csv_rfile:
        print(row)
