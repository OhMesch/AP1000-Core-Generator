from readWrite import ReadWrite

class Core():
    def enrichCheck(self, low, high, fuelArr):
        '''
        Takes all the fuel assemblies in a given core and returns the average enrichment

        :type low: int
        The lower enrichment assembly to be used in the interior checkerboard

        :type high: int
        The higher enrichment assembly to be used in the interior checkerboard

        :type fuelArr: arr
        The generated core assembly layout to be tested

        :rtype: Float
        The average enrichment of all assemblies in the core
        '''
        totalEnrich = 0

        #Enrichment levels corresponding to 0 = A1, 1 = B1, etc...
        rodEnrichLevels = [0.740 , 1.655 , 2.800 , 3.200 , 4.330 , 3.779, 4.330 , 4.330]

        #Accounts for layout of interior checkerboard
        totalEnrich += 8 * rodEnrichLevels[low] * 4 + rodEnrichLevels[low]
        totalEnrich += 9 * rodEnrichLevels[high] * 4

        for i in range(len(fuelArr)):
            #These assemblies do not get doubled from 1/4th to 1/8th symmetry
            if i in [0,2,11,12]:
                totalEnrich += rodEnrichLevels[fuelArr[i]] * 4
            #These assemblies get double from 1/4th to 1/8th symmetry
            else: 
                totalEnrich += rodEnrichLevels[fuelArr[i]] *2 * 4
        return(totalEnrich/157)

    def generate(self,low,high):
        '''
        Takes the fuel assemblies to be used in the internal checkerboard 
        Returns all possible combinations of fuel assemblies passing enrichment screening

        :type low: int
        The lower enrichment assembly to be used in the interior checkerboard

        :type high: int
        The higher enrichment assembly to be used in the interior checkerboard

        :rtype: void
        Generates output files
        '''
        iterations = 0
        passed = 0
        for i in range(3):
            for j in range(3):
                for k in range(5):
                    for l in range(8):
                        for m in range(3):
                            for n in range(3):
                                for o in range(5):
                                    for p in range(8):
                                        for q in range (5):
                                            for r in range(3):
                                                for s in range(8):
                                                    for t in range(5):
                                                        for u in range(5):
                                                            fuelPat = [i,j,k,l,m,n,o,p,q,r,s,t,u]
                                                            if 2.775 < self.enrichCheck(low,high,fuelPat) < 2.785:
                                                                rWDriver = ReadWrite()
                                                                rWDriver.write(fuelPat,low,high,passed)
                                                                passed+=1
                                                            iterations += 1
                                                            if iterations %100000 == 0:
                                                                print(388800000-iterations,' Remaining')
        print('Program Completed\n%d fuelPats passed enrichment out of %d' % (passed,iterations))

coreDriver = Core()
coreDriver.generate(1,5)