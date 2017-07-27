class ReadWrite():
	def read(self, fileName):
		"""
		Takes an ANC.out file name to be read and determines if the fuelPat
		passes the power and FDH criteria

		:type fileName: str
		The file to be read
		
		:rtype: Tuple
		(Results of power test, Results of FDH test)
		"""

		esum = False
		atTable = False
		FDH = []
		Power = []
		EFPD = 0

		file = open(fileName)

		#This loop determines the maxium core FDH
		#Core FDH fail criteria is: FDH > 1.475
		for currLine in file.readlines():

			#Get each line more accessible for reading
			currLine = currLine.strip()
			currArr = currLine.split()

			#Out file contains many blank lines
			if not currLine:
				continue

			#Marks the beginning of the E-SUM table
			#Important table holding many test results at different timesteps
			#Contains FDH data
			if 'E-SUM' in currLine:
				esum = True

			#The E-COR report gives data on core power
			#The E-COR report has a very unique structure making it very easy to parse
			#The E-COR report gives equivilant powers at specific boron concentrations
			#The criteria for core power is EFPD >= 467 with 5 PPM boron remaining
			#5 PPM boron marks end of core cycle
			#Core power is measured at end of cycle
			elif("ACCUMULATED CYCLE ENERGY IS") in currLine:
				temp = currArr[4]
			#Also apart of E-COR Table
			elif('SOLUBLE BORON CONCENTRATION IS') in currLine:
				if float(currArr[4]) >= 5:
					EFPD = temp

			#Skips past the clutter at the top of the E-SUM table to core time step #2
			#Time step #1 is skipped as it accounts for the reactor powering up.
			if esum and currArr[0] == '2':
				atTable = True

			#End of E-SUM table conditions
			#Sometimes the reactor is tested for a Trip (SCRAM) accident scenario
			#Trip data is unnessicary for this stage and can be ignored
			#The table always ends with a footnote starting with '*'
			#Either of these two conditions signal to stop recording FDH values
			if currArr[0] == '*' or ('TRIP' in currArr[-1]):
				atTable = False
				esum = False

			#Once reading in the table, there will be no empty cells
			#FDH information is always stored in the 11th index
			if atTable:
				FDH.append(currArr[11])

		#In nuclear engineering, the most conservative answer is the correct answer
		#The most ideal FDH value is 1.00
		#FDH will always be above 1
		#Generated cores are graded on maximium FDH in lifetime for safety
		coreFDH = max(FDH)
		return(float(EFPD),float(coreFDH))

	def write(self,fuelArr,low,high,passNumber):
		"""
		Takes a fuelPat array and generates an ANC job file with it.

		:type fuelArr: arr
		Assembly locations
		
		:type low: int
		Lower enrichment assembly in fuelPat

		:type high: int
		Higher enrichment assembly in fuelPat

		:type passNumber: int
		Number to be added to basic fileName

		:rtype: void
		"""

		fileName = ("ANCinput%d.job" % passNumber)
		fuelNames = ['A1__000','B1__000','C1__000','D1__000','F1__148','E112080','F104080','F104148']
		convertedArr = []

		#Convert the numerical assembly system into the names used by Westinghouse
		for i in range(len(fuelArr)):
			convertedArr.append(fuelNames[fuelArr[i]])
		low = fuelNames[low]
		high = fuelNames[high]

		file = open(fileName,'w')

		#---------------------------------IMPORTANT NOTE---------------------------------
		#Out of respect for Westinghouse, this part of the function has been ommitted
		#Westinghouse jobs use a specific file structure
		#All this part of the fucntion does is mimics that structure
		#The only thing changed is the fuel assembly section
		#The job is created using the generated fuelPat that passed enrichment screenings
		#--------------------------------------------------------------------------------
		
		'''
		Large chunck of ANC Job file here
		'''

		#Example of FUELPAT generation (Only different part across each .job file)
		file.write("FUELPAT(1,1) = %s/\n" % low)
		file.write("FUELPAT(1,2) = %s, %s, %s, %s, %s, %s, %s, %s/\n" % (high,low,high,low,high,convertedArr[6],convertedArr[3],convertedArr[1]))
		file.write("FUELPAT(1,3) = %s, %s, %s, %s, %s, %s, %s/\n" % (low,high,low,high,low,convertedArr[7],convertedArr[4]))
		file.write("FUELPAT(1,4) = %s, %s, %s, %s, %s, %s, %s/\n" % (high,low,high,convertedArr[12],convertedArr[10],convertedArr[8],convertedArr[5]))
		file.write("FUELPAT(1,5) = %s, %s, %s, %s, %s, %s/\n" % (low,high,low,convertedArr[10],convertedArr[11],convertedArr[9]))
		file.write("FUELPAT(1,6) = %s, %s, %s, %s, %s/\n" % (high,convertedArr[6],convertedArr[7],convertedArr[8],convertedArr[9]))
		file.write("FUELPAT(1,7) = %s, %s, %s, %s/\n" % (convertedArr[2],convertedArr[3],convertedArr[4],convertedArr[5]))
		file.write("FUELPAT(1,8) = %s, %s/\n" % (convertedArr[0],convertedArr[1]))

		'''
		Large chunck of ANC Job file here
		'''

		file.close()