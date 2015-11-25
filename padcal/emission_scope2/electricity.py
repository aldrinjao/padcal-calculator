#electricity.py
#October 9, 2015
#fugitive emission computation for SCOPE 2 - Electricity

import csv,math

def electricity_exec():

	efficiency={}
	mill= [0] * 12
	mine= [0] * 12
	other= [0] * 12
	total= [0] * 12

	totalMill=0
	totalMine=0
	totalOther=0
	rowCount = 0




	efficiency={}

	coalmill= [0] * 12
	coalmine= [0] * 12
	coalother= [0] * 12
	coaltotal= [0] * 12

	lvmill= [0] * 12
	lvmine= [0] * 12
	lvother= [0] * 12
	lvtotal= [0] * 12

	minmill= [0] * 12
	minmine= [0] * 12
	minother= [0] * 12
	mintotal= [0] * 12

	coaltotalMill=0
	coaltotalMine=0
	coaltotalOther=0

	lvtotalMill=0
	lvtotalMine=0
	lvtotalOther=0

	mintotalMill=0
	mintotalMine=0
	mintotalOther=0

	rowCount = 0


	fname='./inputs/meta.csv'
	with open(fname, 'r+') as in_config:
		reader = csv.reader(in_config, delimiter=',')
		row = next(reader)

		project = row[1]

		for row in range(0,9):
			next(reader)

		row = next(reader)
		encoder=row[1]
		date=row[2]




	#read gwp dictionary 
	with open('./inputs/scope2/EF.csv', 'r+') as in_csv:
		reader = csv.reader(in_csv, delimiter=',')
		next(reader)
		for row in reader:
			#create dict of GWP
			efficiency[row[0]]=float(row[2])

	with open('./inputs/scope2/electricity.csv', 'r+') as in_csv:
		reader = csv.reader(in_csv, delimiter=',')
		next(reader)
		next(reader)	
		next(reader)

		for row in reader:
			rowCount+=1
			index=int(row[0]) -1

			coalmill[index] = float(row[1])
			coalmine[index] = float(row[2])
			coalother[index] = float(row[3])

			lvmill[index] = float(row[4])
			lvmine[index] = float(row[5])
			lvother[index] = float(row[6])

			minmill[index] = float(row[7])
			minmine[index] = float(row[8])
			minother[index] = float(row[9])

			coaltotalMill+=float(row[1])
			coaltotalMine+=float(row[2])
			coaltotalOther+=float(row[3])

			lvtotalMill+=float(row[4])
			lvtotalMine+=float(row[5])
			lvtotalOther+=float(row[6])

			mintotalMill+=float(row[7])
			mintotalMine+=float(row[8])
			mintotalOther+=float(row[9])


			total[index]=coalmill[index]+coalmine[index]+coalother[index] + lvmill[index]+lvmine[index]+lvother[index] +minmill[index]+minmine[index]+minother[index]


	with open('./outputs/percomponent/scope2_electricity.csv' , 'w+') as summary_out_csv:
		summarywriter = csv.writer(summary_out_csv, delimiter=',',lineterminator='\n',quoting=csv.QUOTE_NONE)
		summarywriter.writerow(['PROJECT:',project,'ENCODER:',encoder,'DATE:', date])
		summarywriter.writerow([])


		summarywriter.writerow(['SOURCE','Coal','Coal','Coal','Luzon-Visayas Grid','Luzon-Visayas Grid','Luzon-Visayas Grid','Mindanao Grid','Mindanao Grid','Mindanao Grid'])
		summarywriter.writerow(['Month','Mill Operations','Mine Operations','Other Loads','Mill Operations','Mine Operations','Other Loads','Mill Operations','Mine Operations','Other Loads'])
		for row in range(1,rowCount+1):
			summarywriter.writerow([row,coalmill[row-1],coalmine[row-1],coalother[row-1],lvmill[row-1],lvmine[row-1],lvother[row-1],minmill[row-1],minmine[row-1],minother[row-1]])
		summarywriter.writerow(['TOTAL (kg)',coaltotalMill,coaltotalMine,coaltotalOther,lvtotalMill,lvtotalMine,lvtotalOther,mintotalMill,mintotalMine,mintotalOther])

		coaltotalMill = coaltotalMill/1000
		coaltotalMine = coaltotalMine/1000
		coaltotalOther = coaltotalOther/1000

		lvtotalMill = lvtotalMill/1000
		lvtotalMine = lvtotalMine/1000
		lvtotalOther = lvtotalOther/1000

		mintotalMill = mintotalMill/1000
		mintotalMine = mintotalMine/1000
		mintotalOther = mintotalOther/1000


		summarywriter.writerow(['TOTAL (Mg)',coaltotalMill,coaltotalMine,coaltotalOther,lvtotalMill,lvtotalMine,lvtotalOther,mintotalMill,mintotalMine,mintotalOther])


		summarywriter.writerow(['efficiency',efficiency['1'],efficiency['1'],efficiency['1'],efficiency['2'],efficiency['2'],efficiency['2'],efficiency['3'],efficiency['3'],efficiency['3']])
		summarywriter.writerow(['tCO2e',efficiency['1']*coaltotalMill,efficiency['1']*coaltotalMine,efficiency['1']*coaltotalOther,efficiency['2']*lvtotalMill,efficiency['2']*lvtotalMine,efficiency['2']*lvtotalOther,efficiency['3']*mintotalMill,efficiency['3']*mintotalMine,efficiency['3']*mintotalOther])
		summarywriter.writerow(['TOTAL tCO2e',efficiency['1']*coaltotalMill+efficiency['1']*coaltotalMine+efficiency['1']*coaltotalOther+efficiency['2']*lvtotalMill+efficiency['2']*lvtotalMine+efficiency['2']*lvtotalOther+efficiency['3']*mintotalMill+efficiency['3']*mintotalMine+efficiency['3']*mintotalOther])