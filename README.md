# AP1000-Core-Generator
Nuclear engineering senior capstone project at The University of Pennsylvania
Spring 2017

The project was divided into three major componets:
  1. Design the fuel pattern (fuelPat) of an AP1000 core using fuel assemblies of various enrichments and burnable absorbers
  2. Run safety caclulations on the designed core
  3. Run operational caclulations on the designed core
  
About half of the semester was devoted to designing the core layout in step 1.

The objective of this repository is to generate all possible core assembly layouts that pass basic criteria of a safe and efficent core.

An AP1000 reactor core uses 157 fuel assemblies. 
For this core 8 assemblies have been made availible for use, representing 6 levels of enrichment.
The code represents different possible assembies using the numerals 0-7

Furthermore the numerals are grouped based on similar assembly properties.
Assemblies 0,1, and 2 are the only assemblies usable on the core perifory. (Low neutron leakage core)
Assemblies 0,1,2,3,4 can be used anywhere within the core
Assemblies 5,6,7 can only be used in certain assembly slots (WABA assemblies conflict with control rods)

Using these "rules" along with 1/8th core symmetry and conventional design practices (Ring of fire, internal checkerboard, low neutron leakage core), we can reduce the orignal 6.10(10^141) fuelPat combinations to 400 million.

An acceptible generated core has three main criteria:
  1. Average enrichment must be below 2.785%
  2. The core must have generated at least 467 effective full power days (EFPD) by end of cycle (EOC)
  3. At no point in the core cycle can the all rods out (ARO) peaking factor (FDH) exceed 1.475

The coreGen.py file is run first. This program generates every possible core in complience with the rules listed in lines 19-23 and runs a preliminary average enrichment screening. Any average enrihment above 2.7785% is discarded. Any Enrichment too far below is also discarded (will not pass power criteria).

This preliminary screening reduces the number of potentional cores to about
