#lpgIssuance.py
#October 9, 2015
#fugitive emission computation for SCOPE 3 - LPG

import csv,math


efficiencyCO2={}
efficiencyCH4={}
efficiencyN2O={}


# [0] = first index is Total Distance traveled
# [1] = kg CO2
# [2] = kg CH4 
# [3] = kg N2O

totalLarge = [0]*4
totalSmall = [0]*4
totalMedium = [0]*4




gwp={}

def lpgIssuance_exec():



	encoder =''
	date = ''
	project= ''

	fname='./inputs/meta.csv'
	with open(fname, 'r+') as in_config:
		reader = csv.reader(in_config, delimiter=',')
		row = next(reader)

		project = row[1]

		for row in range(0,12):
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

	with open('./inputs/scope3/lpgEF.csv', 'r+') as in_csv:
		reader = csv.reader(in_csv, delimiter=',')
		next(reader)
		for row in reader:
			#create dict of GWP
			key =str(row[0]).lower()
			efficiencyCO2[key]=float(row[1])
			efficiencyCH4[key]=float(row[2])
			efficiencyN2O[key]=float(row[3])


	with open('./inputs/scope3/lpg.csv', 'r+') as in_csv:
		reader = csv.reader(in_csv, delimiter=',')
		next(reader)
		next(reader)
		for row in reader:
			totalLarge[0] += float(row[3]) * 50
			totalMedium[0] += float(row[2]) * 22
			totalSmall[0] += float(row[1]) * 11


	totalLarge[1] = efficiencyCO2['lpg'] * totalLarge[0]
	totalLarge[2] = efficiencyCH4['lpg'] * totalLarge[0]
	totalLarge[3] = efficiencyN2O['lpg'] * totalLarge[0]

	totalMedium[1] = efficiencyCO2['lpg'] * totalMedium[0]
	totalMedium[2] = efficiencyCH4['lpg'] * totalMedium[0]
	totalMedium[3] = efficiencyN2O['lpg'] * totalMedium[0]

	totalSmall[1] = efficiencyCO2['lpg'] * totalSmall[0]
	totalSmall[2] = efficiencyCH4['lpg'] * totalSmall[0]
	totalSmall[3] = efficiencyN2O['lpg'] * totalSmall[0]

	totalWeight =totalLarge[0]+totalMedium[0]+totalSmall[0]
	totalCO2 = totalLarge[1]+totalMedium[1]+totalSmall[1]
	totalCH4 = totalLarge[2]+totalMedium[2]+totalSmall[2]
	totalN2O = totalLarge[3]+totalMedium[3]+totalSmall[3]

	with open('./outputs/percomponent/scope3_lpg.csv' , 'w+') as summary_out_csv:
		summarywriter = csv.writer(summary_out_csv, delimiter=',',lineterminator='\n',quoting=csv.QUOTE_NONE)

		summarywriter.writerow(['PROJECT:',project,'ENCODER:',encoder,'DATE:', date])
		summarywriter.writerow([])


		summarywriter.writerow(['Weight','kg','kg CO2','kg CH4','kg N2O'])
		
		summarywriter.writerow(['Small Tank',totalSmall[0],totalSmall[1],totalSmall[2],totalSmall[3]])
		summarywriter.writerow(['Medium Tank',totalMedium[0],totalMedium[1],totalMedium[2],totalMedium[3]])
		summarywriter.writerow(['Large Tank',totalLarge[0],totalLarge[1],totalLarge[2],totalLarge[3]])

		summarywriter.writerow(['TOTAL',totalWeight,totalCO2,totalCH4,totalN2O])
		totalCO2=totalCO2*gwp['co2']
		totalCH4=totalCH4*gwp['ch4']
		totalN2O=totalN2O*gwp['n2o']
		summarywriter.writerow(['gwp','',gwp['co2'],gwp['ch4'],gwp['n2o']])
		summarywriter.writerow(['TOTAL * gwp',totalWeight,totalCO2,totalCH4,totalN2O])

		summarywriter.writerow([])
		grandTotal = totalCO2 +totalCH4+totalN2O
		summarywriter.writerow(['Grand Total(kg)',grandTotal,'','Grand Total (Mg)',grandTotal/1000])