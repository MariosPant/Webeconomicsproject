import csv
import pandas
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
data = pandas.read_csv("ConstRand.csv")#OPEN file for comparison change name between ConstRand, Linear,Gaussian,Stochastic
data2 = pandas.read_csv("Linear.csv")
numeric_columns  = data._get_numeric_data()
numeric_columns2 = data2._get_numeric_data()
#open validation file, result files(const/rand,linear,gausian,stochastic)
print list(numeric_columns)
print list(numeric_columns2)
conversions = sum(data2["logtype"])
clicks =sum(data2["click"])#get sum of column clicks
views =sum(data2["Views"])#get sum of column views
Lavg = sum(data2["PBid"])/len(data2["payprice"])
#Cavg = sum(data["Const"])/len(data["click"])

# with open('SGDClassifier.csv', 'rb') as csvfile:
	# spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	# for row in spamreader:
		

# print len(data2["PBid"])
# print impressions
# print clicks
# print views
# print Lavg
# print Cavg
CTR = clicks/float(views)
CVR = conversions/(float(clicks))
avgCPM = Lavg/(views/1000)
avgCPC = Lavg/clicks#
AavgCPM = Lavg/(views/1000)
#AavgCPC = Cavg/clicks#
print len(data2["logtype"])
print CTR
print CVR
print conversions
print views#impressions
print Lavg
#print AavgCPC



tempdata = data.sample(frac=1,random_state=1)
#print sum(data["click"])
cols = ["click","weekday","hour","region","city","slotwidth","slotheight","payprice","bidprice","slotprice","Views"]
tempdata[cols].hist()

#plt.show()


#CTR clicks/views
#CVR = conversion/clicks
#avg CPM = avg of payment/1000views
#avg CPC = avg of payment/clicks

	
#print mean_squared_error(data2["bidprice"], data2["PBid"])
