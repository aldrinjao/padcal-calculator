import csv,math

def understorey_exec():

	fname='./inputs/meta.csv'
	with open(fname, 'r+') as in_config:
		reader = csv.reader(in_config, delimiter=',')
		row = next(reader)

		project = row[1]

		for row in range(0,6):
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
			plotSize = float(row[3])


	percentMC = 0
	#understorey
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
	with open('./inputs/understorey/understorey.csv', 'r+') as in_csv:

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



	with open('./outputs/percomponent/understorey.csv' , 'w+') as summary_out_csv:
		summarywriter = csv.writer(summary_out_csv, delimiter=',',lineterminator='\n',quoting=csv.QUOTE_NONE)
		summarywriter.writerow(['PROJECT:',project,'ENCODER:',encoder,'DATE:', date])
		summarywriter.writerow([])

		summarywriter.writerow(['plot number','% MC','BioMass','C Stored','CO Stored'])
		for i in range(0, numberOfPlots):
			summarywriter.writerow([i+1,(totalFresh[i]-totalOvenDried[i])/totalFresh[i] * 100, totalHBD[i]/numberSubplot[i],totalcStored[i]/numberSubplot[i],totalcoStored[i]/numberSubplot[i]]) 
			#summarywriter.writerow([i+1,(totalFresh[i]-totalOvenDried[i])/totalFresh[i] * 100, totalHBD[i],totalcStored[i],totalcoStored[i]]) 
