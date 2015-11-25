# summarize.py
# october 14, 2015
# python file that will summarize the vegetation data

import csv,math

import understorey.understorey as understorey
import necrolitter.necrolitter as necrolitter
import cwd.cwd as cwd
import treebiomass.tbd_biggerplot as tbd_biggerplot
import treebiomass.tbd_mainplot as tbd_mainplot
import soils.soils as soils

import emission_scope1.fuel as fuel
import emission_scope1.fugitiveEmission as fugitiveEmission

import emission_scope2.electricity as electricity

import emission_scope3.powerRented as powerRented
import emission_scope3.airTravel as airTravel
import emission_scope3.iclei as iclei
import emission_scope3.lpgIssuance as lpgIssuance

import emission_scope4.landConversion as landConversion
import emission_scope4.forestFire as forestFire

from xlwt import *


clear = lambda: os.system('cls')



#call vegetation vegetation components
try:
	necrolitter.necrolitter_exec()
	print('(vegetation component 1 of 6) necromass computation successful')
	print('necromass.csv created\n')


except Exception as e:
	print('\n!!!')
	print(str(e))
	print('\n')
	input("Press ENTER to close the program")
	quit()

try:
	understorey.understorey_exec()
	print('(vegetation component 2 of 6) understorey computation successful')
	print('understorey.csv created\n')
except Exception as e:
	print('\n!!!')
	print(str(e))
	print('\n')
	input("Press ENTER to close the program")
	quit()

try:
	cwd.cwd_exec()
	print('(vegetation component 3 of 6) cwd computation successful')
	print('cwd.csv created\n')

except Exception as e:
	print('\n!!!')
	print(str(e))
	print('\n')
	input("Press ENTER to close the program")
	quit()


try:
	tbd_biggerplot.tbd_biggerplot_exec()
	print('(vegetation component 4 of 6) tree and root (big plot) computation successful')
	print('treeandRootBiomass_summary_biggerplot.csv created\n')

except Exception as e:
	print('\n!!!')
	print(str(e))
	print('\n')
	input("Press ENTER to close the program")
	quit()


try:
	tbd_mainplot.tbd_mainplot_exec()
	print('(vegetation component 5 of 6) tree and root (main plot) computation successful')
	print('treeandRootBiomass_summary_mainplot.csv created\n')

except Exception as e:
	print('\n!!!')
	print(str(e))
	print('\n')
	input("Press ENTER to close the program")
	quit()

try:
	soils.soils_exec()
	print('(vegetation component 6 of 6) soils computation successful')
	print('soils_AllPlotsSummary.csv created\n')

except Exception as e:
	print('\n!!!')
	print(str(e))
	print('\n')
	input("Press ENTER to close the program")
	quit()


print('\n\n!!! vegetation computed successfuly')
print('!!! creating summary files (biomass, c stored, co2)  (FINAL_vegetation_summary.csv)\n\n')





################################################
# create a summary file from all other csv files
################################################

lowStandType=[]
mediumStandType=[]
highStandType=[]
fname='./inputs/standType.csv'

with open(fname, 'r+') as in_config:
	reader = csv.reader(in_config, delimiter=',')
	next(reader)
	for row in reader:
		if(str(row[1]).lower() == 'low'):
			lowStandType.append(row[0])
		elif(str(row[1]).lower() == 'medium'):
			mediumStandType.append(row[0])
		elif(str(row[1]).lower() == 'high'):
			highStandType.append(row[0])


###############################################
#cwd
###############################################

cwdBiomass=[]
cwdCStored=[]
cwdCO2=[]

fname='./outputs/percomponent/cwd.csv'
index=0

with open(fname, 'r+') as in_config:
	reader = csv.reader(in_config, delimiter=',')
	next(reader)
	next(reader)
	next(reader)
	for row in reader:
		cwdBiomass.append(float(row[1]))
		cwdCStored.append(float(row[2]))
		cwdCO2.append(float(row[3]))
		index+=1

cwdBiomassLowAverage=0
cwdBiomassMediumAverage=0
cwdBiomassHighAverage=0

cwdCStoredLowAverage=0
cwdCStoredMediumAverage=0
cwdCStoredHighAverage=0

cwdCO2LowAverage=0
cwdCO2MediumAverage=0
cwdCO2HighAverage=0

counter=0
for item in lowStandType:
	cwdBiomassLowAverage+=cwdBiomass[int(item)-1]
	cwdCStoredLowAverage+=cwdCStored[int(item)-1]
	cwdCO2LowAverage+=cwdCO2[int(item)-1]
	counter+=1
cwdBiomassLowAverage=cwdBiomassLowAverage/counter
cwdCStoredLowAverage=cwdCStoredLowAverage/counter
cwdCO2LowAverage=cwdCO2LowAverage/counter


counter=0
for item in mediumStandType:
	cwdBiomassMediumAverage+=cwdBiomass[int(item)-1]
	cwdCStoredMediumAverage+=cwdCStored[int(item)-1]
	cwdCO2MediumAverage+=cwdCO2[int(item)-1]
	counter+=1
cwdBiomassMediumAverage=cwdBiomassMediumAverage/counter
cwdCStoredMediumAverage=cwdCStoredMediumAverage/counter
cwdCO2MediumAverage=cwdCO2MediumAverage/counter

counter=0
for item in highStandType:
	cwdBiomassHighAverage+=cwdBiomass[int(item)-1]
	cwdCStoredHighAverage+=cwdCStored[int(item)-1]
	cwdCO2HighAverage+=cwdCO2[int(item)-1]
	counter+=1
cwdBiomassHighAverage=cwdBiomassHighAverage/counter
cwdCStoredHighAverage=cwdCStoredHighAverage/counter
cwdCO2HighAverage=cwdCO2HighAverage/counter



###############################################
#end of cwd
#
#tree and root
###############################################

treeBiomass=[]
treeCStored=[]
treeCO2=[]

rootBiomass=[]
rootCStored=[]
rootCO2=[]


fname='./outputs/percomponent/treeandRootBiomass_summary_biggerplot.csv'
index=0

with open(fname, 'r+') as in_config:
	reader = csv.reader(in_config, delimiter=',')
	next(reader)
	next(reader)
	next(reader)

	for row in reader:
		rootBiomass.append(float(row[4]))
		rootCStored.append(float(row[5]))
		rootCO2.append(float(row[6]))

		treeBiomass.append(float(row[1]))
		treeCStored.append(float(row[2]))
		treeCO2.append(float(row[3]))


		index+=1

biggerTreeBiomassLowAverage=0
biggerTreeBiomassMediumAverage=0
biggerTreeBiomassHighAverage=0

