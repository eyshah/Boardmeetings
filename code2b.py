# import csv moudle
import csv
# create a varible to open / store the csv file in as "a" append
appendingcsv = open("new_meetingme.csv", "a")
# time variable created to add numbers to string
time = "4:30pm"
# appendingcsv.write module to add additionl information to csv + "str" to attach numbers to whole string
appendingcsv.write("STELLA\nHARRIS\nTOM\n**have another team meeting at**"  + str(time))
# close the code after finished
appendingcsv.close()