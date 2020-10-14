# imports the required csv module
import csv

# input csv file to r function into a variable / input the delimited used in csv file
csvreadings = csv.reader(open("boardmeetingnew.csv", "r"), delimiter=",")

# writing "w" a new csv file with with a new name
with open("new_meetingme.csv", "w") as new_nfile:

    # adding the new delimiter to new file with csv.writer function
    csv_writing = csv.writer(new_nfile, delimiter="/")

    # write out all rows from original file csvreadings into new file with writerow(row)module
    for row in csvreadings:
        csv_writing.writerow(row)