biggerRootBiomassLowAverage=0
biggerRootBiomassMediumAverage=0
biggerRootBiomassHighAverage=0

biggerTreeCStoredLowAverage=0
biggerTreeCStoredMediumAverage=0
biggerTreeCStoredHighAverage=0

biggerRootCStoredLowAverage=0
biggerRootCStoredMediumAverage=0
biggerRootCStoredHighAverage=0


biggerTreeCO2LowAverage=0
biggerTreeCO2MediumAverage=0
biggerTreeCO2HighAverage=0

biggerRootCO2LowAverage=0
biggerRootCO2MediumAverage=0
biggerRootCO2HighAverage=0


counter=0
for item in lowStandType:
	biggerTreeBiomassLowAverage+=treeBiomass[int(item)-1]
	biggerRootBiomassLowAverage+=rootBiomass[int(item)-1]

	biggerTreeCStoredLowAverage+=treeCStored[int(item)-1]
	biggerRootCStoredLowAverage+=rootCStored[int(item)-1]
	
	biggerTreeCO2LowAverage+=treeCO2[int(item)-1]
	biggerRootCO2LowAverage+=rootCO2[int(item)-1]

	counter+=1

biggerTreeBiomassLowAverage=biggerTreeBiomassLowAverage/counter
biggerRootBiomassLowAverage=biggerRootBiomassLowAverage/counter

biggerTreeCStoredLowAverage=biggerTreeCStoredLowAverage/counter
biggerRootCStoredLowAverage=biggerRootCStoredLowAverage/counter

biggerTreeCO2LowAverage=biggerTreeCO2LowAverage/counter
biggerRootCO2LowAverage=biggerRootCO2LowAverage/counter



counter=0
for item in mediumStandType:
	biggerTreeBiomassMediumAverage+=treeBiomass[int(item)-1]
	biggerRootBiomassMediumAverage+=rootBiomass[int(item)-1]

	biggerTreeCStoredMediumAverage+=treeCStored[int(item)-1]
	biggerRootCStoredMediumAverage+=rootCStored[int(item)-1]
	
	biggerTreeCO2MediumAverage+=treeCO2[int(item)-1]
	biggerRootCO2MediumAverage+=rootCO2[int(item)-1]

	counter+=1

biggerTreeBiomassMediumAverage=biggerTreeBiomassMediumAverage/counter
biggerRootBiomassMediumAverage=biggerRootBiomassMediumAverage/counter

biggerTreeCStoredMediumAverage=biggerTreeCStoredMediumAverage/counter
biggerRootCStoredMediumAverage=biggerRootCStoredMediumAverage/counter

biggerTreeCO2MediumAverage=biggerTreeCO2MediumAverage/counter
biggerRootCO2MediumAverage=biggerRootCO2MediumAverage/counter



counter=0
for item in highStandType:
	biggerTreeBiomassHighAverage+=treeBiomass[int(item)-1]
	biggerRootBiomassHighAverage+=rootBiomass[int(item)-1]

	biggerTreeCStoredHighAverage+=treeCStored[int(item)-1]
	biggerRootCStoredHighAverage+=rootCStored[int(item)-1]
	
	biggerTreeCO2HighAverage+=treeCO2[int(item)-1]
	biggerRootCO2HighAverage+=rootCO2[int(item)-1]

	counter+=1

biggerTreeBiomassHighAverage=biggerTreeBiomassHighAverage/counter
biggerRootBiomassHighAverage=biggerRootBiomassHighAverage/counter

biggerTreeCStoredHighAverage=biggerTreeCStoredHighAverage/counter
biggerRootCStoredHighAverage=biggerRootCStoredHighAverage/counter

biggerTreeCO2HighAverage=biggerTreeCO2HighAverage/counter
biggerRootCO2HighAverage=biggerRootCO2HighAverage/counter



#mainplot

treeBiomass=[]
treeCStored=[]
treeCO2=[]

rootBiomass=[]
rootCStored=[]
rootCO2=[]


fname='./outputs/percomponent/treeandRootBiomass_summary_mainplot.csv'
index=0

with open(fname, 'r+') as in_config:
	reader = csv.reader(in_config, delimiter=',')
	next(reader)
	next(reader)
	next(reader)
	for row in reader:
		rootBiomass.append(float(row[4]))
		rootCStored.append(float(row[5]))
		rootCO2.append(float(row[6]))

		treeBiomass.append(float(row[1]))
		treeCStored.append(float(row[2]))
		treeCO2.append(float(row[3]))


		index+=1

mainTreeBiomassLowAverage=0
mainTreeBiomassMediumAverage=0
mainTreeBiomassHighAverage=0

mainRootBiomassLowAverage=0
mainRootBiomassMediumAverage=0
mainRootBiomassHighAverage=0

mainTreeCStoredLowAverage=0
mainTreeCStoredMediumAverage=0
mainTreeCStoredHighAverage=0

mainRootCStoredLowAverage=0
mainRootCStoredMediumAverage=0
mainRootCStoredHighAverage=0


mainTreeCO2LowAverage=0
mainTreeCO2MediumAverage=0
mainTreeCO2HighAverage=0

mainRootCO2LowAverage=0
mainRootCO2MediumAverage=0
mainRootCO2HighAverage=0


counter=0
for item in lowStandType:
	mainTreeBiomassLowAverage+=treeBiomass[int(item)-1]
	mainRootBiomassLowAverage+=rootBiomass[int(item)-1]

	mainTreeCStoredLowAverage+=treeCStored[int(item)-1]
	mainRootCStoredLowAverage+=rootCStored[int(item)-1]
	
	mainTreeCO2LowAverage+=treeCO2[int(item)-1]
	mainRootCO2LowAverage+=rootCO2[int(item)-1]

	counter+=1

mainTreeBiomassLowAverage=mainTreeBiomassLowAverage/counter
mainRootBiomassLowAverage=mainRootBiomassLowAverage/counter

mainTreeCStoredLowAverage=mainTreeCStoredLowAverage/counter
mainRootCStoredLowAverage=mainRootCStoredLowAverage/counter

mainTreeCO2LowAverage=mainTreeCO2LowAverage/counter
mainRootCO2LowAverage=mainRootCO2LowAverage/counter



counter=0
for item in mediumStandType:
	mainTreeBiomassMediumAverage+=treeBiomass[int(item)-1]
	mainRootBiomassMediumAverage+=rootBiomass[int(item)-1]

	mainTreeCStoredMediumAverage+=treeCStored[int(item)-1]
	mainRootCStoredMediumAverage+=rootCStored[int(item)-1]
	
	mainTreeCO2MediumAverage+=treeCO2[int(item)-1]
	mainRootCO2MediumAverage+=rootCO2[int(item)-1]

	counter+=1

