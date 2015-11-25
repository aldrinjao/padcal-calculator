#fuel.py
#September 21, 2015
#fuel computation for SCOPE 1 of emissions

import csv,math
gwp={}


def fuel_exec():


	fname='./inputs/meta.csv'
	with open(fname, 'r+') as in_config:
		reader = csv.reader(in_config, delimiter=',')
		row = next(reader)

		project = row[1]

		for row in range(0,7):
			next(reader)

		row = next(reader)
		encoder=row[1]
		date=row[2]








	#read gwp dictionary 
	with open('./inputs/scope1/fuel/gwp.csv', 'r+') as in_csv:
		reader = csv.reader(in_csv, delimiter=',')
		for row in reader:
			#create dict of GWP
			gwp[row[0]]=float(row[1])

	gjEF = {}
	co2EF = {}
	ch4EF = {}
	n2oEF = {}

	gasEm = {}
	dieselEm = {}
	bDieselEm = {}
	bGasEM = {}
	lpg = {}

	totalGasConsumed = 0 
	totalDieselConsumed = 0 
	totalBGasConsumed = 0
	totalBDieselConsumed = 0
	totalLPGConsumed = 0

	totalCO2= 0
	totalCH4= 0
	totalN2O= 0

	#read Emission Factors from csv

	with open('./inputs/scope1/fuel/EmissionFactor.csv', 'r+') as in_csv:
		reader = csv.reader(in_csv, delimiter=',')
		next(reader)
		for row in reader:
			#create dict of Emission Factors by making associative arrays with the fuel type
			gjEF[row[0]]=float(row[1])
			co2EF[row[0]]=float(row[2])
			ch4EF[row[0]]=float(row[3])
			n2oEF[row[0]]=float(row[4])


	#
	with open('./inputs/scope1/fuel/consumedFuel.csv', 'r+') as in_csv:
		reader = csv.reader(in_csv, delimiter=',')
		next(reader)
		for row in reader:
			
			totalGasConsumed += float(row[2])
			totalDieselConsumed += float(row[1])
			totalBGasConsumed += float(row[3])
			totalBDieselConsumed += float(row[4])
			totalLPGConsumed += float(row[5])

	#compute for CO2,CH4,N2O for individual type of Gases 

	gasCO2 = totalGasConsumed * co2EF['gas']
	dieselCO2 = totalDieselConsumed * co2EF['diesel'] 
	bDieselCO2 = totalBDieselConsumed * co2EF['blended diesel'] 
	bGasCO2 = totalBDieselConsumed * co2EF['blended gas']
	lpgCO2 = totalBDieselConsumed * co2EF['lpg']

	gasCH4 = totalGasConsumed * ch4EF['gas'] 
	dieselCH4 = totalDieselConsumed * ch4EF['diesel']
	bDieselCH4 = totalBDieselConsumed * ch4EF['blended diesel']
	bGasCH4 = totalBDieselConsumed * ch4EF['blended gas']
	lpgCH4 = totalBDieselConsumed * ch4EF['lpg'] 

	gasN2O = totalGasConsumed * n2oEF['gas'] 
	dieselN2O = totalDieselConsumed * n2oEF['diesel']
	bDieselN2O = totalBDieselConsumed * n2oEF['blended diesel']
	bGasN2O = totalBDieselConsumed * n2oEF['blended gas']
	lpgN2O = totalBDieselConsumed * n2oEF['lpg']


	#write output to a file
	with open('./outputs/percomponent/scope1_fuel.csv' , 'w+') as summary_out_csv:
		summarywriter = csv.writer(summary_out_csv, delimiter=',',lineterminator='\n',quoting=csv.QUOTE_NONE)
		summarywriter.writerow(['PROJECT:',project,'ENCODER:',encoder,'DATE:', date])
		summarywriter.writerow([])


		summarywriter.writerow(['TYPE','kg CO2/liter','kg CH4/liter','kg N2O/liter','TOTAL CONSUMED'])
		summarywriter.writerow(['gas',gasCO2,gasCH4,gasN2O,totalGasConsumed])
		summarywriter.writerow(['diesel',dieselCO2,dieselCH4,dieselN2O,totalDieselConsumed])
		summarywriter.writerow(['blended gas',bGasCO2,bGasCH4,bGasN2O,totalBGasConsumed])
		summarywriter.writerow(['blended diesel',bDieselCO2,bDieselCH4,bDieselN2O,totalBDieselConsumed])
		summarywriter.writerow(['lpg',lpgCO2,lpgCH4,lpgN2O,totalLPGConsumed])
		
		totalCO2 = gasCO2+dieselCO2+bGasCO2+bDieselCO2+lpgCO2
		totalCH4 = gasCH4+dieselCH4+bGasCH4+bDieselCH4+lpgCH4
		totalN2O = gasN2O+dieselN2O+bGasN2O+bDieselN2O+lpgN2O

		summarywriter.writerow(['TOTAL',totalCO2,totalCH4,totalN2O])
		summarywriter.writerow(['GWP',gwp['co2'],gwp['ch4'],gwp['n2o']])
		summarywriter.writerow(['TOTAL * gwp',(totalCO2)*gwp['co2'],(totalCH4)*gwp['ch4'],(totalN2O)*gwp['n2o']])
		summarywriter.writerow(['',''])

		totalCO2 = totalCO2 * gwp['co2']
		totalCH4 = totalCH4 * gwp['ch4']
		totalN2O = totalN2O * gwp['n2o']
		
		grandTotal = totalCO2 + totalCH4 + totalN2O
		summarywriter.writerow(['TOTAL EMISSIONS (Mg)', (grandTotal)/1000])