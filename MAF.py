import matplotlib.pyplot as plt
##plotting the distances in the logarithmic scle (Histogram)

#bins=3, range=(0,30)
plt.hist(tt['MAF'], bins=50,range=(0.05,0.5), alpha = 0.7,color='silver',edgecolor = "black") #label='Chr08'
plt.legend(loc='upper right')
plt.axvline(tt['MAF'].mean(), color='r', linestyle='dashed', linewidth=1)
min_ylim, max_ylim = plt.ylim()
plt.text(tt['MAF'].mean()*1.1, max_ylim*0.9, 'Mean MAF: {:.2f}'.format(tt['MAF'].mean()))
plt.xlabel('Minor Allele Frequency')
plt.ylabel('Frequency')
  

#plt.hist(b, bins, alpha = 0.5, label='b')



plt.show()
