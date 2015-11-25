import csv,math


	#read from config.csv the number of plots and plot area

def iclei_exec():
		
	array_results=[]



		#changed directory for building cx_Freeze
	with open('./inputs/scope3/iclei_results.csv', 'r+') as in_csv:
		reader = csv.reader(in_csv, delimiter=',')
		next(reader)
		
		row= next(reader)
		array_results.append(row[1])
		row= next(reader)
		array_results.append(row[1])
		row= next(reader)
		array_results.append(row[1])

		row= next(reader)
		row= next(reader)
		row= next(reader)
		array_results.append(row[1])

		return array_results