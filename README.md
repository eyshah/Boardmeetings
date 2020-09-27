 CSV FILE Task 4 project brief.

  __PARSE / VISUALIZE IN PYTHON A CSV FILE__

Using python, a high-tech programming language, allowing users to programme on both smaller and larger scales. I have created my own csv file which I will then be modifying and analysing within this language program, with the help of another program known as PyCharm, which is an integrated environment platform used to run codes within python.

  
  __CSV FILE__
  
An csv text file stands for Comma separated value where each line in the file contains data , though within the file at the start each value is separated by a comma later on within python, Within my organisation I will be having individual meetings, hence why I have imputed some emails within my csv file, however to add additional information and parse I will create a python script and commands. 


  __Requirments / Programs needed to be preinstalled__

* Latest version of python 3 / https://www.python.org/downloads/

* Pycharm IDE / https://www.jetbrains.com/pycharm/download/#section=windows



	
__CODE 1 = HOW TO OPEN / READ A CSV FILE__

 __Code sturcture__

import csv "installs the csv function"

with open("File location / File name", "r") as "create a file name"
    variable = csv.reader(create a file name")

    for row in "create a file name"
       print(row)


  __In Python__ 

import csv

with open("C:/Users/Ayesha's laptop/PycharmProjects/try-22/boardmeetingnew.csv", "r") as csv_rfile:
    to_extract = csv.reader(csv_rfile)

    for row in csv_rfile:
        print(row)
 

"Run- Excecute selction in python console"

By applying this code within python allowed it to open and read your csv file.

 


__CODE 2A WRITE THE SAME CSV FILE CHANGING THE DILIMITER__
 
 __Code structure__

Import csv

csvreadings = csv.reader(open(“enter the original file location” , “r”) delimiter= “original delimiter”
	
with open(“enter new files name”, “w”) create new files variable name:
          csv_writing = csv.writerow(enter variable, delimiter=“chose new delimiter”) 

	for row in (csvreadings)
	 csv_writing.writerow(row)


__In Python__

import csv

csvreadings= csv.reader(open("boardmeetingnew.csv","r"), delimiter=",")

with open("new_meetingme_csv", "w") as new_nfile:
     csv_writing = csv.writer(new_nfile, delimiter="/")

     for row in csvreadings:
        csv_writings.writerow(row)
 
 
 "Run - excecute selction in python console"
 
 This code 2 I have written in python allows to separate the data within the csv file by a different delimiter.
 
 
 __CODE2b-- HOW TO APPEND YOUR CSV FILE__
 
 __Code Structure__
 
 import csv
 
 Variable1 = open("required file name", "a") **"a" open files in append mode**
 variable2 = **store a float number**
 variable1.write("Write your text required" \n+str(variable2) **\n** will start the new line 
 variable.close()
 
 
 __In python__
 
 import csv
 
 appendingcsv = open("new_meetingme.csv", "a")
 time= "4:30"
 appendingcsv.write("STELLA\nHARRIS\nTOM\n**Have another meeting at** +str(time))
 appending.close()
 
 
 ""Run - excecute in python selction""
 
 
 
 __CODE 3 - USING DICTREADER FUNCTION TO EXTRACT INFORMATION__
 
 
 __In Python__
 
 import csv

reader= csv.reader(open("boardmeetingnew.csv","r"), delimiter=",")

with open("boardmeetingnew.csv", "r") as new_nfile:
    reading = csv.DictReader(new_nfile)

    for row in reading:
        print(row["email"])
	

""Run - excecute in python selction""

Within this code the DictReader function works as a python dictionary where it reads the first line and using the comma separted values within your files separtes columns and prints out everything that comes under that coloum. Your outcome can be changed according to what information you would want to be extrcated. just remember to use the special keys and first line as the reference to ensure ths code works properly.



__Code 4 – Extract information using DictWriter__


__Code structure__

Import csv 

Csv_read = csv.reader(open(“enter your csv file name” “r”) delimiter “ enter the current delimiter”

With open(“enter your csv file name, “r”) as “enter you knew file variable name”
	csvreading = csv.DictReader( “Enter the variable)

With open (“enter a name for you new csv file”, “w”) as “new file variable”
	Fieldnames = “ insert the fieldnames of your file- fist line within the file)

        Csv_writing = csv.Dictwriter( Enter new files name, fieldnames=fieldnames, delimter= “enter your new delimiter to separate your data”)

	for row in csvreading:
	       csv_writing.writerow(row)
	       
	       
__In Python__


import csv

csv_read = csv.reader(open("boardmeetingnew.csv","r"), delimiter=",")

with open("boardmeetingnew.csv", "r") as new_nfile:
    csvreading = csv.DictReader(new_nfile)

    with open("new_meetingme2_csv", "w") as newest_nfile:
        fieldnames =["First_name", "Last_name", "email"]

        csv_writing = csv.DictWriter(newest_nfile, fieldnames=fieldnames, delimiter="\t")

        for row in csvreading:
            csv_writing.writerow(row)
	    

""Run - Excecute selction in python console""

""DictWriter funtion works is succesfull if fieldnames parameters is accurate."



__CODE 5 - If & break statement to exit loop__

 __Code Structure__
 
 
 Import csv 

with open(“ Enter the files name”) as “create a variable name”
	reader_variable = csv.reader(“enter the files variable name”)

	“Create a variable code before statement” 
	EG; email = 0

	for line in reader_variable:
	print(line)

             if “enter the variable code” > enter a code digit E.g. 5
                  break
		
	    email +=  enter a digit new E.g. 1
	    
	    
	    

__In Python__


import csv

with open("boardmeetingnew.csv") as emails_info:
    reader_variable = csv.reader(emails_info)

    email = 0

    for line in reader_variable:
        print(line)

        if email > 5:
            break

        email += 1


""Run - excecute selection in python console""
