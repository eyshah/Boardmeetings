 CSV FILE Task 4 project brief.

  # PARSE / VISUALIZE IN PYTHON A CSV FILE

Using python, a high-tech programming language, allowing users to programme on both smaller and larger scales. I have created my own csv file which I will then be modifying and analysing within this language program, with the help of another program known as PyCharm, which is an integrated environment platform used to run codes within python.

  
  # CSV FILE
  
An csv text file stands for Comma separated value where each line in the file contains data , though within the file at the start each value is separated by a comma later on within python, Within my organisation I will be having individual meetings, hence why I have imputed some emails within my csv file, however to add additional information and parse I will create a python script and commands. 


  # Requirments / Programs needed to be preinstalled

* Latest version of python 3 / https://www.python.org/downloads/

* Pycharm IDE / https://www.jetbrains.com/pycharm/download/#section=windows



	
# CODE 1 = HOW TO OPEN / READ A CSV FILE

![code1](https://user-images.githubusercontent.com/69476214/96037297-8e796580-0e5d-11eb-8614-246e9e8e89b8.PNG)

"Run- Excecute selction in python console"

By applying this code within python allowed it to open and read your csv file.

 
 # CODE 2A WRITE THE SAME CSV FILE CHANGING THE DILIMITER

![code2a](https://user-images.githubusercontent.com/69476214/96037814-38f18880-0e5e-11eb-9a30-04b0d03fca17.PNG)
 
 "Run - excecute selction in python console"
 
 This code 2 I have written in python allows to separate the data within the csv file by a different delimiter.
 
 
 # CODE2b = HOW TO APPEND YOUR CSV FILE
 
 ![code2b](https://user-images.githubusercontent.com/69476214/96038313-dbaa0700-0e5e-11eb-8b9a-b0a11fe3603e.PNG)

 ""Run - excecute in python selction""
 
 

 # CODE 3 - USING DICTREADER FUNCTION TO EXTRACT INFORMATION
 
![code3](https://user-images.githubusercontent.com/69476214/96038473-1744d100-0e5f-11eb-8972-66366b71b073.PNG)

""Run - excecute in python selction""

Within this code the DictReader function works as a python dictionary where it reads the first line and using the comma separted values within your files separtes columns and prints out everything that comes under that coloum. Your outcome can be changed according to what information you would want to be extrcated. just remember to use the special keys and first line as the reference to ensure ths code works properly.



# Code 4 – Extract information using DictWriter

# imports the csv module
import csv

csv_read = csv.reader(open("boardmeetingnew.csv","r"), delimiter=",")

# Currently using the Dictreader funtion for new file.
with open("boardmeetingnew.csv", "r") as new_nfile:
    csvreading = csv.DictReader(new_nfile)

    # Opening and writing a new csv file using "w" python function
    with open("new_meetingme2.csv", "w") as newest_nfile:
        # pass in fieldnames first line of csv for the order of values in the dictionary.
        fieldnames = ["First_name", "Last_name", "email"]

        """
        Dictwriter method to pass in new file being written two 
        along side with fieldnames and new chosen delimeiter.
        """
        csv_writing = csv.DictWriter(newest_nfile, fieldnames=fieldnames, delimiter="\t")
        for row in csvreading:
            csv_writing.writerow(row)

""Run - Excecute selction in python console""

""DictWriter funtion works is succesfull if fieldnames parameters is accurate."



# CODE 5 - If & break statement to exit loop

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


""Run - excecute selection in python console""
