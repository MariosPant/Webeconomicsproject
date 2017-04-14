import csv

with open('cluster.csv', 'wb') as csvfile:
	var1=0
	spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
	with open('sample.csv', 'wb') as csvfile:
		spamwriter2 = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
		with open('train.csv', 'rb') as csvfile:
			spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')	
			##NEXT line is no of users	len(test[25:])
			row = spamreader.next()
			
			# row.append("Views")
			# row.append("CTR")
			# row.append("VPC")
			#print row			
			spamwriter.writerow(row)#[0:22])
			spamwriter2.writerow(row)#[0:22])
			#print row[1:22]
			for row in spamreader:
				
				# views = len(row[25:])
				# c = float(row[0])
				# price = float(row[22])
				# CTR = c/views
				
				# if ((price>0)and(c>0)): 
					# VPC = price/c
				# else:
					# VPC=0
				#row.pop(25:)
				#rowtemp = row[0:25]
				# row.append(views)
				# row.append(CTR)
				# row.append(VPC)
				
				spamwriter.writerow(row)#[0:22])
				if var1<100:
					spamwriter2.writerow(row)#[0:22])
				var1=var1+1
				
				# if CTR!=0:
					# print "found one ",CTR
					
				#if var1>5000:			
				#	break
				


			