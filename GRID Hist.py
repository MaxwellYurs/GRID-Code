# coding=utf-8
import matplotlib.pyplot as plt #imports the matplot library pyplot and names it plt

Channel1=[2.1,2.3,2.2,2,3,2.25,2.6,5,5,6,6,7,7,7,7,7]  #Channel 1 Data (need to figure out how to import data array
Channel2=[3,3,3,4,1,4,6,6,6,6,3,3,3,9,9,9,9,9,7]  #Channel 2 Data  and subarray by channel)
Channel3=[1,1,1,1,1,1,1,1,1,4,4,4,4,4,4,4,4,4,4]  #Channel 3 Data
Channel4=[2,2,2,2,2,2,2,2,2,2,2,7,7,7,7,7,7,7,7]  #Channel 4 Data

Bins1=3    #<-----Channel 1 number of Bins (Can be modified)
Bins2=25    #<-----Channel 2 number of Bins (Can be modified)
Bins3=25    #<-----Channel 3 number of Bins (Can be modified)
Bins4=25    #<-----Channel 4 number of Bins (Can be modified)

fig, axes = plt.subplots(1,4, figsize=(15,3)) #<----defines the number of plots, figure size(width,height) in inches

axes[0].hist(Channel1,bins=Bins1,histtype='step'
,range=(2,3),normed=False)                                   #Directions for adjusting Plot attributes:
axes[0].set_title("Channel 1")                              #number of bins and can be adujusted using
axes[0].set_xlabel("volts")                                 #the above Bins(1-4) assingments.
axes[0].set_ylabel("counts")                                #histtype : ‘bar’, ‘barstacked’, ‘step’, ‘stepfilled’
                                                            #x-axis range can be adjusted using a tuple instead of None
                                                            #Plots can be normalized by changing 'normed' to True
axes[1].hist(Channel2,bins=Bins2,histtype='step'
,range=None,normed=False)
axes[1].set_title("Channel 2")
axes[1].set_xlabel("volts")
axes[1].set_ylabel("counts")

axes[2].hist(Channel3,bins=Bins3,histtype='step'
,range=None,normed=False)
axes[2].set_title("Channel 3")
axes[2].set_xlabel("volts")
axes[2].set_ylabel("counts")

axes[3].hist(Channel4,bins=Bins4,histtype='step'
,range=None,normed=False)
axes[3].set_title("Channel 4")
axes[3].set_xlabel("volts")
axes[3].set_ylabel("counts")
plt.show()

#fig.tight_layout()  #<------automatically aligns the plots so they don't inadvertantly over lap