mainTreeBiomassMediumAverage=mainTreeBiomassMediumAverage/counter
mainRootBiomassMediumAverage=mainRootBiomassMediumAverage/counter

mainTreeCStoredMediumAverage=mainTreeCStoredMediumAverage/counter
mainRootCStoredMediumAverage=mainRootCStoredMediumAverage/counter

mainTreeCO2MediumAverage=mainTreeCO2MediumAverage/counter
mainRootCO2MediumAverage=mainRootCO2MediumAverage/counter


counter=0
for item in highStandType:
	mainTreeBiomassHighAverage+=treeBiomass[int(item)-1]
	mainRootBiomassHighAverage+=rootBiomass[int(item)-1]

	mainTreeCStoredHighAverage+=treeCStored[int(item)-1]
	mainRootCStoredHighAverage+=rootCStored[int(item)-1]
	
	mainTreeCO2HighAverage+=treeCO2[int(item)-1]
	mainRootCO2HighAverage+=rootCO2[int(item)-1]

	counter+=1

mainTreeBiomassHighAverage=mainTreeBiomassHighAverage/counter
mainRootBiomassHighAverage=mainRootBiomassHighAverage/counter

mainTreeCStoredHighAverage=mainTreeCStoredHighAverage/counter
mainRootCStoredHighAverage=mainRootCStoredHighAverage/counter

mainTreeCO2HighAverage=mainTreeCO2HighAverage/counter
mainRootCO2HighAverage=mainRootCO2HighAverage/counter



###############################################
#end of tree and root
#
#necromass
###############################################

necromassBiomass=[]
necromassCStored=[]
necromassCO2=[]

fname='./outputs/percomponent/necromass.csv'
index=0

with open(fname, 'r+') as in_config:
	reader = csv.reader(in_config, delimiter=',')
	next(reader)
	next(reader)
	next(reader)
	for row in reader:
		necromassBiomass.append(float(row[2]))
		necromassCStored.append(float(row[3]))
		necromassCO2.append(float(row[4]))
		index+=1

necromassBiomassLowAverage=0
necromassBiomassMediumAverage=0
necromassBiomassHighAverage=0

necromassCStoredLowAverage=0
necromassCStoredMediumAverage=0
necromassCStoredHighAverage=0

necromassCO2LowAverage=0
necromassCO2MediumAverage=0
necromassCO2HighAverage=0


counter=0
for item in lowStandType:
	necromassBiomassLowAverage+=necromassBiomass[int(item)-1]
	necromassCStoredLowAverage+=necromassCStored[int(item)-1]
	necromassCO2LowAverage+=necromassCO2[int(item)-1]
	counter+=1
necromassBiomassLowAverage=necromassBiomassLowAverage/counter
necromassCStoredLowAverage=necromassCStoredLowAverage/counter
necromassCO2LowAverage=necromassCO2LowAverage/counter


counter=0
for item in mediumStandType:
	necromassBiomassMediumAverage+=necromassBiomass[int(item)-1]
	necromassCStoredMediumAverage+=necromassCStored[int(item)-1]
	necromassCO2MediumAverage+=necromassCO2[int(item)-1]
	counter+=1
necromassBiomassMediumAverage=necromassBiomassMediumAverage/counter
necromassCStoredMediumAverage=necromassCStoredMediumAverage/counter
necromassCO2MediumAverage=necromassCO2MediumAverage/counter

counter=0
for item in highStandType:
	necromassBiomassHighAverage+=necromassBiomass[int(item)-1]
	necromassCStoredHighAverage+=necromassCStored[int(item)-1]
	necromassCO2HighAverage+=necromassCO2[int(item)-1]
	counter+=1
necromassBiomassHighAverage=necromassBiomassHighAverage/counter
necromassCStoredHighAverage=necromassCStoredHighAverage/counter
necromassCO2HighAverage=necromassCO2HighAverage/counter

###############################################
#end of necromass
#
#understorey
###############################################


understoreyBiomass=[]
understoreyCStored=[]
understoreyCO2=[]

fname='./outputs/percomponent/understorey.csv'
index=0

with open(fname, 'r+') as in_config:
	reader = csv.reader(in_config, delimiter=',')
	next(reader)
	next(reader)
	next(reader)
	for row in reader:
		understoreyBiomass.append(float(row[2]))
		understoreyCStored.append(float(row[3]))
		understoreyCO2.append(float(row[4]))
		index+=1

understoreyBiomassLowAverage=0
understoreyBiomassMediumAverage=0
understoreyBiomassHighAverage=0

understoreyCStoredLowAverage=0
understoreyCStoredMediumAverage=0
understoreyCStoredHighAverage=0


understoreyCO2LowAverage=0
understoreyCO2MediumAverage=0
understoreyCO2HighAverage=0


counter=0
for item in lowStandType:
	understoreyBiomassLowAverage+=understoreyBiomass[int(item)-1]
	understoreyCStoredLowAverage+=understoreyCStored[int(item)-1]
	understoreyCO2LowAverage+=understoreyCO2[int(item)-1]
	counter+=1
understoreyBiomassLowAverage=understoreyBiomassLowAverage/counter
understoreyCStoredLowAverage=understoreyCStoredLowAverage/counter
understoreyCO2LowAverage=understoreyCO2LowAverage/counter


counter=0
for item in mediumStandType:
	understoreyBiomassMediumAverage+=understoreyBiomass[int(item)-1]
	understoreyCStoredMediumAverage+=understoreyCStored[int(item)-1]
	understoreyCO2MediumAverage+=understoreyCO2[int(item)-1]
	counter+=1
understoreyBiomassMediumAverage=understoreyBiomassMediumAverage/counter
understoreyCStoredMediumAverage=understoreyCStoredMediumAverage/counter
understoreyCO2MediumAverage=understoreyCO2MediumAverage/counter

counter=0
for item in highStandType:
	understoreyBiomassHighAverage+=understoreyBiomass[int(item)-1]
	understoreyCStoredHighAverage+=understoreyCStored[int(item)-1]
	understoreyCO2HighAverage+=understoreyCO2[int(item)-1]
	counter+=1
understoreyBiomassHighAverage=understoreyBiomassHighAverage/counter
understoreyCStoredHighAverage=understoreyCStoredHighAverage/counter
understoreyCO2HighAverage=understoreyCO2HighAverage/counter


###############################################
#end of understorey
#soilMarker
#soils
###############################################


soilCO2=[]
soilCStored=[]

soilCO2LowAverage=0
soilCO2MediumAverage=0
soilCO2HighAverage=0

soilCStoredLowAverage=0
soilCStoredMediumAverage=0
soilCStoredHighAverage=0

