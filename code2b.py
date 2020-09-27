import csv

appendingcsv = open("new_meetingme.csv", "a")
time = "4:30pm"
appendingcsv.write("STELLA\nHARRIS\nTOM\n**have another team meating at**"  + str(time))
appendingcsv.close()
