import stats
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


fr=open('un_s.txt','r')
a=fr.read()
aa=a.split("\n")[:-1]
listname=[]
for base in aa:
    listname.append(base.split(","))

i=0
while i<len(listname)-1:
    j=i+1
    dist= (int(listname[j][2])-int(listname[i][2]))+1
    listname[i].append(dist)
    i+=1
df9=pd.DataFrame(listname)
df9.columns=['Affx ID','cust_chr','cust_pos','SNPType','dist_snps']
#df9.to_csv('dist_calculated_chr12.txt',index=False,header=True,sep="\t")

m=df9[["dist_snps"]].describe()
med = df9['dist_snps'].median()
#print(m)
#print('median  ',med)
df9['dist_snps'].min()


##plotting the distances in the logarithmic scle (Histogram)
bins = np.linspace(1, 221460, 100)
#plt.hist(df9['dist_snps'], bins, alpha = 0.7, label='Chr08')

logbins = np.logspace(np.log10(bins[0]),np.log10(bins[-1]),len(bins))
plt.hist(df9['dist_snps'], bins=logbins, alpha = 0.9, label='Chrun')

plt.legend(loc='upper right')
plt.axvline(df9['dist_snps'].mean(), color='k', linestyle='dashed', linewidth=1)
min_ylim, max_ylim = plt.ylim()
plt.text(df9['dist_snps'].mean()*1.1, max_ylim*0.9, 'Mean: {:.2f}'.format(df9['dist_snps'].mean()))
plt.xscale('log')

#plt.hist(b, bins, alpha = 0.5, label='b')

plt.show()