fname='./outputs/percomponent/soils_AllPlotsSummary.csv'
index=0
counter=0

with open(fname, 'r+') as in_config:
	reader = csv.reader(in_config, delimiter=',')
	next(reader)
	next(reader)
	next(reader)
	for row in reader:
		soilCO2.append(float(row[2]))
		soilCStored.append(float(row[1]))
		index+=1

for item in lowStandType:

	soilCO2LowAverage+=soilCO2[int(item)-1]
	soilCStoredLowAverage+=soilCStored[int(item)-1]
	counter+=1

soilCO2LowAverage=soilCO2LowAverage/counter
soilCStoredLowAverage=soilCStoredLowAverage/counter

counter=0
for item in mediumStandType:
	soilCO2MediumAverage+=soilCO2[int(item)-1]
	soilCStoredMediumAverage+=soilCStored[int(item)-1]
	counter+=1

soilCO2MediumAverage=soilCO2MediumAverage/counter
soilCStoredMediumAverage=soilCStoredMediumAverage/counter

counter=0
for item in highStandType:
	soilCO2HighAverage+=soilCO2[int(item)-1]
	soilCStoredHighAverage+=soilCStored[int(item)-1]
	counter+=1

soilCO2HighAverage=soilCO2HighAverage/counter
soilCStoredHighAverage=soilCStoredHighAverage/counter

soilCO2 = soilCO2LowAverage + soilCO2MediumAverage + soilCO2HighAverage
soilCStored = soilCStoredLowAverage + soilCStoredMediumAverage + soilCStoredHighAverage


	
totalmainTreeBiomass=(mainTreeBiomassLowAverage+mainTreeBiomassMediumAverage+mainTreeBiomassHighAverage)/3
totalbiggerTreeBiomass=(biggerTreeBiomassLowAverage+biggerTreeBiomassMediumAverage+biggerTreeBiomassHighAverage)/3
totalunderstoreyBiomass=(understoreyBiomassLowAverage+understoreyBiomassMediumAverage+understoreyBiomassHighAverage)/3
totalnecromassBiomass=(necromassBiomassLowAverage+necromassBiomassMediumAverage+necromassBiomassHighAverage)/3
totalcwdBiomass=(cwdBiomassLowAverage+cwdBiomassMediumAverage+cwdBiomassHighAverage)/3
totalmainRootBiomass=(mainRootBiomassLowAverage+mainRootBiomassMediumAverage+mainRootBiomassHighAverage)/3
totalbiggerRootBiomass=(biggerRootBiomassLowAverage+biggerRootBiomassMediumAverage+biggerRootBiomassHighAverage)/3
biograndTotal=totalmainTreeBiomass+totalbiggerTreeBiomass+totalunderstoreyBiomass+totalnecromassBiomass+totalcwdBiomass+totalmainRootBiomass+totalbiggerRootBiomass


#######################################################################################################################
wb = Workbook()
ws0 = wb.add_sheet('SUMMARY')


fnt = Font()
fnt.bold = True

borders = Borders()
borders.bottom = 0x0052

topborder = Borders()
topborder.top = 0x0052


style = XFStyle()
style.font = fnt
	
style2 = XFStyle()
style2.borders = borders

style3 =XFStyle()
style3.borders = topborder


decimal_style = XFStyle()
decimal_style.num_format_str = '0.00'


decimal_style2 = XFStyle()
decimal_style2.num_format_str = '0.00'
decimal_style2.font = fnt

headerStyle = "font: bold on; align: horiz center, vert center "


ws0.col(0).width = 10000
ws0.col(1).width = 3000
ws0.col(2).width = 3000
ws0.col(3).width = 3000
ws0.col(4).width = 3000
ws0.col(5).width = 3000
ws0.col(6).width = 3000
ws0.col(7).width = 3000
ws0.col(8).width = 3000
ws0.col(9).width = 3000
ws0.col(10).width = 3000


ws0.write_merge(0, 3, 0, 0, 'CARBON POOLS',  easyxf(headerStyle))
ws0.write_merge(0, 0, 1, 9, 'Stand Composition/Density',  easyxf(headerStyle))
ws0.write_merge(1, 1, 1, 3, 'High',  easyxf(headerStyle))
ws0.write_merge(1, 1, 4, 6, 'Medium',  easyxf(headerStyle))
ws0.write_merge(1, 1, 7, 9, 'Low',  easyxf(headerStyle))
ws0.write_merge(19, 19, 0, 10, '', style2)
ws0.write_merge(4, 4, 0, 10, '', style3)


ws0.write(2,1,'BIOMASS', easyxf(headerStyle))
ws0.write(2,2,'C STORED', easyxf(headerStyle))
ws0.write(2,3,'CO2', easyxf(headerStyle))

ws0.write(2,4,'BIOMASS', easyxf(headerStyle))
ws0.write(2,5,'C STORED', easyxf(headerStyle))
ws0.write(2,6,'CO2', easyxf(headerStyle))

ws0.write(2,7,'BIOMASS', easyxf(headerStyle))
ws0.write(2,8,'C STORED', easyxf(headerStyle))
ws0.write(2,9,'CO2', easyxf(headerStyle))

ws0.write(3,1,'(Mg ha-1)', easyxf(headerStyle))
ws0.write(3,2,'(Mg ha-1)', easyxf(headerStyle))
ws0.write(3,3,'(Mg ha-1)', easyxf(headerStyle))

ws0.write(3,4,'(Mg ha-1)', easyxf(headerStyle))
ws0.write(3,5,'(Mg ha-1)', easyxf(headerStyle))
ws0.write(3,6,'(Mg ha-1)', easyxf(headerStyle))

ws0.write(3,7,'(Mg ha-1)', easyxf(headerStyle))
ws0.write(3,8,'(Mg ha-1)', easyxf(headerStyle))
ws0.write(3,9,'(Mg ha-1)', easyxf(headerStyle))

ws0.write(1,10,'AVERAGE', easyxf(headerStyle))
ws0.write(2,10,'Total', easyxf(headerStyle))
ws0.write(3,10,'(Mg ha-1)', easyxf(headerStyle))

ws0.write(5,0,'TREE BIOMASS',style)
ws0.write(6,0,'     Small Plot')
ws0.write(7,0,'     Big Plot')
ws0.write(8,0,'Sub Total',style)
ws0.write(10,0,'UNDERSTOREY',style)
ws0.write(11,0,'NECRO/LITTER',style)
ws0.write(12,0,'COARSE WOODY DEBRIS (CWD)',style)
ws0.write(13,0,'ROOTS',style)
ws0.write(14,0,'     Small Plot')
ws0.write(15,0,'     Big Plot')
ws0.write(16,0,'Sub-Total',style)
ws0.write(18,0,'Soil',style)
ws0.write(20,0,'TOTAL',style)
ws0.write(21,0,'Biomass Density',style)
ws0.write(22,0,'C Stored',style)
ws0.write(23,0,'CO2',style)


