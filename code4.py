# imports the csv module
import csv

csv_read = csv.reader(open("boardmeetingnew.csv","r"), delimiter=",")

# Currently using the Dictreader funtion for new file.
with open("boardmeetingnew.csv", "r") as new_nfile:
    csvreading = csv.DictReader(new_nfile)

    # Opening and writing a new csv file using "w" python function
    with open("new_meetingme2.csv", "w") as newest_nfile:
        # pass in fieldnames first line of csv for the order of values in the dictionary.
        fieldnames = ["Salary", "Age", "First_name", "Last_name", "email"]

        """
        Dictwriter method to pass in new file being written two 
        along side with fieldnames and new chosen delimeiter.
        """
        csv_writing = csv.DictWriter(newest_nfile, fieldnames=fieldnames, delimiter="\t")
        for row in csvreading:
            csv_writing.writerow(row)


