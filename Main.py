import csv
import numpy as np
import pandas
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.cross_validation import train_test_split
from sklearn import linear_model
#Model import
from sklearn.metrics import mean_squared_error #linear regretion
from sklearn.linear_model import SGDClassifier #stochastic
from sklearn.naive_bayes import GaussianNB		#Gaussian




data = pandas.read_csv("cluster.csv")
data2 = pandas.read_csv("test.csv")
numeric_columns = data._get_numeric_data()
numeric_columns2=data2._get_numeric_data()



#correlations
# tempdata = data.sample(frac=1,random_state=1)
# print len(tempdata["click"])
# print data.corr()["click"]
# print "\n"
# print sum(data["click"])
# tempdata.hist()
# plt.show()

# quit()

columns = numeric_columns
columns2 = numeric_columns2
columns3 = numeric_columns
columns4 = numeric_columns2
columns = [c for c in numeric_columns if c in ["logtype","hour","region","city","slotwidth","slotheight","slotprice"]]
columns2 = [c for c in numeric_columns2 if c in ["hour","logtype","region","city","slotwidth","slotheight","slotprice"]]

columns3 = [c for c in numeric_columns if c in ["weekday","hour","region","city","slotwidth","slotheight","slotprice"]] ##Maybe add bidprice after predicting it. MAYBE
columns4 = [c for c in numeric_columns2 if c in ["weekday","hour","region","city","slotwidth","slotheight","slotprice"]]

#print list(columns)
#print list(columns2)
# print list(columns3)
# print list(columns4)
#quit()
#percentage of data used to train
train = data.sample(frac=0.5,random_state=2)
test = data.loc[~data.index.isin(train.index)]

#TARGET BIDPRICE
#################################################################################

#$$$$$$$$$$$$$$$$$$$$$$ MODEL CHOICE $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
modelbid = linear_model.LinearRegression()
#modelbid = SGDClassifier(loss="huber")
#modelbid =GaussianNB()

#Model fit
target = "bidprice"
modelbid.fit(train[columns], train[target])

bidpredictions = modelbid.predict(data2[columns2])
##################################################################################

#TARGET CLICKS
##################################################################################
modelclick = linear_model.LinearRegression()
modelclick.fit(train[columns3], train["click"])

clickpredictions = modelclick.predict(data2[columns4])
##################################################################################
	

#USED TO GET TOP BIDS
#######################################################################	

g=0
A=[]
B=[]
C=[]


f = open("bids.txt","w")
f.write("No     ,Bid			,Click\n")

with open('test.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	spamreader.next()
	for x,z in zip(np.nditer(bidpredictions),np.nditer(clickpredictions)):
		row = spamreader.next()
		
		a=float(x)
		d=float(z)
		s = "{:6} ,{:.7f}, {}\n".format(g,a,d)
		f.write(s)
		A.append([row[3]])
		B.append([x])
		C.append([z])
		
		g=g+1
	f.close()



	bc = [B,C]

	BC = np.array(bc)#0 for Bids | 1 for clicks
	tempBC = np.argsort(BC,axis=1).astype(int).tolist()
	np.savetxt('bids2.txt', BC, delimiter=',') 
	finalbids=[]
	budget = 0
	n=0

	
	while True:
		z=tempBC[1].index([n])#index of top choices
		budget=budget+BC[0][z]
		finalbids.append(BC[0][z])
		
		n=n+1
	# if budget>25000:
		# finalbids.pop(-1)
	# print (finalbids)	


########################################################################

#DONT REMEMBER
#print (tempBC[1])
# BC= np.transpose(BC)
#np.set_printoptions(formatter={'float': '{: 0.3f}'.format})
# print(BC.shape)
# print BC(0,1)
# f = open("bids2.txt","w")
# f.write("Bid			,Click\n")
# for v in np.transpose(BC):
	# s = "{}, {}\n".format(v[0],v[1])
	# f.write(s)
#print mean_squared_error(predictions, test[target])



###########################################################################
##  Uses as many bids as required to reach 25000, no regard for usefullness
# iterator =0
# spent =0 
# with open('validation.csv', 'rb') as csvfile:
	# spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	# with open('SGDClassifier.csv', 'wb') as csvfile:				
		# spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
		# row = spamreader.next()
		# row.append("PBid")
		# row.append("Views")
		# spamwriter.writerow(row)
		##print len(bidpredictions)
		# for x in zip(np.nditer(bidpredictions)):
			# if (spent+x[0])>25000:
				# print spent
				# break
			# row = spamreader.next()
			# row.append(x[0])
			##Add views to result csv file, taken from "test.csv"
			# if (data2["usertag"][iterator])=="null":
				# row.append(0)
			# else:
				# row.append(len((data2["usertag"][iterator]).split(",")))
			# spamwriter.writerow(row)
			# iterator=iterator+1
			# spent = spent +x[0]
			