## Overview
#This program takes the results of knife edge measurements of laser beams, which should have the form of 
#an error function if the beam is Gaussian, and turns them into a 1/e^2 beam size.
#The short cut is to take only the 90% of max power and the 10% of max power positions.

import numpy as np #import numpy functions
import matplotlib.pyplot as plt #import matplotlib functions
import csv #import csv functions

## Options
fontsize = 16;
shortcut1090 = 1; # 1 if you want to use positions of only 90% and 10% maximum power to determine beam size (shortcut for beam profiling)

if shortcut1090 == 1:
	##Import data
	directoryname = '/Users/mickelsp/Documents/YAG Beam Profile/'; 
	inputfilename = 'NdYAG10Hz_BeamProfile_20140313.txt';
	outputfilename = 'NdYAG10Hz_BeamProfile_20140313_BeamSize.txt';
	filename = directoryname + inputfilename;
	
	measurementposition = []; position90=[]; position10=[]; #initialize vectors
	inputfile = open(filename, 'r') #open file for reading
	for line in inputfile:
		line = line.strip() #read in a line at a time
		if not line.startswith("%"): #only read a line if it doesn't start with "%", the comment symbol used in Matlab.
			columns = line.split()
			measurementposition.extend([float(columns[0])]); # append value of measurementposition from this line to the list of measurement position values
			position90.extend([float(columns[1])]);
			position10.extend([float(columns[2])]);
	inputfile.close()

	## Convert lists into numeric vectors
	measurementposition = np.array(measurementposition); #[cm]
	position90 = np.array(position90); #[mm]
	position10 = np.array(position10); #[mm]

	### Calculate waist size based on Siegman formula (see p. 94 Pascal's Lab Notebook 1)
	waistsize = abs(position90-position10)/1.28; #[mm] 1/e^2 beam radius as a function of measurement position along length of beam
	
	## Plot waist size versus distance from lens]
	plt.figure(1)
	plt.plot(measurementposition,waistsize,'ro')
	plt.show()
	plt.xlabel('Longitudinal Position [cm]')
	plt.ylabel('Waist Size [mm]')
	#xlim([0 1.13])
	#ylim([0 max(waistsize(:))+0.1.*max(waistsize(:))])
	#legend('Vertical Size','Horizontal Size','Location','best')
	plt.title('Beam Sizes of Nd:YAG Laser')

## Write data to output file
outputfilepath = directoryname + outputfilename; # Full path for output file
np.savetxt(outputfilepath, (measurementposition,waistsize),fmt='%1.4e') #[cm mm] Data is written to text file 