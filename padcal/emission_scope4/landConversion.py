# landConversion.py
# october 14, 2015
# compute Vegetation loss due to land conversion

import csv,math

def landcover_exec(biomass):

	areaCovered= 0
	ageOfForest= 0
	meanAnnualIncrement= 0
	cOfBiomass= 0
	CO2e= 0
	annualCLoss= 0
	mgCO2PerYear= 0
	percentOffsite= 0
	percentOnsite= 0
	percentDecay= 0
	percentLongTermsProducts= 0

	cLossOffsite= 0
	cLossOnsite= 0
	cLossDecay= 0
	cLossLongTermsProducts= 0

	co2Offsite= 0
	co2Onsite= 0
	co2Decay= 0
	co2LongTermsProducts= 0

	co2EmissionTotal= 0

	gwp={}

	ch4=0
	n2o=0
	
	fname='./inputs/scope4/forestInfo.csv'
	with open(fname, 'r+') as in_config:
		reader = csv.reader(in_config, delimiter=',')
		next(reader)
		for row in reader:
			ageOfForest= int(row[0])
			areaCovered= float(row[1])
			percentOffsite= float(row[2])/100
			percentOnsite=  float(row[3])/100
			percentDecay=  float(row[4])/100
			percentLongTermsProducts= float(row[5])/100

	fname='./inputs/scope4/gwp.csv'
	with open(fname, 'r+') as in_config:
		reader = csv.reader(in_config, delimiter=',')
		for row in reader:
			gwp[str(row[0])]= float(row[1])		


	meanAnnualIncrement=biomass/ageOfForest
	cOfBiomass= meanAnnualIncrement * 0.45
	CO2e= cOfBiomass * (44/12)
	annualCLoss= meanAnnualIncrement * areaCovered * 0.45
	mgCO2PerYear= annualCLoss * (44/12)

	cLossOffsite= annualCLoss * percentOffsite
	cLossOnsite= annualCLoss * percentOnsite
	cLossDecay= annualCLoss * percentDecay
	cLossLongTermsProducts= annualCLoss * percentLongTermsProducts

	co2Offsite= cLossOffsite * (44/12)
	co2Onsite= cLossOnsite * (44/12)
	co2Decay= cLossDecay * (44/12)
	co2LongTermsProducts= cLossLongTermsProducts * (44/12)

	co2EmissionTotal= co2Offsite + co2Onsite + co2Decay + co2LongTermsProducts
	ch4= cLossOnsite * 0.012 * gwp['ch4'] * (16/12)
	n2o= cLossOnsite * 0.01 * gwp['n2o'] * (44/28)

	ch4_forsummary= cLossOnsite * 0.012 * (16/12)
	n2o_forsummary= cLossOnsite * 0.01 *  (44/28)

	with open('./outputs/percomponent/scope4_landconversion.csv' , 'w+') as summary_out_csv:
		summarywriter = csv.writer(summary_out_csv, delimiter=',',lineterminator='\n',quoting=csv.QUOTE_NONE)
		summarywriter.writerow(['Ave. biomass of forest (Mg/ha)',biomass])
		summarywriter.writerow(['Age of the forest (years)',ageOfForest])
		summarywriter.writerow(['Mean Annual Increment (Mg/ha/year)',meanAnnualIncrement])
		summarywriter.writerow(['Biomass C (Mg/ha/year)',cOfBiomass])
		summarywriter.writerow(['Biomass CO2 e (Mg/ha/year)',CO2e])


		summarywriter.writerow([])
		summarywriter.writerow(['A = area covered ',areaCovered])
		summarywriter.writerow(['B = Annual Biomass growth/MAI',meanAnnualIncrement])
		summarywriter.writerow(['C = % C  in the biomass','45%'])
		summarywriter.writerow(['Annual Carbon Loss due to conversion=  A X B X C',annualCLoss])
		summarywriter.writerow(['Mg of CO2/year',mgCO2PerYear])

		totalCLoss=cLossDecay+cLossOnsite+cLossOffsite
		totalCO2=co2Decay+co2Onsite+co2Offsite
		summarywriter.writerow([])
		summarywriter.writerow(['On/Off Site Biomass Burning and Decay '])
		summarywriter.writerow(['Assumptions','C Loss','CO2'])
		summarywriter.writerow([str(percentOffsite*100) +'% off site burning of annual loss',cLossOffsite,co2Offsite])
		summarywriter.writerow([str(percentOnsite*100) +'% on-site burning',cLossOnsite,co2Onsite])
		summarywriter.writerow([str(percentDecay*100) +'% decay ',cLossDecay,co2Decay])
		summarywriter.writerow([str(percentLongTermsProducts*100) +'% long terms products',cLossLongTermsProducts,co2LongTermsProducts])
		summarywriter.writerow(['TOTAL',totalCLoss,totalCO2])



		summarywriter.writerow([])
		summarywriter.writerow(['Non-CO2 gases/trace gases ','gwp'])
		summarywriter.writerow(['gases','CH4','N2O'])
		summarywriter.writerow(['',ch4_forsummary,n2o_forsummary])
		summarywriter.writerow(['gwp',gwp['ch4'],gwp['n2o']])
		summarywriter.writerow(['gases * gwp',ch4,n2o])
		summarywriter.writerow(['TOTAL',n2o+ch4])
		

	
