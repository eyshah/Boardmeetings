# Boardmeetings - CSV FILE Task 4

  __PARSE / VISUALIZE IN PYTHON A CSV FILE__

Using python, a high-tech programming language, allowing users to programme on both smaller and larger scales. I have created my own csv file which I will then be modifying and analysing within this language program, with the help of another program known as PyCharm, which is an integrated environment platform used to run codes within python.

  __CSV FILE__
  
An csv text file stands for Comma separated value where each line in the file contains data , though within the file at the start each value is separated by a comma later on within python, Within my organisation I will be having individual meetings, hence why I have imputed some emails within my csv file, however to add additional information and parse I will create a python script and commands. 


  __Requirments / Programs needed to be preinstalled__

* Latest version of python 3 / https://www.python.org/downloads/

* Pycharm IDE / https://www.jetbrains.com/pycharm/download/#section=windows



__Code 1 = HOW TO OPEN / READ A CSV FILE__

 __Code sturcture__

import csv "installs the csv function"

with open("File location / File name", "r") as "create a file name"
    csv_reader = csv.reader(create a file name")

    for line in create a file name"
       print(line)


  __In practice__ 

import csv

with open("C:/Users/Ayesha's laptop/PycharmProjects/try-22/boardmeetingnew.csv", "r") as csv_rfile:
    csv_reader = csv.reader(csv_rfile)

    for line in csv_rfile:
        print(line)
 
"Run- Excecute selction in python console"

By applying this code within python allowed it to open and read your csv file.

 


__CODE 2 WRITE HE SAME CSV FILE CHANGING THE DILIMITER__
 
 __Code structure__
 *Code 1 minus line 4-5. Following on with code 2*

Import csv

with open("File location / File name", "r") as “Create a file name”:
    csv_reader = csv.reader(file name)
	       for line in csv_reader

with open(“enter new files name”, “w”) create new files variable name:
      csv_writer = csv.writerow(enter variable, delimiter=“chose new delimiter”) 
      
      for line in (csv_reader)
      csv_writer.writerow(line)


__In practice__

import csv

csv_reader= csv.reader(open("boardmeetingnew.csv","r"), delimiter=",")

with open("new_meetingme_csv", "w") as new_nfile:
     csv_writer = csv.writer(new_nfile, delimiter="/")

     for line in csv_reader:
        csv_writer.writerow(line)
 
 "Run - excecute selction in python console"
 
 This code 2 I have written in python allows to separate the data within the csv file by a different delimiter.
 
 
 
 
 **CODE 3 - USING DICTREADER TO EXTRACT INFORMATION**
 
 
 __In practice__
 
 import csv

csv_reader= csv.reader(open("boardmeetingnew.csv","r"), delimiter=",")

with open("boardmeetingnew.csv", "r") as new_nfile:
    csv_reader = csv.DictReader(new_nfile)

    for line in csv_reader:
        print(line["email"])
	
""Run - excecute in python selction""


This dictreader code works a s aython dictionary hwhere it reads the first line and using the comma separted values within your files sepatrehte colums and print out everything that come sout under that coloum. Your outcome can be changed according to what infromation you would want to be extrcated. just remember to use the special keys and first line as the reference to ensure ths code works properly.
