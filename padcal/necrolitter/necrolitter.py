import csv,math


def necrolitter_exec():

	fname='./inputs/meta.csv'
	with open(fname, 'r+') as in_config:
		reader = csv.reader(in_config, delimiter=',')
		row = next(reader)

		project = row[1]

		for row in range(0,5):
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
			plotSize = float(row[3])

	percentMC = 0
	#understory
	hbd = 0
	cStored = 0
	coStored = 0


	totalMC = [0] * numberOfPlots
	totalHBD = [0] * numberOfPlots
	totalcStored = [0] * numberOfPlots
	totalcoStored = [0] * numberOfPlots
	totalFresh =[0] * numberOfPlots
	totalOvenDried=[0] * numberOfPlots
	numberSubplot=[0] * numberOfPlots
		
	#changed directory for building cx_Freeze
	with open('./inputs/necromass/necromass.csv', 'r+') as in_csv:
		reader = csv.reader(in_csv, delimiter=',')
		next(reader)
		for row in reader:
			#decode the row values
			plotIndex =int(row[0])-1

			hbd = (float(row[3]) / plotSize) * 100000 * (1/1000000)
			cStored = hbd * 0.45
			coStored = cStored * (44/12)
				
			totalHBD[plotIndex] += hbd
			totalcStored[plotIndex] += cStored
			totalcoStored[plotIndex] += coStored
			totalFresh[plotIndex]  += float(row[2])
			totalOvenDried[plotIndex]  += float(row[3])
			numberSubplot[plotIndex]+=1

				#changed directory for building cx_Freeze
	with open('./outputs/percomponent/necromass.csv' , 'w+') as summary_out_csv:
		summarywriter = csv.writer(summary_out_csv, delimiter=',',lineterminator='\n',quoting=csv.QUOTE_NONE)
		summarywriter.writerow(['PROJECT:',project,'ENCODER:',encoder,'DATE:', date])
		summarywriter.writerow([])


		summarywriter.writerow(['plot number','% MC','BioMass (Mg ha^-1)','C Stored (Mg ha^-1)','CO Stored (Mg ha^-1)'])
		for i in range(0, numberOfPlots):
			summarywriter.writerow([i+1,(totalFresh[i]-totalOvenDried[i])/totalFresh[i] * 100, totalHBD[i]/numberSubplot[i],totalcStored[i]/numberSubplot[i],totalcoStored[i]/numberSubplot[i]])
			#summarywriter.writerow([i+1,(totalFresh[i]-totalOvenDried[i])/totalFresh[i] * 100, totalHBD[i],totalcStored[i],totalcoStored[i]])