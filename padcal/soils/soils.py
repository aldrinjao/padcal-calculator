import csv,math

#read from plot,csv
#read from config.csv the number of plots and plot area

def soils_exec():

	encoder =''
	date = ''
	project= ''

	fname='./inputs/meta.csv'
	with open(fname, 'r+') as in_config:
		reader = csv.reader(in_config, delimiter=',')
		row = next(reader)

		project = row[1]

		for row in range(0,15):
			next(reader)

		row = next(reader)
		encoder=row[1]
		date=row[2]


	fname='./inputs/config.csv'
	with open(fname, 'r+') as in_config:
		reader = csv.reader(in_config, delimiter=',')
		next(reader)
		for row in reader:
			numberOfPlots=int(row[0])
			cylinder=float(row[4])

	fname='./inputs/soils/sampleDepth.csv'
	with open(fname, 'r+') as in_config:
		reader = csv.reader(in_config, delimiter=',')
		for row in reader:
			sampleDepth=float(row[1])	

	#initialize 4 x number of plots array
	odwTable = [[0 for x in range(4)] for x in range(numberOfPlots)] 
	soilsTable = [[0 for x in range(19)] for x in range(numberOfPlots)]

	perPlotSoilDensity =  [0] * numberOfPlots
	perPlotSoilCO2 =  [0] * numberOfPlots

	totalLowSoilDensity = 0
	totalLowSoilCO2 = 0

	totalMidSoilDensity = 0
	totalMidSoilCO2 = 0

	totalTopSoilDensity = 0
	totalTopSoilCO2 = 0



	totalSoilDensity = 0
	totalSoilCO2 = 0


	#gawing variable yung 0.1 depth
	soilVolume= 100 * 100 * sampleDepth


	#read odw and store in odwTable

	with open('./inputs/soils/soils.csv', 'r+') as odw_in_csv:
		odwreader = csv.reader(odw_in_csv, delimiter=',')
		next(odwreader)
		next(odwreader)
		for row in odwreader:
			plotIndex = int(row[0])-1
			for i in range(0,19):
				soilsTable[plotIndex][i] =row[i]
					

	with open('./inputs/soils/odw.csv', 'r+') as odw_in_csv:
		odwreader = csv.reader(odw_in_csv, delimiter=',')
		next(odwreader)
		for row in odwreader:
			plotIndex = int(row[0])-1
			for i in range(0,4):
				odwTable[plotIndex][i] =row[i]
			


	#computtttte
	for i in range(0,numberOfPlots):
		filename = "./outputs/percomponent/soils per plot/plot_"+str(i+1)+".csv" 	
		with open(filename , 'w+') as summary_out_csv:

			

			summarywriter = csv.writer(summary_out_csv, delimiter=',',lineterminator='\n',quoting=csv.QUOTE_NONE)
			summarywriter.writerow(['','low','','','','mid','','','','high','','',''])
			summarywriter.writerow(['','BD g/cm3','Weight','Soil Density','Soil CO2','BD g/cm3','Weight','Soil Density','Soil CO2','BD g/cm3','Weight','Soil Density','Soil CO2'])

			#for 0-10 low 
			lowbd = float(odwTable[i][1])/cylinder
			lowweight = lowbd * soilVolume
			lowsoilDensity=  lowweight * ( float(soilsTable[i][1])/100)
			lowsoilCO2 = lowsoilDensity * (44/12)


			#copy 2 more for 0-10 mid and 0-10 high

			midbd = float(odwTable[i][2])/cylinder
			midweight = midbd * soilVolume
			midsoilDensity=  midweight * ( float(soilsTable[i][7])/100)
			midsoilCO2 = midsoilDensity * (44/12)


			topbd = float(odwTable[i][3])/cylinder
			topweight = topbd * soilVolume
			topsoilDensity=  topweight * ( float(soilsTable[i][13])/100)
			topsoilCO2 = topsoilDensity * (44/12)


			#compute totals
			totalLowSoilDensity += lowsoilDensity
			totalLowSoilCO2 += lowsoilCO2

			totalMidSoilDensity += midsoilDensity
			totalMidSoilCO2 += midsoilCO2

			totalTopSoilDensity += topsoilDensity
			totalTopSoilCO2 += topsoilCO2
			######################################

			lowbd = format(lowbd, '.2f')
			lowweight = format(lowweight, '.2f')
			lowsoilDensity = format(lowsoilDensity, '1.2f')
			lowsoilCO2 = format(lowsoilCO2, '1.2f')

			midbd = format(midbd, '.2f')
			midweight = format(midweight, '.2f')
			midsoilDensity = format(midsoilDensity, '1.2f')
			midsoilCO2 = format(midsoilCO2, '1.2f')

			topbd = format(topbd, '.2f')
			topweight = format(topweight, '.2f')
			topsoilDensity = format(topsoilDensity, '1.2f')
			topsoilCO2 = format(topsoilCO2, '1.2f')



			summarywriter.writerow(['0-10 cm',lowbd,lowweight,lowsoilDensity,lowsoilCO2,midbd,midweight,midsoilDensity,midsoilCO2,topbd,topweight,topsoilDensity,topsoilCO2,])


			#for 10-20 low 
			lowbd = float(odwTable[i][1])/cylinder
			lowweight = lowbd * soilVolume
			lowsoilDensity=  lowweight * ( float(soilsTable[i][3])/100)
			lowsoilCO2 = lowsoilDensity * (44/12)


			#copy 2 more for 0-10 mid and 0-10 high

			midbd = float(odwTable[i][2])/cylinder
			midweight = midbd * soilVolume
			midsoilDensity=  midweight * ( float(soilsTable[i][9])/100)
			midsoilCO2 = midsoilDensity * (44/12)


			topbd = float(odwTable[i][3])/cylinder
			topweight = topbd * soilVolume
			topsoilDensity=  topweight * ( float(soilsTable[i][15])/100)
			topsoilCO2 = topsoilDensity * (44/12)


			#compute totals
			totalLowSoilDensity += lowsoilDensity
			totalLowSoilCO2 += lowsoilCO2

			totalMidSoilDensity += midsoilDensity
			totalMidSoilCO2 += midsoilCO2

			totalTopSoilDensity += topsoilDensity
			totalTopSoilCO2 += topsoilCO2
			######################################

			lowbd = format(lowbd, '.2f')
			lowweight = format(lowweight, '.2f')
			lowsoilDensity = format(lowsoilDensity, '1.2f')
			lowsoilCO2 = format(lowsoilCO2, '1.2f')

			midbd = format(midbd, '.2f')
			midweight = format(midweight, '.2f')
			midsoilDensity = format(midsoilDensity, '1.2f')
			midsoilCO2 = format(midsoilCO2, '1.2f')


			topbd = format(topbd, '.2f')
			topweight = format(topweight, '.2f')
			topsoilDensity = format(topsoilDensity, '1.2f')
			topsoilCO2 = format(topsoilCO2, '1.2f')

			summarywriter.writerow(['10-20 cm',lowbd,lowweight,lowsoilDensity,lowsoilCO2,midbd,midweight,midsoilDensity,midsoilCO2,topbd,topweight,topsoilDensity,topsoilCO2,])
			

			#for 20-30 low
			lowbd = float(odwTable[i][1])/cylinder
			lowweight = lowbd * soilVolume
			lowsoilDensity=  lowweight * ( float(soilsTable[i][5])/100)
			lowsoilCO2 = lowsoilDensity * (44/12)


			#copy 2 more for 0-10 mid and 0-10 high

			midbd = float(odwTable[i][2])/cylinder
			midweight = midbd * soilVolume
			midsoilDensity=  midweight * ( float(soilsTable[i][11])/100)
			midsoilCO2 = midsoilDensity * (44/12)





			topbd = float(odwTable[i][3])/cylinder
			topweight = topbd * soilVolume
			topsoilDensity=  topweight * ( float(soilsTable[i][17])/100)
			topsoilCO2 = topsoilDensity * (44/12)

			#compute totals
			totalLowSoilDensity += lowsoilDensity
			totalLowSoilCO2 += lowsoilCO2

			totalMidSoilDensity += midsoilDensity
			totalMidSoilCO2 += midsoilCO2

			totalTopSoilDensity += topsoilDensity
			totalTopSoilCO2 += topsoilCO2
			######################################

			lowbd = format(lowbd, '.2f')
			lowweight = format(lowweight, '.2f')
			lowsoilDensity = format(lowsoilDensity, '1.2f')
			lowsoilCO2 = format(lowsoilCO2, '1.2f')


			midbd = format(midbd, '.2f')
			midweight = format(midweight, '.2f')
			midsoilDensity = format(midsoilDensity, '1.2f')
			midsoilCO2 = format(midsoilCO2, '1.2f')


			topbd = format(topbd, '.2f')
			topweight = format(topweight, '.2f')
			topsoilDensity = format(topsoilDensity, '1.2f')
			topsoilCO2 = format(topsoilCO2, '1.2f')


			summarywriter.writerow(['20-30 cm',lowbd,lowweight,lowsoilDensity,lowsoilCO2,midbd,midweight,midsoilDensity,midsoilCO2,topbd,topweight,topsoilDensity,topsoilCO2,])




			summarywriter.writerow(['totalLowSoilDensity',totalLowSoilDensity,'totalLowSoilCO2',totalLowSoilCO2])
			summarywriter.writerow(['totalMidSoilDensity',totalMidSoilDensity,'totalMidSoilCO2',totalMidSoilCO2])
			summarywriter.writerow(['totalTopSoilDensity',totalTopSoilDensity,'totalTopSoilCO2',totalTopSoilCO2])
			summarywriter.writerow(['averageSoilDensity',(totalLowSoilDensity+totalMidSoilDensity+totalTopSoilDensity)/3])
			summarywriter.writerow(['averageSoilDensity',(totalLowSoilCO2+totalMidSoilCO2+totalTopSoilCO2)/3])
			
			totalSoilDensity +=(totalLowSoilDensity+totalMidSoilDensity+totalTopSoilDensity)/3
			totalSoilCO2 +=(totalLowSoilCO2+totalMidSoilCO2+totalTopSoilCO2)/3


			perPlotSoilCO2[i] =(totalLowSoilCO2+totalMidSoilCO2+totalTopSoilCO2)/3
			perPlotSoilDensity[i]=(totalLowSoilDensity+totalMidSoilDensity+totalTopSoilDensity)/3

			totalLowSoilDensity =0
			totalMidSoilDensity=0
			totalTopSoilDensity=0
			totalLowSoilCO2=0
			totalMidSoilCO2=0
			totalTopSoilCO2=0






	with open('./outputs/percomponent/soils_AllPlotsSummary.csv' , 'w+') as summary_out_csv:

		summarywriter = csv.writer(summary_out_csv, delimiter=',',lineterminator='\n',quoting=csv.QUOTE_NONE)
		summarywriter.writerow(['PROJECT:',project,'ENCODER:',encoder,'DATE:', date])
		summarywriter.writerow([])

		summarywriter.writerow(['PLOT #','Soil Density (mg ha^-1)','Soil CO2(mg ha^-1)'])

		for i in range(0,numberOfPlots):
			summarywriter.writerow([(i+1),perPlotSoilDensity[i],perPlotSoilCO2[i]])

		summarywriter.writerow(['TOTAL',totalSoilDensity,totalSoilCO2])
		summarywriter.writerow(['AVE',totalSoilDensity/numberOfPlots,totalSoilCO2/numberOfPlots])
