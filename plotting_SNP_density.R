#install.packages("CMplot")
setwd("/home/baign/HPC/Project")
library("CMplot")
annot <- read.csv("head.txt", header=TRUE,sep="\t")

##plotting snp density plot
CMplot(annot,type="p",plot.type="d",bin.size=25000,chr.den.col=c("darkgreen", "yellow", "red"),file="pdf",memo="",
       main="SNP density within 25kb bin size ",file.output=TRUE,verbose=TRUE,width=9,height=6)
dev.off()

