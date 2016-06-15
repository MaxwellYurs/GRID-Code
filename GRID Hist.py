# coding=utf-8
import matplotlib.pyplot as plt #imports the matplot library pyplot and names it plt

import csv

Channel1 = []                         #initializing the lists for each channel to be filled from file
Channel2 = []
Channel3 = []
Channel4 = []
TotalCounts = []
                                                                            #opening the .csv file from the serial port. File needs to be saved
with open('firstCoolTermUse1.csv') as csvfile:                              #in the same folder as the code being written. Must select file before
    readCSV = csv.reader(csvfile, delimiter=',')                            #running 
    for row in readCSV:
        TotalCounts.append(float(row[2]))
        if float(row[0]) == 1:
            Channel1.append(float(row[2]))

        if float(row[0]) == 2:
            Channel2.append(float(row[2]))

        if float(row[0]) == 3:
            Channel3.append(float(row[2]))

        if float(row[0]) == 4:
            Channel4.append(float(row[2]))



Bins1=3    #<-----Channel 1 number of Bins (Can be modified)
Bins2=25    #<-----Channel 2 number of Bins (Can be modified)
Bins3=25    #<-----Channel 3 number of Bins (Can be modified)
Bins4=25    #<-----Channel 4 number of Bins (Can be modified)
BinsTC=25    #<-----Channel 4 number of Bins (Can be modified)

fig, axes = plt.subplots(1,5, figsize=(15,3)) #<----defines the number of plots, figure size(width,height) in inches

axes[0].hist(Channel1,bins=Bins1,histtype='step',range=None,normed=False)  #Directions for adjusting Plot attributes:
axes[0].set_title("Channel 1")                              #number of bins and can be adujusted using
axes[0].set_xlabel("volts")                                 #the above Bins(1-4) assingments.
axes[0].set_ylabel("counts")                                #histtype : ‘bar’, ‘barstacked’, ‘step’, ‘stepfilled’
                                                            #x-axis range can be adjusted using a tuple instead of None
                                                            #Plots can be normalized by changing 'normed' to True
axes[1].hist(Channel2,bins=Bins2,histtype='step',range=None,normed=False)
axes[1].set_title("Channel 2")
axes[1].set_xlabel("volts")
axes[1].set_ylabel("counts")

axes[2].hist(Channel3,bins=Bins3,histtype='step',range=None,normed=False)
axes[2].set_title("Channel 3")
axes[2].set_xlabel("volts")
axes[2].set_ylabel("counts")

axes[3].hist(Channel4,bins=Bins4,histtype='step',range=None,normed=False)
axes[3].set_title("Channel 4")
axes[3].set_xlabel("volts")
axes[3].set_ylabel("counts")

axes[4].hist(TotalCounts,bins=BinsTC,histtype='step',range=None,normed=False)
axes[4].set_title("Total Counts")
axes[4].set_xlabel("volts")
axes[4].set_ylabel("counts")

fig.tight_layout()  #<------automatically aligns the plots so they don't inadvertantly over lap
plt.show()


