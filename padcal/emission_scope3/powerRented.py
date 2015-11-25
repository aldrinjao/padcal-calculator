#powerRented.py
#October 9, 2015
#fugitive emission computation for SCOPE 3 - Power Rented

import csv,math



def powerRented_exec():


	efficiency={}
	power= [0] * 12
	source= [0] * 12

	totalPower=0

	rowCount = 0

	totalMWh = 0
	totalCO2 = 0

	encoder =''
	date = ''
	project= ''

	fname='./inputs/meta.csv'
	with open(fname, 'r+') as in_config:
		reader = csv.reader(in_config, delimiter=',')
		row = next(reader)

		project = row[1]

		for row in range(0,13):
			next(reader)

		row = next(reader)
		encoder=row[1]
		date=row[2]

	#read gwp dictionary 
	with open('./inputs/scope3/powerEF.csv', 'r+') as in_csv:
		reader = csv.reader(in_csv, delimiter=',')
		next(reader)
		for row in reader:
			#create dict of GWP
			efficiency[row[0]]=float(row[2])

	with open('./inputs/scope3/powerRented.csv', 'r+') as in_csv:
		reader = csv.reader(in_csv, delimiter=',')
		next(reader)
		for row in reader:
			rowCount+=1
			index=int(row[0]) -1
			power[index] = float(row[1])
			source[index] = row[2]

	with open('./outputs/percomponent/scope3_powerRented.csv' , 'w+') as summary_out_csv:
		summarywriter = csv.writer(summary_out_csv, delimiter=',',lineterminator='\n',quoting=csv.QUOTE_NONE)
		summarywriter.writerow(['PROJECT:',project,'ENCODER:',encoder,'DATE:', date])
		summarywriter.writerow([])

		summarywriter.writerow(['Month','Power Rented (kWh)','Power Rented (MWh)', 'total ton CO2 emission/MWh (Mg)'])
		for row in range(1,rowCount+1):

			temp1 = power[row-1]
			totalPower += temp1
			temp2 = power[row-1]/1000
			totalMWh += temp2
			temp3 = temp2 * efficiency[source[row-1]]
			totalCO2 += temp3
			summarywriter.writerow([row,temp1, temp2,temp3])
		
		summarywriter.writerow(['TOTAL',totalPower,totalMWh,totalCO2])
