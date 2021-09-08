library(ggplot2)
#install.packages("ggrepel")
library(ggrepel)
figtype = 'boxplot'
getwd()
pop_t=read.csv("Maf_added_recommended_vars.txt",sep="\t")
names(pop_t)[1] <- "Chr"
names(pop_t)[2] <- "POs"
names(pop_t)[3] <- "RA"
names(pop_t)[4] <- "AF"
names(pop_t)[5] <- "MAF"
#pop_t <-pop_t[,c("Chr","Pos","RA","AF","MAF")] 
head(pop_t)
pdf("MAF_all.pdf")

#png("before_maf.png",width=6,height=6,units="in",res=1200)
hist(pop_t$MAF, main = "Minor Allele Frequency Distribution ", xlab = "Minor Allele Frequency",ylab="Number of SNPs", xlim = c(0.0, 0.5),ylim=c(0,200000),col = "peachpuff")
dev.off()
####making boxplot per chromosomes https://r-coder.com/boxplot-r/
pdf("boxplot_all_maf_colored.pdf")
par(mar=c(15,5,1,1))
boxplot(MAF ~ Chr, data = pop_t,las=2,cex.names=0.3,label.cex=2,outlier=TRUE,cex.axis = 0.8) # Equivalent

dev.off()
´##adding points to boxplot
#pdf("boxplot_2all_maf_colored.pdf")
#stripchart(MAF ~ Chr, data = pop_t, vertical = TRUE, method = "jitter",
           #pch = 19, add = TRUE, col = 1:length(levels(pop_t$Chr)))


##return values from boxplot
#res <- boxplot(MAF ~ Chr, data = pop_t)
#res
# Boxplot by group
pdf("MAF_all_chr.pdf")
ggplot(data = pop_t, aes(x = Chr, y = MAF)) +
  stat_boxplot(geom = "errorbar", # Boxplot with error bars 
               width = 0.2) +
  geom_boxplot(fill = "#4271AE", colour = "#1F3552", # Colors
               alpha = 0.9, outlier.colour = "red") +
  scale_y_continuous(name = "MAF") +  # Continuous variable label
  scale_x_discrete(name = "Chromosomes") +      # Group label
  #ggtitle("b)") + # Plot title
  theme(axis.line = element_line(colour = "black", # Theme customization
                                 size = 0.25))
dev.off()
