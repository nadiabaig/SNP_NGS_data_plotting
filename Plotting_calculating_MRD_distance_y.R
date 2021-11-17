library(stringr)
library(ggplot2)
library(ape)
library(ggrepel)
setwd("/home/baign/.../new_plots")
source("genetic_diversity.txt")
temp=read.csv("t.txt", sep="\t")
data <- sapply(temp,function(x) {x <- gsub("na",NA,x)})
temp2 <- as.matrix(data)
colnames(temp2) <- c("s1","s2","s3")  #your sample names
dim(temp2) ##this will give you total samples and snps in the matrix

rownames(temp2) <- paste("Marker",c(1:99),sep="")  #not including header
test2 <- as.matrix(genetic.distance(temp2))

test2[is.nan(test2)] = 0
a <-as.matrix(test2)
dim(a)
pop_t=read.csv("ypop.txt")
b=t(a)
b
dim(b)

write.table(b,"Rogered distance.txt", sep="\t",col.names = TRUE,quote = F)

#install.packages('ggfortify')
b <- read.csv(file = 'Rogered distance_year.txt',sep="\t")
pcoa <- cmdscale(b, eig = T)
(pcoa$eig/sum(pcoa$eig)*100)[1:10]

pcoa.var<- pcoa$eig
pcoa.var.per <- round(pcoa.var/sum(pcoa.var)*100, 2)
pcoa.var.per
## now make plot that shows the PCs and the variation:
pcoa1.data <- data.frame(Sample=rownames(pcoa$points),
                        X=pcoa$points[,1],
                        Y=pcoa$points[,2])

pcoa1.data$Year <-pop_t$Year
write.table(pca1.data,"usage_year_only_tet_pca.txt", sep="\t",col.names = TRUE,quote = F)

pcoa1.data=pcoa1.data%>%
  tibble::rownames_to_column(var="Genotypes")
pcoa1.data

pdf('New_ploidy.pdf',width=8,height=8)
theme_classic<-theme(panel.background = element_blank(),panel.border=element_rect(fill=NA),panel.grid.major = element_blank(),panel.grid.minor = element_blank(),strip.background=element_blank(),axis.text.x=element_text(colour="black",size=5),axis.text.y=element_text(colour="black",size=5),axis.ticks=element_line(colour="black",size=5),plot.margin=unit(c(1,1,1,1),"line"),text = element_text(size = 27))

labels.clone <- c("S_spegazzini","S_gourlayi","P40","H98D12","S_vernei","S_hawkesianum","S_sparsipilum","H80_577_1")
pc3 <- ggplot(pcoa1.data, aes(x = X, y = Y, colour =Ploidy ,shape=Ploidy,label=row.names(pcoa1.data)))+geom_point(size=1)+
  geom_label_repel(aes(label=ifelse(Genotypes %in% labels.clone, Genotypes , '')), size=4.2, max.overlaps =45, alpha=1, label.padding=unit(0.25,"lines"), label.size=0.3)+
  labs(
    x = paste0("PCoA 1 (",pcoa.var.per[1]," %)"),
    y = paste0("PCoA 2 (",pcoa.var.per[2]," %)"))
pc3=pc3+theme_classic()
pc3
dev.off()
