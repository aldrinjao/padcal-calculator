import csv,math

#create a config file to be read for size of plot and number of plot
#and the headers

#calculate na pagread tapos iread na lang ulit pag ok na para issumarize?

#magingat sa input csv na walang extra columns
#maglagay ng cleanup ng input csv


#read from config.csv the number of plots and plot area

def tbd_mainplot_exec():


	fname='./inputs/meta.csv'
	with open(fname, 'r+') as in_config:
		reader = csv.reader(in_config, delimiter=',')
		row = next(reader)

		project = row[1]

		for row in range(0,3):
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
			plotArea = float(row[1])


	tbPlotSum  = [0] * numberOfPlots
	tcPlotSum  = [0] * numberOfPlots
	tcoPlotSum = [0] * numberOfPlots

	rbPlotSum  = [0] * numberOfPlots
	rcPlotSum  = [0] * numberOfPlots
	rcoPlotSum = [0] * numberOfPlots

	treePerPlot = [0] * numberOfPlots

	mgPlot      = [0] * numberOfPlots
	mgHAPlot    = [0] * numberOfPlots



	with open('./inputs/treeAndRoot/mainTreeAndRoot.csv', 'r+') as in_csv:
		reader = csv.reader(in_csv, delimiter=',')
		#writer = csv.writer(out_csv, delimiter=',',lineterminator='\n',quoting=csv.QUOTE_NONE)
		next(reader)
		for row in reader:
			
			#decode the row values
			plotIndex =int(row[0])-1

			if int(row[1])!=0:
				dbh=float(row[3])
				commonName=str(row[2]).lower()
				conifer = 'benguet pine'
				#count trees per plot
				treePerPlot[plotIndex]+=1
				flag = 0

				#TBD conifer add category filter for conifer
				
				if conifer in commonName:
					tbd=math.exp(-1.170+2.119*math.log(dbh))
				else:
					if (dbh < 60): 
						tbd=math.exp(-2.134+2.53*math.log(dbh))
					elif(dbh >=60 ):
						tbd = (42.69 - 12.8 * dbh) + ( 1.242 * dbh^2)

				#root BD
				rbd = math.exp(-1.0587+0.8836*math.log(tbd))
				rbPlotSum[plotIndex] += rbd
				rcPlotSum[plotIndex] += rbd * 0.45
				rcoPlotSum[plotIndex] += (rbd * 0.45) * (44/12)

				#trees
				tbPlotSum[plotIndex] +=tbd
				tcPlotSum[plotIndex] += tbd*0.45
				tcoPlotSum[plotIndex] += (tbd*0.45) * (44/12)
		
	#for printing

	with open('./outputs/percomponent/treeandRootBiomass_summary_mainplot.csv' , 'w+') as summary_out_csv:
		summarywriter = csv.writer(summary_out_csv, delimiter=',',lineterminator='\n',quoting=csv.QUOTE_NONE)
		summarywriter.writerow(['PROJECT:',project,'ENCODER:',encoder,'DATE:', date])
		summarywriter.writerow([])

		summarywriter.writerow(['MAIN PLOT #','TBD (Mg ha^-1)','TREE CARBON STOCK (Mg ha^-1)','TREE CO2 (Mg ha^-1)','ROOT BIOMASS (Mg ha^-1)','ROOT CARBON STOCK (Mg ha^-1)','ROOT CO2 (Mg ha^-1)'])
		for i in range(0, numberOfPlots):
			summarywriter.writerow([i+1,tbPlotSum[i]/1000/plotArea,(tcPlotSum[i]/1000/plotArea),(tcoPlotSum[i]/1000/plotArea),rbPlotSum[i]/1000/plotArea,rcPlotSum[i]/1000/plotArea,rcoPlotSum[i]/1000/plotArea]) 

	with open('./outputs/percomponent/treeBiomass_summary_mainplot.csv' , 'w+') as summary_out_csv:
		summarywriter = csv.writer(summary_out_csv, delimiter=',',lineterminator='\n',quoting=csv.QUOTE_NONE)
		summarywriter.writerow(['PROJECT:',project,'ENCODER:',encoder,'DATE:', date])
		summarywriter.writerow([])

		summarywriter.writerow(['MAIN PLOT #','TBD (Mg ha^-1)','TREE CARBON STOCK (Mg ha^-1)','TREE CO2 (Mg ha^-1)'])
		for i in range(0, numberOfPlots):
			summarywriter.writerow([i+1,tbPlotSum[i]/1000/plotArea,(tcPlotSum[i]/1000/plotArea),(tcoPlotSum[i]/1000/plotArea)]) 

	with open('./outputs/percomponent/rootBiomass_summary_mainplot.csv' , 'w+') as summary_out_csv:
		summarywriter = csv.writer(summary_out_csv, delimiter=',',lineterminator='\n',quoting=csv.QUOTE_NONE)
		summarywriter.writerow(['PROJECT:',project,'ENCODER:',encoder,'DATE:', date])
		summarywriter.writerow([])

		summarywriter.writerow(['MAIN PLOT #','ROOT BIOMASS (Mg ha^-1)','ROOT CARBON STOCK (Mg ha^-1)','ROOT CO2 (Mg ha^-1)'])
		for i in range(0, numberOfPlots):
			summarywriter.writerow([i+1,rbPlotSum[i]/1000/plotArea,rcPlotSum[i]/1000/plotArea,rcoPlotSum[i]/1000/plotArea]) 