from readWrite import ReadWrite

class Results():
	def filterResults(self, fileNum):
		'''
		:type fileNum: int
		The number of out files to sort

		:rtype: void
		'''
		goodResults = open("Possible_Cores.txt",'w')
		readDriver = ReadWrite()
		#for each output file
		for i in range(fileNum):
			testResults = readDriver.read("coreGenANC%d.out" % i)
			print(testResults)
			if testResults[0] >= 467 and testResults[1] <= 1.465:
				goodResults.write("Core %d passes all criteria.\n" % i)
				goodResults.write("EFPD = %d\n" % testResults[0])
				goodResults.write("Max FDH = %.3f\n" % testResults[1])

driver = Results()

#Number of files currently generated using the enrichment range 2.775-2.785 (Default range)
#Place the number of the largest output file +1
driver.filterResults(3762658)