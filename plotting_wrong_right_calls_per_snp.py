#this code is plotting the wrong calls present in diploid genotypes based on fitpoly genotyping.
# Sort data by Chrom in alphabetical order
fd_dip_only_filtered = fd_dip_only_filtered.sort_values(by='Chrom', ascending=True)

# Set the figure size
plt.figure(figsize=(20, 10))

# Plot the count of the Status variable for each level of the Chrom variable
g = sns.catplot(x="Status", col="Chrom", col_wrap=7,
                data=fd_dip_only_filtered[fd_dip_only_filtered.Chrom.notnull()],
                kind="count", height=3.5, aspect=.8, 
                palette='tab10')

# Add the count value to each bar
for ax in g.axes:
    for p in ax.patches:
        height = p.get_height()
        ax.text(p.get_x()+p.get_width()/2.,
                height + 3,
                '{:1.0f}'.format(height),
                ha="center")

# Show the plot
plt.show()
