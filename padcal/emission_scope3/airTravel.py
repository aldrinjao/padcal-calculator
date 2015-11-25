#airTravel.py
#October 9, 2015
#fugitive emission computation for SCOPE 3 - Air Travel

import csv,math


efficiencyCO2={}
efficiencyCH4={}
efficiencyN2O={}


# [0] = first index is Total Distance traveled
# [1] = kg CO2
# [2] = kg CH4 
# [3] = kg N2O

totalLong = [0]*4
totalShort = [0]*4
totalMedium = [0]*4

gwp={}

def airTravel_exec():

	fname='./inputs/meta.csv'
	with open(fname, 'r+') as in_config:
		reader = csv.reader(in_config, delimiter=',')
		row = next(reader)

		project = row[1]

		for row in range(0,10):
			next(reader)

		row = next(reader)
		encoder=row[1]
		date=row[2]
	#read gwp dictionary 
	with open('./inputs/scope3/gwp.csv', 'r+') as in_csv:
		reader = csv.reader(in_csv, delimiter=',')
		for row in reader:
			#create dict of GWP
			gwp[row[0]]=float(row[1])

	with open('./inputs/scope3/airEF.csv', 'r+') as in_csv:
		reader = csv.reader(in_csv, delimiter=',')
		next(reader)
		for row in reader:
			#create dict of GWP
			efficiencyCO2[row[1]]=float(row[2])
			efficiencyCH4[row[1]]=float(row[3])
			efficiencyN2O[row[1]]=float(row[4])


	with open('./inputs/scope3/airTravel.csv', 'r+') as in_csv:
		reader = csv.reader(in_csv, delimiter=',')
		next(reader)
		next(reader)
		for row in reader:
			totalLong[0] += float(row[1])
			totalMedium[0] += float(row[2])
			totalShort[0] += float(row[3])


	totalLong[1] = efficiencyCO2['long'] * totalLong[0]
	totalLong[2] = efficiencyCH4['long'] * totalLong[0]
	totalLong[3] = efficiencyN2O['long'] * totalLong[0]

	totalMedium[1] = efficiencyCO2['medium'] * totalMedium[0]
	totalMedium[2] = efficiencyCH4['medium'] * totalMedium[0]
	totalMedium[3] = efficiencyN2O['medium'] * totalMedium[0]

	totalShort[1] = efficiencyCO2['short'] * totalShort[0]
	totalShort[2] = efficiencyCH4['short'] * totalShort[0]
	totalShort[3] = efficiencyN2O['short'] * totalShort[0]

	totalmiles =totalLong[0]+totalMedium[0]+totalShort[0]
	totalCO2 = totalLong[1]+totalMedium[1]+totalShort[1]
	totalCH4 = totalLong[2]+totalMedium[2]+totalShort[2]
	totalN2O = totalLong[3]+totalMedium[3]+totalShort[3]

	with open('./outputs/percomponent/scope3_airTravel.csv' , 'w+') as summary_out_csv:
		summarywriter = csv.writer(summary_out_csv, delimiter=',',lineterminator='\n',quoting=csv.QUOTE_NONE)
		summarywriter.writerow(['PROJECT:',project,'ENCODER:',encoder,'DATE:', date])
		summarywriter.writerow([])

		summarywriter.writerow(['Miles Traveled','Total (mi)','kg CO2','kg CH4','kg N2O'])
		
		summarywriter.writerow(['Long Haul',totalLong[0],totalLong[1],totalLong[2],totalLong[3]])
		summarywriter.writerow(['Medium Haul',totalMedium[0],totalMedium[1],totalMedium[2],totalMedium[3]])
		summarywriter.writerow(['Short Haul',totalShort[0],totalShort[1],totalShort[2],totalShort[3]])

		totalCO2=totalCO2/1000
		totalCH4=totalCH4/1000
		totalN2O=totalN2O/1000

		summarywriter.writerow(['TOTAL (Mg)',totalmiles,totalCO2,totalCH4,totalN2O])

		totalCO2=totalCO2*2
		totalCH4=totalCH4*2
		totalN2O=totalN2O*2

		summarywriter.writerow(['TOTAL Round Trip',totalmiles,totalCO2,totalCH4,totalN2O])
	
		totalCO2=totalCO2*gwp['co2']
		totalCH4=totalCH4*gwp['ch4']
		totalN2O=totalN2O*gwp['n2o']

		summarywriter.writerow(['TOTAL Round Trip * GWP',totalmiles * 2,totalCO2,totalCH4,totalN2O])
		summarywriter.writerow([])
		grandTotal = totalCO2 + totalCH4 + totalN2O
		summarywriter.writerow(['Grand Total (Mg)',grandTotal,])