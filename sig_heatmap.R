# install packages
#install.packages(pkgs = c("ggplot2","dplyr","tidyr","stringr","gplots","plotrix"),dependencies = T)

#load packages
library(ggplot2) # ggplot() for plotting
library(dplyr) # data reformatting
library(tidyr) # data reformatting
library(stringr) # string manipulation


#read csv file
m <- read.csv("ALL_SIG_RESULTS_voom.csv",header=T,stringsAsFactors=F)

m2 <- m %>%
  # convert data to long format
  gather(key="feature",value="value",-Drug) %>%
  # rename columns
  setNames(c("drug","feature","value")) %>%
  # convert year to factor
  mutate(drug=factor(drug)) %>%
  # convert value to numeric (also converts '-' to NA, gives a warning)
  mutate(value=as.numeric(value))

p1 <- ggplot(m2,aes(x=feature,y=drug,fill=value))+
  geom_tile()
print(p)

#modified ggplot
p2 <- ggplot(m2,aes(x=feature,y=drug,fill=value))+
  #add border white colour of line thickness 0.25
  geom_tile(colour="white",size=0.25)+
  #remove x and y axis labels
  labs(x="",y="")+
  #remove extra space
  scale_y_discrete(expand=c(0,0))+
  #define new breaks on x-axis
  scale_x_discrete(expand=c(0,0))+
  #set a base size for all fonts
  theme_grey(base_size=8)+
  #theme options
  theme(
    #bold font for legend text
    legend.text=element_text(face="bold"),
    #set thickness of axis ticks
    axis.ticks=element_line(size=0.4),
    #remove plot background
    plot.background=element_blank(),
    #remove plot border
    panel.border=element_blank())

print(p2)

m3 <- m2 %>%
  mutate(drug=factor(drug,levels=rev(sort(unique(drug))))) %>%
  # create a new variable from count
  mutate(countfactor=cut(value,breaks=c(-2,-1,0,1),
                         labels=c("Sensitive","0","Resistant"))) %>%
  # change level order
  mutate(countfactor=factor(as.character(countfactor),levels=rev(levels(countfactor))))

# assign text colour
textcol <- "grey40"

# further modified ggplot
p3 <- ggplot(m3,aes(x=feature,y=drug,fill=countfactor))+
  geom_tile(colour="grey",size=0.2)+
  guides(fill=guide_legend(title="Sensitivity"))+
  labs(x="Features",y="Drugs",title="Significant Features for ALL Drugs RNA-seq")+
  scale_y_discrete(expand=c(0,0))+
  scale_x_discrete(expand=c(0,0))+
  scale_fill_manual(values=c("#d53e4f","#435af4","#fdae61","#fee08b","#e6f598","#abdda4","#ddf1da"),na.value = "white")+
  theme_grey(base_size=10)+
  theme(legend.position="right",legend.direction="vertical",
        legend.title=element_text(colour=textcol),
        legend.margin=margin(grid::unit(0,"cm")),
        legend.text=element_text(colour=textcol,size=7,face="bold"),
        legend.key.height=grid::unit(0.8,"cm"),
        legend.key.width=grid::unit(0.2,"cm"),
        axis.text.x=element_text(size=10,angle=90,colour=textcol),
        axis.text.y=element_text(size=10,vjust=0.2,colour=textcol),
        axis.ticks=element_line(size=0.4),
        plot.background=element_blank(),
        panel.border=element_blank(),
        plot.margin=margin(0.7,0.4,0.1,0.2,"cm"),
        plot.title=element_text(colour=textcol,hjust=0,size=14,face="bold"))

print(p3)



