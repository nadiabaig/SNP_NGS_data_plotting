#plotting results
import matplotlib.pyplot as plt
import random

data = {
"Agria-01":1.1496926190865318 ,
"Agria-02": 1.1088360960741968,
"Agria-03": 1.45537936984593 ,
"Agria_04": 1.093525761526489,
"Agria-Stich_05":1.0321974075615357 ,
"Agria-06":1.0372462184213327 ,
"Agria-07":1.01243657896714 ,
"Agria-08":1.0371274050865915 ,
"AgriaRP-09":0.9008744961504583 ,
"Agria-10":0.9882924179249235 ,
"Agria-11":1.009760041979995,
"Agria-12":0.9168985420417592,
"Agria-13":1.012674117947831,
"Agria-14":1.0226999278094169,
}

fig, ax = plt.subplots(figsize=(10, 5))

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd','hotpink','darkseagreen',
          '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf','salmon','khaki']

for i, (key, value) in enumerate(data.items()):
    ax.bar(key, value, color=colors[i])
    
ax.set_xlabel("Replicates")
ax.set_ylabel("Mendelian error rate (%)")
ax.set_ylim([0, max(data.values())+2])
ax.yaxis.grid(True)
plt.xticks(rotation=90) # Rotates x-labels by 90 degrees
plt.tight_layout()
plt.show()
