import csv,math

pi = 3.1415926535897

def cwd_exec():

	fname='./inputs/meta.csv'
	with open(fname, 'r+') as in_config:
		reader = csv.reader(in_config, delimiter=',')
		row = next(reader)

		project = row[1]

		for row in range(0,4):
			next(reader)

		row = next(reader)
		encoder=row[1]
		date=row[2]



	#read from config.csv the number of plots and plot area
	fname='./inputs/config.csv'
	with open(fname, 'r+') as in_config:
		reader = csv.reader(in_config, delimiter=',')
		next(reader)
		for row in reader:
			numberOfPlots=int(row[0])
			plotArea = float(row[2])


	woodDensitySound = {}
	woodDensityIntermediate = {}
	woodDensityRotten = {}
	woodDensityAverage = {}


	perPlotCO2 = [0] * numberOfPlots
	perPlotCStored = [0] * numberOfPlots
	perPlotWoodDensity =[0] * numberOfPlots

	treePerPlot = [0] * numberOfPlots

	cPerPlot = [0] * numberOfPlots
	CO2PerPlot = [0] * numberOfPlots
	biomassDensityPerPlot = [0] * numberOfPlots




	with open('./inputs/cwd/woodDensity.csv', 'r+') as in_csv:
		reader = csv.reader(in_csv, delimiter=',')
		next(reader)

		for row in reader:
			woodDensitySound[row[0]]=row[1]
			woodDensityIntermediate[row[0]] = row[2]
			woodDensityRotten[row[0]] = row[3]
			woodDensityAverage[row[0]] = row[4]




	with open('./inputs/cwd/cwd.csv', 'r+') as in_csv:
		reader = csv.reader(in_csv, delimiter=',')
		next(reader)
		#writer = csv.writer(out_csv, delimiter=',',lineterminator='\n',quoting=csv.QUOTE_NONE)

		for row in reader:

			plotIndex =int(row[0])-1

			smallEnd = float(row[5])
			bigEnd = float(row[4])
			length = float(row[6])

			volume = (1/3)* pi * length * ((pow((bigEnd/2),2)) + pow((smallEnd/2),2) + ((bigEnd/2)*(smallEnd/2)))


			status =row[7].lower().strip()
			treeName= row[3].lower().strip()
			woodSampleDensity = 0.0

			if (status == 'sound'):
				woodSampleDensity =woodDensitySound[treeName]
			elif (status =='intermediate'):
				woodSampleDensity =woodDensityIntermediate[treeName]
			elif (status == 'rotten'):
				woodSampleDensity =woodDensityRotten[treeName]
			elif (status == '4'):
				woodSampleDensity =woodDensityAverage[treeName]
			elif (status == '1'):
				biomassDensity = math.exp(-1.17 + 2.119 * math.log(bigEnd)) - 73.87

			if(status != '1'):
				biomassDensity = float(woodSampleDensity)*float(volume)
			CStored = biomassDensity * 0.45
			CO2 = CStored * (44/12)

			cPerPlot[plotIndex] += CStored
			CO2PerPlot[plotIndex]+= CO2
			biomassDensityPerPlot[plotIndex]+=biomassDensity



	with open('./outputs/percomponent/cwd.csv' , 'w+') as summary_out_csv:
		summarywriter = csv.writer(summary_out_csv, delimiter=',',lineterminator='\n',quoting=csv.QUOTE_NONE)
		summarywriter.writerow(['PROJECT:',project,'ENCODER:',encoder,'DATE:', date])
		summarywriter.writerow([])

		summarywriter.writerow(['PLOT #','Biomass Density (kg)', 'Carbon Stored (mg ha^-1)','CO2(mg ha^-1)'])
		for x in range(0,numberOfPlots):
			summarywriter.writerow([x+1,(biomassDensityPerPlot[x]/1000)/plotArea,(cPerPlot[x]/1000)/plotArea,(CO2PerPlot[x]/1000)/plotArea])
