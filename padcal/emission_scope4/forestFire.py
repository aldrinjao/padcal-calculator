#forestFire.py
#October 13, 2015
#forestFire emission computation for SCOPE 4

import csv,math



def forestFire_exec(treeBiomass,understoreyBiomass,necroBiomass,cwdBiomass):



	rowCount =0
	burnedArea =[]
	index =0
	totalBurnedArea =0
	gwp ={}
	aveBiomass =0
	age =0
	mAI=0
	cMAI=0
	MgofCPerYear = 0
	percentCInBiomass = 0.45
	biomassPerYear= 0
	carbonReleased = 0
	CO2 = 0
	CH4 = 0
	N2O = 0
	CO2gwp =0
	CH4gwp = 0
	N2Ogwp = 0
	totalMGofCO2 =0
	totalMGofCO2TraceGases = 0
	CO2FromDecay = 0
	total = 0

	carbonLossPerYear = 0

	################################
	#READ INPUT
	################################

	fname='./inputs/meta.csv'
	with open(fname, 'r+') as in_config:
		reader = csv.reader(in_config, delimiter=',')
		row = next(reader)

		project = row[1]

		for row in range(0,14):
			next(reader)

		row = next(reader)
		encoder=row[1]
		date=row[2]


	#read forestFire.csv to get the burned forest area 
	with open('./inputs/scope4/forestFire.csv', 'r+') as in_csv:
		reader = csv.reader(in_csv, delimiter=',')
		next(reader)
		for row in reader:
			rowCount+=1
			index=int(row[0]) -1
			burnedArea.append(float(row[1]))


	#read forestInfo.csv to get average biomass and age of forest 
	with open('./inputs/scope4/forestInfo.csv', 'r+') as in_csv:
		reader = csv.reader(in_csv, delimiter=',')
		next(reader)
		row=next(reader)
		age=int(row[0])

	aveBiomass = treeBiomass *.1 +cwdBiomass +necroBiomass+understoreyBiomass
			
	#read gwp dictionary 
	with open('./inputs/scope4/gwp.csv', 'r+') as in_csv:
		reader = csv.reader(in_csv, delimiter=',')
		for row in reader:
			#create dict of GWP
			gwp[row[0]]=float(row[1])


	for x in range(0,len(burnedArea)):
		totalBurnedArea +=burnedArea[x]


####################################################
#
# PROCESS INPUT FROM CSV FILES
# these are the formulas for computing the total CO2e
#  
#
####################################################



	mAI=aveBiomass/age
	cMAI= mAI * 0.45

	MgofCPerYear = totalBurnedArea * mAI * .45
	carbonLossPerYear = MgofCPerYear * (44/12)

	biomassPerYear = mAI * totalBurnedArea

	CO2 = carbonLossPerYear 
	CH4 = MgofCPerYear * 0.012 * (16/12)
	N2O = MgofCPerYear * 0.007 * (44/28)



	CO2gwp = CO2 *gwp['co2']
	CH4gwp = CH4 *gwp['ch4']
	N2Ogwp = N2O *gwp['n2o']

	totalMGofCO2=CO2gwp+CH4gwp+N2Ogwp
	totalMGofCO2TraceGases=CH4gwp+N2Ogwp

	CO2FromDecay = ( MgofCPerYear * 0.1 ) * (44/12)

	carbonFromDecay = MgofCPerYear * 0.1
	CH4FromDecay = (carbonFromDecay * 0.012 * (16/12))
	N2OFromDecay = (carbonFromDecay * 0.007 * (44/28))

	CO2FromDecaygwp = CO2FromDecay * gwp['co2']
	CH4FromDecaygwp = CH4FromDecay * gwp['ch4']
	N2OFromDecaygwp = N2OFromDecay * gwp['n2o']

	totalMGofCO2FromDecayTraceGases = CH4FromDecaygwp + N2OFromDecaygwp

	total = CO2FromDecay + CO2 + totalMGofCO2TraceGases


#################################################
#
#PRODUCE OUTPUT ->scope4_forestFire.csv
#
#################################################

	with open('./outputs/percomponent/scope4_forestFire.csv' , 'w+') as summary_out_csv:
		summarywriter = csv.writer(summary_out_csv, delimiter=',',lineterminator='\n',quoting=csv.QUOTE_NONE)

		summarywriter.writerow(['PROJECT:',project,'ENCODER:',encoder,'DATE:', date])
		summarywriter.writerow([])

		summarywriter.writerow(['Biomass Mean Annual Increment',mAI])
		summarywriter.writerow(['Annual Carbon Loss due to fire',MgofCPerYear])
		summarywriter.writerow([])
		summarywriter.writerow(['summary'])
		summarywriter.writerow(['','','gwp','emission'])
		summarywriter.writerow(['CO2',CO2,gwp['co2'],CO2*gwp['co2']])
		summarywriter.writerow(['CH4',CH4,gwp['ch4'],CH4*gwp['ch4']])
		summarywriter.writerow(['N2O',N2O,gwp['n2o'],N2O*gwp['n2o']])
		summarywriter.writerow([])

		summarywriter.writerow(['TOTAL'])
		summarywriter.writerow(['Mg Non-CO2/trace gases',CH4*gwp['ch4'] + N2O*gwp['n2o']])
		summarywriter.writerow(['Mg of CO2e',CO2*gwp['co2']+CH4*gwp['ch4']+N2O*gwp['n2o']])