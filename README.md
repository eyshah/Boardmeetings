 # Project brief Task 4 PARSE / VISUALIZE IN PYTHON A CSV FILE

Using Pycharm an IDE for python, which is a high-tech programming language, allowing users to programme on both smaller and larger scales. The project iam working on is task 4 where I will be modifying and manipulating my own CSV file in various iffrent ways by creating diffrent codes. An csv text file stands for Comma separated value where each line in the file contains data. Within my organisation I will be having a small meeting, hence why I have imputed some information of my workers within my csv file, so wwith this file i will be creating codes which each of the code will excecute a diffrent task. So for example a code to to add additional information to the file, known as "Appending" the file, create codes to extract certain data, write the same file changing the delimeter making the dat within the file readble to the ye and the code will demonstate a way user can change the way data is stored in a csv. Overall my project will ensure that the fundamentals of handiling a CSV file using python and pycharm comes through.

  # Requirments / Programs needed to be preinstalled

* Latest version of python 3 / https://www.python.org/downloads/

* Pycharm IDE / https://www.jetbrains.com/pycharm/download/#section=windows

# Codes and CSV file can be found in my Github Respository.

	
# CODE 1 = HOW TO OPEN / READ A CSV FILE

![code1](https://user-images.githubusercontent.com/69476214/96037297-8e796580-0e5d-11eb-8614-246e9e8e89b8.PNG)

"Run- Excecute selction in python console"

By applying this code within python allowed it to open and read your csv file.

 
 # CODE 2A WRITE THE SAME CSV FILE CHANGING THE DILIMITER.

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

![code4](https://user-images.githubusercontent.com/69476214/96038640-4eb37d80-0e5f-11eb-84bf-a9d95d55b9b8.PNG)

""Run - Excecute selction in python console""

""DictWriter funtion works is succesfull if fieldnames parameters is accurate."



# CODE 5 - If & break statement to exit loop

![code5](https://user-images.githubusercontent.com/69476214/96038809-9f2adb00-0e5f-11eb-9038-9733e78ed740.PNG)

""Run - excecute selection in python console""


# Imports the csv module
import csv

# opens the csv file to "r" read function
with open("C:/Users/Ayesha's laptop/PycharmProjects/try-22/boardmeetingnew.csv","r") as csv_rfile:

    # Variable created to store the file in
    to_extract = csv.reader(csv_rfile)

    # final command will print the rows as an output from the "csv_rfile"
    for row in csv_rfile:
        print(row)
