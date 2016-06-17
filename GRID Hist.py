# coding=utf-8
import matplotlib.pyplot as plt                         #imports the matplot library pyplot and names it plt, also the csv format and Counter
                                                        #function
import csv

from collections import Counter

file_name = raw_input("Please input file name: ")       #prompts user to input a file name, must be in .csv format

Channel1 = []                                           #initializing the lists for each channel to be filled from file
Channel2 = []
Channel3 = []
Channel4 = []
TotalCounts = []

Check1 = False                                          #initializing check to see if any reading occurred for each channel
Check2 = False
Check3 = False
Check4 = False
                                                        #opening the .csv file from the serial port. File needs to be saved
with open(file_name) as csvfile:                        #in the same folder as the code being written. User is prompted for file name
    readCSV = csv.reader(csvfile, delimiter=',')

    for row in readCSV:                                 #checks to make sure at least one event occurred for each channel. If no event occurred,
        if row[0] == '1':                               #nothing will be appended to the lists causing issues on Mac
           Check1 = True
        if row[0] == '2':
            Check2 = True
        if row[0] == '3':
            Check3 = True
        if row[0] == '4':
            Check4 = True

with open(file_name) as csvfile:                       #appends the voltage levels to each channels' respective list. If no event occurred, the list
    readCSV = csv.reader(csvfile, delimiter=',')       #is set equal to zero

    for row in readCSV:
        TotalCounts.append(float(row[2]))

        if Check1 == True:
            if row[0] == '1':
                Channel1.append(float(row[2]))
        else:
            Channel1 = 0

        if Check2 == True:
            if row[0] == '2':
                Channel2.append(float(row[2]))
        else:
            Channel2 = 0

        if Check3 == True:
            if row[0] == '3':
                Channel3.append(float(row[2]))
        else:
            Channel3 = 0

        if Check4 == True:
            if row[0] == '4':
                Channel4.append(float(row[2]))
        else:
            Channel4= 0


Bins1=50    #<-----Channel 1 number of Bins (Can be modified)
Bins2=50    #<-----Channel 2 number of Bins (Can be modified)
Bins3=50    #<-----Channel 3 number of Bins (Can be modified)
Bins4=50    #<-----Channel 4 number of Bins (Can be modified)
BinsTC=50    #<-----Channel 4 number of Bins (Can be modified)

fig, axes = plt.subplots(1,5, figsize=(30,3)) #<----defines the number of plots, figure size(width,height) in inches

CH1 = axes[0].hist(Channel1,bins=Bins1,histtype='step',range=None,normed=False)  #Directions for adjusting Plot attributes:
axes[0].set_title("Channel 1")                              #number of bins and can be adujusted using
axes[0].set_xlabel("volts")                                 #the above Bins(1-4) assingments.
axes[0].set_ylabel("counts")                                #histtype : ‘bar’, ‘barstacked’, ‘step’, ‘stepfilled’
                                                            #x-axis range can be adjusted using a tuple instead of None
                                                            #Plots can be normalized by changing 'normed' to True
CH2 = axes[1].hist(Channel2,bins=Bins2,histtype='step',range=None,normed=False)
axes[1].set_title("Channel 2")
axes[1].set_xlabel("volts")
axes[1].set_ylabel("counts")

CH3 = axes[2].hist(Channel3,bins=Bins3,histtype='step',range=None,normed=False)
axes[2].set_title("Channel 3")
axes[2].set_xlabel("volts")
axes[2].set_ylabel("counts")

CH4 = axes[3].hist(Channel4,bins=Bins4,histtype='step',range=None,normed=False)
axes[3].set_title("Channel 4")
axes[3].set_xlabel("volts")
axes[3].set_ylabel("counts")

CHTC = axes[4].hist(TotalCounts,bins=BinsTC,histtype='step',range=None,normed=False)
axes[4].set_title("Total Counts")
axes[4].set_xlabel("volts")
axes[4].set_ylabel("counts")

fig.tight_layout()  #<------automatically aligns the plots so they don't inadvertantly over lap

i = 0

for n in CH1[0]:                                       #mutliple for loops to find the maximum number of counts for each channel along with the
    if n == max(CH1[0]):                               #voltage values for the left and right sides of the max. count bin
        max_counts1 = n
        break
    else:
        i+=1

k = i+1
i = 0

for n in CH1[1]:
    if i == k-1:
        left_side1 = n
    if i == k:
        right_side1 = n
        break
    i += 1

i = 0
k = 0

for n in CH2[0]:
    if n == max(CH2[0]):
        max_counts2 = n
        break
    else:
        i += 1

k = i + 1
i = 0

for n in CH2[1]:
    if i == k - 1:
        left_side2 = n
    if i == k:
        right_side2 = n
        break
    i += 1

i = 0
k = 0

for n in CH3[0]:
    if n == max(CH3[0]):
        max_counts3 = n
        break
    else:
        i += 1

k = i + 1
i = 0

for n in CH3[1]:
    if i == k - 1:
        left_side3 = n
    if i == k:
        right_side3 = n
        break
    i += 1

i = 0
k = 0

for n in CH4[0]:
    if n == max(CH4[0]):
        max_counts4 = n
        break
    else:
        i += 1

k = i + 1
i = 0

for n in CH4[1]:
    if i == k - 1:
        left_side4 = n
    if i == k:
        right_side4 = n
        break
    i += 1

i = 0
k = 0

for n in CHTC[0]:
    if n == max(CHTC[0]):
        max_countsTC = n
        break
    else:
        i += 1

k = i + 1
i = 0

for n in CHTC[1]:
    if i == k - 1:
        left_sideTC = n
    if i == k:
        right_sideTC = n
        break
    i += 1

print "The max counts for Channel 1 was " + str(max_counts1) + " ranging from " + str(left_side1) + " to " + str(right_side1)
print "The max counts for Channel 2 was " + str(max_counts2) + " ranging from " + str(left_side2) + " to " + str(right_side2)
print "The max counts for Channel 3 was " + str(max_counts3) + " ranging from " + str(left_side3) + " to " + str(right_side3)
print "The max counts for Channel 4 was " + str(max_counts4) + " ranging from " + str(left_side4) + " to " + str(right_side4)
print "The max counts for all channels was " + str(max_countsTC) + " ranging from " + str(left_sideTC) + " to " + str(right_sideTC)

plt.show()                                                 #shows the graphs created earlier