ws0.write(6,1,mainTreeBiomassHighAverage,decimal_style)
ws0.write(6,2,mainTreeCStoredHighAverage,decimal_style)
ws0.write(6,3,mainTreeCO2HighAverage,decimal_style)

ws0.write(6,4,mainTreeBiomassMediumAverage,decimal_style)
ws0.write(6,5,mainTreeCStoredMediumAverage,decimal_style)
ws0.write(6,6,mainTreeCO2MediumAverage,decimal_style)

ws0.write(6,7,mainTreeBiomassLowAverage,decimal_style)
ws0.write(6,8,mainTreeCStoredLowAverage,decimal_style)
ws0.write(6,9,mainTreeCO2LowAverage,decimal_style)

ws0.write(7,1,biggerTreeBiomassHighAverage,decimal_style)
ws0.write(7,2,biggerTreeCStoredHighAverage,decimal_style)
ws0.write(7,3,biggerTreeCO2HighAverage,decimal_style)

ws0.write(7,4,biggerTreeBiomassMediumAverage,decimal_style)
ws0.write(7,5,biggerTreeCStoredMediumAverage,decimal_style)
ws0.write(7,6,biggerTreeCO2MediumAverage,decimal_style)

ws0.write(7,7,biggerTreeBiomassLowAverage,decimal_style)
ws0.write(7,8,biggerTreeCStoredLowAverage,decimal_style)
ws0.write(7,9,biggerTreeCO2LowAverage,decimal_style)


ws0.write(8, 1, Formula("B7+B8"),decimal_style)
ws0.write(8, 2, Formula("c7+c8"),decimal_style)
ws0.write(8, 3, Formula("d7+d8"),decimal_style)
ws0.write(8, 4, Formula("e7+e8"),decimal_style)
ws0.write(8, 5, Formula("f7+f8"),decimal_style)
ws0.write(8, 6, Formula("g7+g8"),decimal_style)

ws0.write(8, 7, Formula("h7+h8"),decimal_style)
ws0.write(8, 8, Formula("i7+i8"),decimal_style)
ws0.write(8, 9, Formula("j7+j8"),decimal_style)


ws0.write(10,1,understoreyBiomassHighAverage,decimal_style)
ws0.write(10,2,understoreyCStoredHighAverage,decimal_style)
ws0.write(10,3,understoreyCO2HighAverage,decimal_style)

ws0.write(10,4,understoreyBiomassMediumAverage,decimal_style)
ws0.write(10,5,understoreyCStoredMediumAverage,decimal_style)
ws0.write(10,6,understoreyCO2MediumAverage,decimal_style)

ws0.write(10,7,understoreyBiomassLowAverage,decimal_style)
ws0.write(10,8,understoreyCStoredLowAverage,decimal_style)
ws0.write(10,9,understoreyCO2LowAverage,decimal_style)



ws0.write(11,1,necromassBiomassHighAverage,decimal_style)
ws0.write(11,2,necromassCStoredHighAverage,decimal_style)
ws0.write(11,3,necromassCO2HighAverage,decimal_style)

ws0.write(11,4,necromassBiomassMediumAverage,decimal_style)
ws0.write(11,5,necromassCStoredMediumAverage,decimal_style)
ws0.write(11,6,necromassCO2MediumAverage,decimal_style)

ws0.write(11,7,necromassBiomassLowAverage,decimal_style)
ws0.write(11,8,necromassCStoredLowAverage,decimal_style)
ws0.write(11,9,necromassCO2LowAverage,decimal_style)


ws0.write(12,1,cwdBiomassHighAverage,decimal_style)
ws0.write(12,2,cwdCStoredHighAverage,decimal_style)
ws0.write(12,3,cwdCO2HighAverage,decimal_style)

ws0.write(12,4,cwdBiomassMediumAverage,decimal_style)
ws0.write(12,5,cwdCStoredMediumAverage,decimal_style)
ws0.write(12,6,cwdCO2MediumAverage,decimal_style)

ws0.write(12,7,cwdBiomassLowAverage,decimal_style)
ws0.write(12,8,cwdCStoredLowAverage,decimal_style)
ws0.write(12,9,cwdCO2LowAverage,decimal_style)

ws0.write(14,1,mainRootBiomassHighAverage,decimal_style)
ws0.write(14,2,mainRootCStoredHighAverage,decimal_style)
ws0.write(14,3,mainRootCO2HighAverage,decimal_style)

ws0.write(14,4,mainRootBiomassMediumAverage,decimal_style)
ws0.write(14,5,mainRootCStoredMediumAverage,decimal_style)
ws0.write(14,6,mainRootCO2MediumAverage,decimal_style)

ws0.write(14,7,mainRootBiomassLowAverage,decimal_style)
ws0.write(14,8,mainRootCStoredLowAverage,decimal_style)
ws0.write(14,9,mainRootCO2LowAverage,decimal_style)


ws0.write(15,1,biggerRootBiomassHighAverage,decimal_style)
ws0.write(15,2,biggerRootCStoredHighAverage,decimal_style)
ws0.write(15,3,biggerRootCO2HighAverage,decimal_style)

ws0.write(15,4,biggerRootBiomassMediumAverage,decimal_style)
ws0.write(15,5,biggerRootCStoredMediumAverage,decimal_style)
ws0.write(15,6,biggerRootCO2MediumAverage,decimal_style)

ws0.write(15,7,biggerRootBiomassLowAverage,decimal_style)
ws0.write(15,8,biggerRootCStoredLowAverage,decimal_style)
ws0.write(15,9,biggerRootCO2LowAverage,decimal_style)


ws0.write(16, 1, Formula("B15+B16"),decimal_style)
ws0.write(16, 2, Formula("C15+C16"),decimal_style)
ws0.write(16, 3, Formula("D15+D16"),decimal_style)

ws0.write(16, 4, Formula("E15+E16"),decimal_style)
ws0.write(16, 5, Formula("F15+F16"),decimal_style)
ws0.write(16, 6, Formula("G15+G16"),decimal_style)

ws0.write(16, 7, Formula("H15+H16"),decimal_style)
ws0.write(16, 8, Formula("I15+I16"),decimal_style)
ws0.write(16, 9, Formula("J15+J16"),decimal_style)


ws0.write(18,2,soilCStoredHighAverage,decimal_style)
ws0.write(18,3,soilCO2HighAverage,decimal_style)

ws0.write(18,5,soilCStoredMediumAverage,decimal_style)
ws0.write(18,6,soilCO2MediumAverage,decimal_style)

