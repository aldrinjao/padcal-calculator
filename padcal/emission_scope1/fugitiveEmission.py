#fugitiveEmission.py
#September 21, 2015
#fugitive emission computation for SCOPE 1 of emissions

import csv,math




def fugitiveEmission_exec():

	fname='./inputs/meta.csv'
	with open(fname, 'r+') as in_config:
		reader = csv.reader(in_config, delimiter=',')
		row = next(reader)

		project = row[1]

		for row in range(0,8):
			next(reader)

		row = next(reader)
		encoder=row[1]
		date=row[2]

	gwp={}
	emission = [[0 for x in range(5)]] 
	rowCount=1
	#read gwp dictionary 
	with open('./inputs/scope1/fugitive emission/gwp.csv', 'r+') as in_csv:
		reader = csv.reader(in_csv, delimiter=',')
		next(reader)
		for row in reader:
			#create dict of GWP
			gwp[row[0]]=float(row[1])

	with open('./inputs/scope1/fugitive emission/fugitiveEmission.csv', 'r+') as in_csv:
		reader = csv.reader(in_csv, delimiter=',')
		next(reader)
		for row in reader:
			rowCount += 1
			emission.append([row[0],row[1],row[2],float(row[3])])


	#run trough the emissions table and compute the emissions
	#then output to a file
	total=0
	with open('./outputs/percomponent/scope1_fugitiveEmission.csv' , 'w+') as summary_out_csv:
		summarywriter = csv.writer(summary_out_csv, delimiter=',',lineterminator='\n',quoting=csv.QUOTE_NONE)
		summarywriter.writerow(['PROJECT:',project,'ENCODER:',encoder,'DATE:', date])
		summarywriter.writerow([])

		summarywriter.writerow(['Unit/Brand','Refrigerant','CHEMICAL FORMULA','QUANTITY','CO2 Emission (kg)','CO2 Emission (Mg)'])
		for row in range(1,rowCount):
			
			CO2 =  ((float(emission[row][3]) * .5) + (float(emission[row][3]) * .01)) * gwp[emission[row][2]]
			summarywriter.writerow([emission[row][0],emission[row][1],emission[row][2],emission[row][3],CO2,CO2/1000])
		