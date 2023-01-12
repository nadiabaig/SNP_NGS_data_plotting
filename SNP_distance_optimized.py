########checking the average distance b/w chromosmes of different dataframes 'i.e markers saved based on some specific conditions'
##also getting average for each class per chr
import os
annot=annot_a_b[['probeset_id','cust_chr','cust_pos','#Chrom']].copy()

#keeping only 4n probesets
annot_4n_only=pd.merge(annot,mclust_all1,on='probeset_id')
a_4=annot_4n_only[['probeset_id','cust_chr','cust_pos','#Chrom']].copy()

def separate_chromosomes(a_4):
    chromosomes = {}
    for chr_name in a_4['#Chrom'].unique():
        chromosomes[chr_name] = a_4[a_4['#Chrom']==chr_name]
    return chromosomes

def sort_chromosomes(chromosomes):
    sorted_chromosomes = {}
    for chr_name, chr_df in chromosomes.items():
        chr_df.sort_values(by=['cust_pos'], inplace=True)
        sorted_chromosomes[chr_name] = chr_df
    return sorted_chromosomes

chromosomes = separate_chromosomes(a_4)
sorted_chromosomes = sort_chromosomes(chromosomes)

#writing sorted chromosomes to separate files
for chr_name, chr_df in sorted_chromosomes.items():
    chr_df.to_csv(os.path.join("/1data/Nadia/10_Genotyping/Final_analysis/posterior_all/scored_posteriors", chr_name + ".csv9"), index=False)


def process_file(file_path):
    listname = []
    with open(file_path) as f:
        next(f) 
        for i in f:
            listname.append(i.split(","))
    i=0
    while i<len(listname)-1:
        j=i+1
        dist= (int(listname[j][2])-int(listname[i][2]))+1
        listname[i].append(dist)
        i+=1
    df = pd.DataFrame(listname)
    df.columns=['probeset_id','cust_chr','cust_pos','Chrom','dist_snps']
    m=df[["dist_snps"]].describe()
    med = df['dist_snps'].median()
    return df, m, med

file_list = ['/1data/Nadia/---/Chr01.csv9', 
             '/1data/Nadia/Chr02.csv9',
             '/1data/Nadia//Chr03.csv9',
             '/1data/Nadia//Chr04.csv9',
             
             
             # add more file paths here as needed
            ]

for file_path in file_list:
    df, m, med = process_file(file_path)
    df.to_csv(file_path + '.out', index=False)
    m.to_csv(file_path + '_describe.out', index=False)
    

'''
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
'''
#avg distance for all catogeries
#read all distance files and merge all
import glob
dip=glob.glob('/1data/Nadia/10_Genotyping/Final_analysis/posterior_all/scored_posteriors/*.out')
df_file001 = pd.concat([pd.read_csv(fp,sep=",").assign(New=os.path.basename(fp)) for fp in dip])
#case1
f1_fa=pd.merge(df_file001,f1_failed,on='probeset_id')
f1_pa=pd.merge(df_file001,f1_passed,on='probeset_id')
#case2
f2_fa=pd.merge(df_file001,f2_failed,on='probeset_id')
f2_pa=pd.merge(df_file001,f2_passed,on='probeset_id')

f1_fa.head(2)

#getting average distance for each chromosome for case1 and case2 SNPs separeted on chr and sorted on postions

def calculate_average_dist_snps(df):
    df.sort_values(by=['cust_pos_x'], inplace=True)
    grouped_df = df.groupby(by='Chrom')
    average_dist_snps = grouped_df['dist_snps'].mean()
    print('Average for all chroms',np.mean(average_dist_snps))
    return average_dist_snps


average_dist_snps = calculate_average_dist_snps(f1_fa)
print('Average for f1_failed:',average_dist_snps)

average_dist_snps = calculate_average_dist_snps(f1_pa)
print('Average for f1_passed:',average_dist_snps)

average_dist_snps = calculate_average_dist_snps(f2_fa)
print('Average for f2_failed:',average_dist_snps)

average_dist_snps = calculate_average_dist_snps(f2_pa)
print('Average for f2_passed:',average_dist_snps)



