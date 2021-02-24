import csv
from random import *
import string
import re as re

voca = {
	"schwedisch" : [],
	"deutsch": [],
	"chapter": [],
	"checkword": [],
	"erfolg": []
}

def checkword(str):
	a = str
	#check, if string has brackets and split string after first brackets
	if a.find(")") >= 0:
		m = re.search(r"\(.*\)", str)
		a = a[:m.start()] + str[m.end():]
	#delete all unnecessairy spaces
	a = a.replace("  ", " ")
	a = a.rstrip()
	#replace sonderzeichen
	a = a.replace("å", "a")
	a = a.replace("å", "a")
	return (a)


chapters = []


prev_chapter = ""
with open('Kap1bis5.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=",")
	for row in csv_reader:
		#test if row is a new chapter and if yes, ignore it, bc its the title of the chapter
		if row[2] == prev_chapter:
			if row[1][1] != "_":
				voca["schwedisch"].append(row[0])
				voca["deutsch"].append(row[1])
				voca["chapter"].append(row[2])
				voca["erfolg"].append(0)
				voca["checkword"].append(checkword(row[0]))
		else:
			chapters.append(row[2])
		prev_chapter = row[2]

#save the dict as csv row by row
with open('voci_dict.csv', 'w') as voci_dict:
	writer = csv.DictWriter(voci_dict, fieldnames=voca.keys())
	writer.writeheader()
	i = 0
	while i < len(voca["schwedisch"]):
		row = {
			"schwedisch" : voca["schwedisch"][i], 
			"deutsch" : voca["deutsch"][i], 
			"chapter" : voca["chapter"][i], 
			"checkword" : voca["checkword"][i], 
			"erfolg" : voca["erfolg"][i] 
		}
		writer.writerow(row)
		i += 1



#	for values in voca:
#		for data in values:
#			print(values)
#			writer.writerow(data)
#		print(data[0])