ws0.write(18,8,soilCStoredLowAverage,decimal_style)
ws0.write(18,9,soilCO2LowAverage,decimal_style)

ws0.write(21,1,Formula("B9+B11+B12+B13+B17+B19"),decimal_style)
ws0.write(22,2,Formula("C9+C11+C12+C13+C17+C19"),decimal_style)
ws0.write(23,3,Formula("D9+D11+D12+D13+D17+D19"),decimal_style)

ws0.write(21,4,Formula("E9+E11+E12+E13+E17+E19"),decimal_style)
ws0.write(22,5,Formula("F9+F11+F12+F13+F17+F19"),decimal_style)
ws0.write(23,6,Formula("G9+G11+G12+G13+G17+G19"),decimal_style)

ws0.write(21,7,Formula("H9+H11+H12+H13+H17+H19"),decimal_style)
ws0.write(22,8,Formula("I9+I11+I12+I13+I17+I19"),decimal_style)
ws0.write(23,9,Formula("J9+J11+J12+J13+J17+J19"),decimal_style)

ws0.write(21,10,Formula("(B22+E22+H22)/3"),decimal_style2)
ws0.write(22,10,Formula("(C23+F23+I23)/3"),decimal_style2)
ws0.write(23,10,Formula("(D24+G24+J24)/3"),decimal_style2)

wb.save('./outputs/FINAL_vegetation_summary.xls')	

#######################################################################################################################




##########################
# call emissions vegetation components #
#emissionmarker
##########################


try:
	fugitiveEmission.fugitiveEmission_exec()
	print('(emission scope 1 of 4) fugitive emission computation successful')
	print('scope1_fugitiveEmission.csv created\n')

except Exception as e:
	print('\n!!!')
	print(str(e))
	print('\n')
	input("Press ENTER to close the program")
	quit()

try:
	fuel.fuel_exec()
	print('(emission scope 1 of 4) fuel computation successful')
	print('scope1_fuel.csv created\n')

except Exception as e:
	print('\n!!!')
	print(str(e))
	print('\n')
	input("Press ENTER to close the program")
	quit()


try:
	electricity.electricity_exec()
	print('(emission scope 2 of 4) electricity computation successful')
	print('scope2_electricity.csv created\n')

except Exception as e:
	print('\n!!!')
	print(str(e))
	print('\n')
	input("Press ENTER to close the program")
	quit()	


try:
	airTravel.airTravel_exec()
	print('(emission scope 3 of 4) air travel computation successful')
	print('scope3_airTravel.csv created\n')

except Exception as e:
	print('\n!!!')
	print(str(e))
	print('\n')
	input("Press ENTER to close the program")
	quit()	

try:
	iclei_array= []
	iclei_array= iclei.iclei_exec()
	print('(emission scope 3 of 4) iclei computation successful')

except Exception as e:
	print('\n!!!')
	print(str(e))
	print('\n')
	input("Press ENTER to close the program")
	quit()	

try:
	powerRented.powerRented_exec()
	print('power rented computation successful')
	print('scope3_powerRented.csv created\n')

except Exception as e:
	print('\n!!!')
	print(str(e))
	print('\n')
	input("Press ENTER to close the program")
	quit()	


try:
	lpgIssuance.lpgIssuance_exec()
	print('(emission scope 3 of 4) lpg issuance computation successful')
	print('scope3_lpg.csv created\n')

except Exception as e:
	print('\n!!!')
	print(str(e))
	print('\n')
	input("Press ENTER to close the program")
	quit()	


try:
	landConversion.landcover_exec(biograndTotal)
	print('(emission scope 4 of 4) land conversion computation successful')
	print('scope4_landconversion.csv created\n')

except Exception as e:
	print('\n!!!')
	print(str(e))
	print('\n')
	input("Press ENTER to close the program")
	quit()


try:
	averageTreeBiomass=((mainTreeBiomassHighAverage+mainRootBiomassLowAverage+mainTreeBiomassMediumAverage)/3) + ((biggerTreeBiomassHighAverage+biggerRootBiomassLowAverage+biggerTreeBiomassMediumAverage)/3) 
	averageUnderstoreyBiomass=(understoreyBiomassHighAverage+understoreyBiomassMediumAverage+understoreyBiomassLowAverage)/3
	averageNecroBiomass=(necromassBiomassHighAverage+necromassBiomassMediumAverage+necromassBiomassLowAverage)/3
	averageCwdBiomass=(cwdBiomassLowAverage+cwdBiomassMediumAverage+cwdBiomassHighAverage)/3
	forestFire.forestFire_exec(averageTreeBiomass,averageUnderstoreyBiomass,averageNecroBiomass,averageCwdBiomass)
	print('(emission scope 4 of 4) forest fire computation successful')
	print('scope4_forestFire.csv created\n')

except Exception as e:
	print('\n!!!')
	print(str(e))
	print('\n')
	input("\rPress ENTER to close the program")
	quit()	


print('\n\n!!! emission computed successfuly')

#total emissions
fuelEmission = 0


fugitiveEmission = 0

fname='./outputs/percomponent/scope1_fuel.csv'

with open(fname, 'r+') as in_config:
	reader = csv.reader(in_config, delimiter=',')
	for x in range(0,12):
		next(reader)
	row = next(reader)
	fuelEmission = row[1]

fname='./outputs/percomponent/scope1_fugitiveEmission.csv'

with open(fname, 'r+') as in_config:
	reader = csv.reader(in_config, delimiter=',')
	next(reader)
	next(reader)
	next(reader)
	for row in reader:
		fugitiveEmission += float(row[5])


fname='./outputs/percomponent/scope2_electricity.csv'

with open(fname, 'r+') as in_config:
	reader = csv.reader(in_config, delimiter=',')
	for row in range(0,20):
		next(reader)
	for row in reader:
		electricity = float(row[1])


fname='./outputs/percomponent/scope3_airTravel.csv'


airTravelEmission = 0

with open(fname, 'r+') as in_config:
	reader = csv.reader(in_config, delimiter=',')
	for x in range(0,10):
		next(reader)
	row=next(reader)
	airTravelEmission = row[1]	

fname='./outputs/percomponent/scope3_lpg.csv'

lpgCO2 =0
lpgCH4 =0
lpgN2O =0

with open(fname, 'r+') as in_config:
	reader = csv.reader(in_config, delimiter=',')
	for x in range(0,6):
		next(reader)
	row=next(reader)
	lpgCO2 =float(row[2])/1000
	lpgCH4 =float(row[3])/1000
	lpgN2O =float(row[4])/1000


fname='./outputs/percomponent/scope3_powerRented.csv'

