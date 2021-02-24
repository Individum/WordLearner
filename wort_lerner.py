import csv
from random import *

voca = {
	"schwedisch" : [],
	"deutsch": [],
	"chapter": [],
	"checkword": [],
	"erfolg": []
}


#Get in list of chapters
chapters = []
def chapters_in():
	prev_chapter = ""
	with open('voci_dict.csv') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=",")
		for row in csv_reader:
			#test if row is a new chapter and if yes, ignore it, bc its the title of the chapter
			if row[2] != prev_chapter:
				chapters.append(row[2])
			prev_chapter = row[2]

#load chosen chapter into dictionary
def fill_in_dict():
	print("welches Kapitel willst du lernen?", "\n", chapters)
	chap_to_learn = input()

	prev_chapter = ""
	with open('voci_dict.csv') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=",")
		for row in csv_reader:
			#test if row is a new chapter and if yes, ignore it, bc its the title of the chapter
			if row[2] == prev_chapter and row[2] == chap_to_learn:
				if row[1][1] != "_":
					voca["schwedisch"].append(row[0])
					voca["deutsch"].append(row[1])
					voca["chapter"].append(row[2])
					voca["erfolg"].append(int(row[4]))
					voca["checkword"].append(row[3])
			else:
				chapters.append(row[2])
			prev_chapter = row[2]

m = [1,2,3,4]
def tester():
#choose randomly a word out of the Chapter and ask what its in swedisch
	for i in m:#voca["schwedisch"]: 

		wort = randint(0, (len(voca["schwedisch"])-1))
		deutsch = voca["deutsch"][wort]
		checkword = voca["checkword"][wort]
		schwedisch = voca["schwedisch"][wort]

		if voca["erfolg"][wort] < 3:
			print(deutsch)
			if input() == checkword :
				print(schwedisch, "\t korrekt", "\n")
				voca["erfolg"][wort] += 3
			else:
				print(schwedisch, "\t falsch", "\n")
				if voca["erfolg"][wort] != 0: 
					voca["erfolg"][wort] -= 1
		else:
			voca["erfolg"][wort] -= 1
		print(voca["erfolg"][wort])

def score_saver():
	with open('voci_dict.csv') as inf:
		reader = csv.reader(inf.readlines())

	with open('voci_dict.csv', 'w') as voci_dict:
		writer = csv.DictWriter(voci_dict, fieldnames=voca.keys())
		i = 0
		while i < len(voca["schwedisch"]):
			row = [
				voca["schwedisch"][i], 
				voca["deutsch"][i], 
				voca["chapter"][i], 
				voca["checkword"][i], 
				voca["erfolg"][i] 
			]
			for line in reader:

				print(line[0])
				print(row[0])

				if line[0] == row[0]:
					writer.writerow([line[4]], row[4])
				else:
					writer.writerow(line)
			i += 1

chapters_in()
fill_in_dict()
tester()
score_saver()


print(voca)









