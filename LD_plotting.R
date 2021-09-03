setwd("/home/baign/project")
library(ggplot2)
library(dplyr)
library(stringr)
library(ggplot2)
dfr <- read.delim("MERGED_un.txt",sep=",",header=T,check.names=F,stringsAsFactors=F)
dfr[is.na(dfr)] = 0
dfr2 <-dfr[,c("Pos","x")] 
colnames(dfr2) <- c("pos","x")
dfr2
##making 1mb intervals of the data
dfr2$distc <- cut(dfr2$pos,breaks=seq(from=min(dfr2$pos)-1,to=max(dfr2$pos)+1,by= 1000000))
#Then compute mean and/or median r2 within the blocks
dfr1 <- dfr2 %>% group_by(distc) %>% summarise(mean=mean(x),median=median(x))
##a helper step to get mid points of our distance intervals for plotting.
dfr1 <- dfr1 %>% mutate(start=as.integer(str_extract(str_replace_all(distc,"[\\(\\)\\[\\]]",""),"^[0-9-e+.]+")),
                        end=as.integer(str_extract(str_replace_all(distc,"[\\(\\)\\[\\]]",""),"[0-9-e+.]+$")),
                        mid=start+((end-start)/2))
###Now plot R
p=ggplot()+
  geom_point(data=dfr1,aes(x=start,y=mean),size=0.4,colour="red")+
  geom_line(data=dfr1,aes(x=start,y=mean),size=0.3,alpha=0.5,colour="black")+
  labs(x="Distance (Megabases)",y=expression(LD-R~(r^{2})))+
  scale_x_continuous(breaks=c(0,10*10^6,20*10^6,30*10^6,40*10^6,50*10^6,60*10^6,70*10^6),labels=c("0","10","20","30","40","50","60","70"))+
  theme_bw()
ggsave("LD_R.png",p,height=8,width=8,units="cm",dpi=250)
