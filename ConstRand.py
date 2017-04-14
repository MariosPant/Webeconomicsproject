import csv
import random
import pandas
data2 = pandas.read_csv("test.csv")
constant = 271
with open('validation.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	with open('ConstRand.csv', 'wb') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
		
		iterator =0
		row = spamreader.next()
		
		row.append("Const")
		row.append("Rand")
		row.append("Views")
		spamwriter.writerow(row)
		#spamwriter.writerow(["Const"]+["Rand"])
		#s = "{:6} ,{:.7f}".format(constant,ra)
		spent=0
		for row in spamreader:
			print row[3]
			break
			ra= random.randrange(267,282,1)+random.random()
			if (spent+constant)>25000:
				print spent
				break
			row.append(constant)
			row.append(ra)
			if (data2["usertag"][iterator])=="null":
				row.append(0)
			else:
				row.append(len((data2["usertag"][iterator]).split(",")))
			spamwriter.writerow(row)
			iterator=iterator+1
			spent=spent+constant
		#print iterator
		# for x in range(20):
			# ra= random.randrange(267,283,1)+random.random()
			# spamwriter.writerow([constant]+[ra])