with open(fname, 'r+') as in_config:
	reader = csv.reader(in_config, delimiter=',')
	for x in range(0,11):
		next(reader)
	for row in reader:
		powerRented = float(row[3])
		

fname='./outputs/percomponent/scope4_forestFire.csv'

fireEmission =0 

with open(fname, 'r+') as in_config:
	reader = csv.reader(in_config, delimiter=',')
	for x in range(0,13):
		next(reader)
	row=next(reader)

	fireEmission= float(row[1])
	
fname='./outputs/percomponent/scope4_landconversion.csv'

landConversionEmission = 0

with open(fname, 'r+') as in_config:
	reader = csv.reader(in_config, delimiter=',')
	
	for x in range(0,10):
		next(reader)
	row= next(reader)
	landConversionEmission= float(row[1])

	
########################################################################
#
# emission summary
# emissionmarker
########################################################################

waterWaste= float(iclei_array[0])+float(iclei_array[1])+float(iclei_array[2])
solidWaste = iclei_array[3]
lpgTotal = lpgCO2+lpgCH4+lpgN2O

wb = Workbook()
ws0 = wb.add_sheet('SUMMARY')


fnt = Font()
fnt.bold = True

borders = Borders()
borders.bottom = 0x0052

style = XFStyle()
style.font = fnt
	
style2 = XFStyle()
style2.borders = borders


decimal_style = XFStyle()
decimal_style.num_format_str = '0.00'



headerStyle = "font: bold on; align: horiz center, vert center "


ws0.col(0).width = 10000
ws0.col(1).width = 6000
ws0.col(2).width = 6000
ws0.col(3).width = 3000
ws0.col(4).width = 3000
ws0.col(5).width = 3000
ws0.col(6).width = 3000
ws0.col(7).width = 3000
ws0.col(8).width = 3000
ws0.col(9).width = 3000
ws0.col(10).width = 3000


ws0.write(0,0,'EMISSION SOURCES', easyxf(headerStyle))

ws0.write(0,1,'TOTAL', easyxf(headerStyle))
ws0.write(0,2,'TOTAL', easyxf(headerStyle))
ws0.write(0,3,'% SHARE', easyxf(headerStyle))
ws0.write(0,4,'% SHARE', easyxf(headerStyle))

ws0.write(1,1,'CO2 EMISSIONS', easyxf(headerStyle))
ws0.write(1,2,'CO2 EMISSIONS', easyxf(headerStyle))
ws0.write(1,3,'PER', easyxf(headerStyle))
ws0.write(1,4,'PER', easyxf(headerStyle))

ws0.write(2,1,'(Mg) PER SOURCE', easyxf(headerStyle))
ws0.write(2,2,'(Mg) PER SOURCE', easyxf(headerStyle))
ws0.write(2,3,'SOURCE', easyxf(headerStyle))
ws0.write(2,4,'SCOPE', easyxf(headerStyle))

ws0.write_merge(3, 3, 0, 4, '', style3)

ws0.write(4,0,'SCOPE 1', style)
ws0.write(5,0,'   Fuel')
ws0.write(6,0,'   Fugitive Emission')

ws0.write(8,0,'SCOPE 2', style)
ws0.write(9,0,'   Electricity')

ws0.write(11,0,'SCOPE 3', style)
ws0.write(12,0,'   Air Travel')
ws0.write(13,0,'   Power Rented')
ws0.write(14,0,'   LPG Consumption')

ws0.write(15,0,'   Waste')
ws0.write(16,0,'      Solid Waste')
ws0.write(17,0,'      Waste Water (CH4)')

ws0.write(19,0,'SCOPE 4', style)
ws0.write(20,0,'   Annual Biomass Loss/Land-Use Conversion')
ws0.write(21,0,'   Forest Fire')

ws0.write_merge(22, 22, 0, 4, '', style2)

ws0.write(23,0,'TOTAL', easyxf(headerStyle))




ws0.write(5,1,float(fuelEmission),decimal_style)
ws0.write(6,1,float(fugitiveEmission),decimal_style)

ws0.write(9,1,float(electricity),decimal_style)

ws0.write(12,1,float(airTravelEmission),decimal_style)
ws0.write(13,1,float(powerRented),decimal_style)
ws0.write(14,1,float(lpgTotal),decimal_style)

ws0.write(16,1,float(waterWaste),decimal_style)
ws0.write(17,1,float(solidWaste),decimal_style)

#landConversionEmission , palitan muna ng 0
ws0.write(20,1,0,decimal_style)
ws0.write(21,1,float(fireEmission),decimal_style)

ws0.write(23,1,Formula('sum(b2:b22)'),decimal_style2)


totalEmission = float(fuelEmission) + float(fugitiveEmission) + float(electricity) + float(airTravelEmission) + float(powerRented) + float(lpgTotal) + float(waterWaste) + float(solidWaste) + float(landConversionEmission)  + float(fireEmission)


ws0.write(4,2,Formula('sum(b6:b7)'),decimal_style)

ws0.write(8,2,Formula('b10'),decimal_style)

ws0.write(11,2,Formula('sum(b13:b18)'),decimal_style)

ws0.write(19,2,Formula('sum(b21:b22)'),decimal_style)



ws0.write(5,3,Formula('(b6/b24)*100'),decimal_style)
ws0.write(6,3,Formula('(b7/b24)*100'),decimal_style)

ws0.write(9,3,Formula('(b10/b24)*100'),decimal_style)

ws0.write(12,3,Formula('(b13/b24)*100'),decimal_style)
ws0.write(13,3,Formula('(b14/b24)*100'),decimal_style)
ws0.write(14,3,Formula('(b15/b24)*100'),decimal_style)

ws0.write(16,3,Formula('(b17/b24)*100'),decimal_style)
ws0.write(17,3,Formula('(b18/b24)*100'),decimal_style)

ws0.write(20,3,Formula('(b21/b24)*100'),decimal_style)
ws0.write(21,3,Formula('(b22/b24)*100'),decimal_style)

ws0.write(23,3,Formula('sum(d5:d22)'),decimal_style)


ws0.write(4,4,Formula('(c5/b24)*100'),decimal_style)

ws0.write(8,4,Formula('(c9/b24)*100'),decimal_style)

ws0.write(11,4,Formula('(c12/b24)*100'),decimal_style)

ws0.write(19,4,Formula('(c20/b24)*100'),decimal_style)
ws0.write(23,4,Formula('sum(e5:e22)'),decimal_style)


wb.save('./outputs/FINAL_emission_summary.xls')	


highCO2Stored = biggerRootCO2HighAverage + mainRootCO2HighAverage + soilCO2HighAverage + biggerTreeCO2HighAverage + mainTreeCO2HighAverage + understoreyCO2HighAverage + cwdCO2HighAverage + necromassCO2HighAverage

mediumCO2Stored = biggerRootCO2MediumAverage + mainRootCO2MediumAverage + soilCO2MediumAverage + biggerTreeCO2MediumAverage + mainTreeCO2MediumAverage + understoreyCO2MediumAverage + cwdCO2MediumAverage + necromassCO2MediumAverage

lowCO2Stored = biggerRootCO2LowAverage + mainRootCO2LowAverage + soilCO2LowAverage + biggerTreeCO2LowAverage + mainTreeCO2LowAverage + understoreyCO2LowAverage + cwdCO2LowAverage + necromassCO2LowAverage

with open('./inputs/scope4/forestInfo.csv', 'r+') as in_csv:
	reader = csv.reader(in_csv, delimiter=',')
	next(reader)
	row=next(reader)
	forestAge=int(row[0])

fname='./inputs/areaPerStandType.csv'

areaPerStandType ={}
with open(fname, 'r+') as in_config:
	reader = csv.reader(in_config, delimiter=',')
	next(reader)
	for row in reader:
		areaPerStandType[row[0]] = float(row[1])

wb = Workbook()
ws0 = wb.add_sheet('SUMMARY')
ws0.col(0).width = 7000
ws0.col(1).width = 4000
ws0.col(2).width = 7000
ws0.col(3).width = 5000
ws0.col(4).width = 5000

ws0.write(0,0,'SEQUESTRATION POTENTIAL', easyxf(headerStyle))
ws0.write(1,0,'PER VEGETATION TYPE', easyxf(headerStyle))
ws0.write(1,1,'TOTAL AREA', easyxf(headerStyle))
ws0.write(1,2,'AMOUNT OF CO2e STORED', easyxf(headerStyle))
ws0.write(1,3,'TOTAL CO2e STORED', easyxf(headerStyle))

ws0.write(2,1,'(ha)', easyxf(headerStyle))
ws0.write(2,2,'(Mg/ha)', easyxf(headerStyle))

ws0.write_merge(3, 3, 0, 3, '', style3)
ws0.write(4,0,'HIGH', easyxf(headerStyle))
ws0.write(5,0,'MEDIUM', easyxf(headerStyle))
ws0.write(6,0,'LOW', easyxf(headerStyle))

ws0.write(4,1, areaPerStandType['high'], decimal_style)
ws0.write(5,1, areaPerStandType['medium'], decimal_style)
ws0.write(6,1, areaPerStandType['low'], decimal_style)

ws0.write(4,2, highCO2Stored, decimal_style)
ws0.write(5,2, mediumCO2Stored, decimal_style)
ws0.write(6,2, lowCO2Stored, decimal_style)

ws0.write(4,3, Formula('b5*c5'), decimal_style)
ws0.write(5,3, Formula('b6*c6'), decimal_style)
ws0.write(6,3, Formula('b7*c7'), decimal_style)
ws0.write_merge(7, 7, 0, 3, '', style2)

ws0.write(8,3, Formula('sum(d5:d7)'), decimal_style)




ws0.write(11,0,'SEQUESTRATION POTENTIAL', easyxf(headerStyle))
ws0.write(12,0,'PER VEGETATION TYPE', easyxf(headerStyle))
ws0.write(12,1,'TOTAL AREA', easyxf(headerStyle))
ws0.write(12,2,'AMOUNT OF CO2e STORED', easyxf(headerStyle))
ws0.write(12,3,'AMOUNT OF CO2e BUILDUP', easyxf(headerStyle))
ws0.write(12,4,'TOTAL CO2e STORED', easyxf(headerStyle))

ws0.write(13,1,'(ha)', easyxf(headerStyle))
ws0.write(13,2,'(Mg/ha)', easyxf(headerStyle))
ws0.write(13,3,'(Mg/ha/yr)', easyxf(headerStyle))

ws0.write_merge(14, 14, 0, 4, '', style3)
ws0.write(15,0,'HIGH', easyxf(headerStyle))
ws0.write(16,0,'MEDIUM', easyxf(headerStyle))
ws0.write(17,0,'LOW', easyxf(headerStyle))
ws0.write(19,0,'TOTAL SEQUESTRATION', easyxf(headerStyle))
ws0.write(20,0,'AVERAGE', easyxf(headerStyle))

ws0.write(15,1, areaPerStandType['high'], decimal_style)
ws0.write(16,1, areaPerStandType['medium'], decimal_style)
ws0.write(17,1, areaPerStandType['low'], decimal_style)

ws0.write(15,2, highCO2Stored, decimal_style)
ws0.write(16,2, mediumCO2Stored, decimal_style)
ws0.write(17,2, lowCO2Stored, decimal_style)

ws0.write(15,3, float(highCO2Stored / forestAge), decimal_style)
ws0.write(16,3, float(mediumCO2Stored / forestAge), decimal_style)
ws0.write(17,3, float(lowCO2Stored / forestAge), decimal_style)


ws0.write(15,4, Formula('d16 * b16'), decimal_style)
ws0.write(16,4, Formula('d17 * b17'), decimal_style)
ws0.write(17,4, Formula('d18 * b18'), decimal_style)

ws0.write_merge(18, 18, 0, 4, '', style2)

ws0.write(19,1, Formula('sum(b16:b18)'), decimal_style)
ws0.write(19,2, Formula('sum(c16:c18)'), decimal_style)
ws0.write(19,3, Formula('sum(d16:d18)'), decimal_style)
ws0.write(19,4, Formula('sum(e16:e18)'), decimal_style2)

ws0.write(20,2, Formula('average(c16:c18)'), decimal_style)
ws0.write(20,3, Formula('average(d16:d18)'), decimal_style)

ws0.write(21,3, 'TOTAL EMISSION', easyxf(headerStyle))
ws0.write(21,4, totalEmission, decimal_style2)

totalSequestrationHigh = float(highCO2Stored / forestAge)
totalSequestrationMedium = float(mediumCO2Stored / forestAge)
totalSequestrationLow = float(lowCO2Stored / forestAge)

totalSequestration = (totalSequestrationHigh * areaPerStandType['high']) + (totalSequestrationMedium * areaPerStandType['medium']) + (totalSequestrationLow * areaPerStandType['low']) 

ws0.write(22,3, 'NET SURPLUS', easyxf(headerStyle))
ws0.write(22,4, totalSequestration - totalEmission, decimal_style2)

wb.save('./outputs/FINAL_net_surplus.xls')	


print('\n\n!!! creating summary file (FINAL_emission_summary.csv)')

print('\n!!! PROGRAM COMPLETED SUCCESSFULLY !!!\n')

input("Press ENTER to close the program")