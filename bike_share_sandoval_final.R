install.packages(haven,dplyr, car, multcomp, readr, mice, gridExtra, ggpubr, RColorBrewer, ggplot2, ggsci, mice, 
                 plyr, ggthemes, tidyverse)


library(dplyr)
library("ggpubr")
library(multcomp)
library(car)
library(Hmisc)
library("colorspace")
library(RColorBrewer)
library(ggthemes)
library(ggsci)
library(ggplot2)
library(mice)
library("e1071")
library(plyr)
library(tidyverse)
library(gridExtra)
library(dplyr)
library(colorspace)
library(devtools)
library(readr)




#reading in chicago dataset
#For the reviewer, you will need to make sure the file path is consistent with the directories you use. 
setwd("C:/rdata")
chi <- read_csv("C:/rdata/chicago.csv")
View(chi)


#obtaining age versus birth_year
chi$approximate_age=2017-chi$`Birth Year`

#converting trip in seconds to minutes
chi$trip_minutes=chi$`Trip Duration`/60

#making a factor for sex, so logistic regression can be performed
sex_levels<-c("Male", "Female")
chi$sex<-factor(chi$Gender, levels=sex_levels)

#making the distributions less skewed
chi$log_trip_minutes<-log10(chi$trip_minutes)
#also making log_age
chi$log_age<-log10(chi$approximate_age)

#making a SEM function
se <- function(x) sqrt(var(x)/length(x))

#selecting columns of data for chi_sum for summary
chi_sum<-chi[,c(4, 10:14)]

#computing summary statistics for each variable categorized by sex, including those that are missing
#you can see there is a lot of missing data for age by sex. Approximately missing 20% of the data for age and sex
summary_a<-chi_sum %>%
  group_by(sex) %>%
  summarise_each(funs(mean = mean(., na.rm = TRUE),
                      sd = sd(., na.rm = TRUE),
                      n = n(),
                      min = min(., na.rm = TRUE),
                      max = max(., na.rm = TRUE)))
summary_aa<-summary_a[,c(1,3,8,4,9,13)]


#QUESTION 1: How are trip minutes distributed within each sex? 

#the histogram is clearly skewed for trip minutes
graph1<-ggplot(data = chi, aes(x = trip_minutes, fill=sex)) + geom_histogram(color = 'black') + 
  scale_x_continuous(name="minutes", limits = c(0, 60), breaks = seq(0, 60, 10)) +
  scale_y_continuous(name="count", breaks=seq(0,30000,5000)) +
  labs(fill="Sex") +
  scale_fill_manual(values=c("#A3041C","#F5636B")) +
  facet_wrap(~sex)+
  ggtitle("Histogram of Trip Duration in Minutes(top) or Log(10) minutes (bottom) by Sex")+
  theme(legend.justification = c("right", "top"),
        legend.box.just = "right",
        legend.box.background = element_rect(color="black", size=1),
        legend.text = element_text(size = 12, colour = "black"),
        legend.title = element_text(size=14, face="bold"),
        axis.title.y = element_text(size=16, face="bold"),
        axis.text.y.left = element_text(size=14, face="bold"),
        plot.title = element_text(hjust = 0.5, size=14, face="bold"),
        axis.text.x = element_text(face="bold",size=12),
        axis.title.x.bottom = element_text(size=14, face="bold"),
        strip.text.x = element_text(size = 14,colour = "black", face="bold"),
        axis.line.x.bottom=element_line(),
        axis.line.y.left=element_line(),
        panel.background = element_blank(),
        panel.grid.major = element_line(colour="light gray"),
        axis.text.y = element_text(face="bold",size=12 ))


#making the distributions less skewed
chi$log_trip_minutes<-log10(chi$trip_minutes)
#also making log_age
chi$log_age<-log10(chi$approximate_age)




#trip duration is now more centrally distributed with the log transformation 
graph2<-ggplot(data = chi, aes(x = log_trip_minutes, fill=sex)) + geom_histogram(color = 'black') + 
  scale_x_continuous(name="log10 minutes", limits = c(0, 2.5), breaks = seq(0, 2.5, 0.5)) +
  scale_y_continuous(name="count", breaks=seq(0,30000,5000)) +
  labs(fill="Sex") +
  scale_fill_manual(values=c("#A3041C","#F5636B")) +
  facet_wrap(~sex)+
  #ggtitle("Trip Duration by Sex")+
  theme(legend.justification = c("right", "top"),
        legend.box.just = "right",
        legend.box.background = element_rect(color="black", size=1),
        legend.text = element_text(size = 12, colour = "black"),
        legend.title = element_text(size=14, face="bold"),
        axis.title.y = element_text(size=16, face="bold"),
        axis.text.y.left = element_text(size=14, face="bold"),
        plot.title = element_text(hjust = 0.5, size=18, face="bold"),
        axis.text.x = element_text(face="bold",size=12),
        axis.title.x.bottom = element_text(size=14, face="bold"),
        strip.text.x = element_text(size = 14,colour = "black", face="bold"),
        axis.line.x.bottom=element_line(),
        axis.line.y.left=element_line(),
        panel.background = element_blank(),
        panel.grid.major = element_line(colour="light gray"),
        axis.text.y = element_text(face="bold",size=12 ))

#putting these graphs over one another for easy visualization
#trip minutes by sex transformed and non transformed
grid.arrange(graph1, graph2, nrow = 2)


#answer: trip minutes have a positively skewed distribution when non-transformed. However, if transformed,
#it conforms to a more centrally distributed distriction


#------------------------------------------------------------------------------------------------------------#
#QUESTION 2: How is age distributed within sex?


#distribution of age in years
graph3<-ggplot(data = chi, aes(x= approximate_age, fill=sex)) + geom_histogram(color = 'black') + 
  scale_x_continuous(name="age in years", limits = c(0, 100), breaks = seq(0, 100, 20)) +
  scale_y_continuous(name="count", breaks=seq(0,47500,5000)) +
  labs(fill="sex") +
  scale_fill_manual(values=c("#023FA5", "#8E063B")) +
  facet_wrap(~sex)+
  ggtitle("Histograms of Age(top) or Log10(Age) (bottom) with Sex")+
  theme(legend.justification = c("right", "top"),
        legend.box.just = "right",
        legend.box.background = element_rect(color="black", size=1),
        legend.text = element_text(size = 12, colour = "black"),
        legend.title = element_text(size=14, face="bold"),
        axis.title.y = element_text(size=16, face="bold"),
        axis.text.y.left = element_text(size=14, face="bold"),
        plot.title = element_text(hjust = 0.5, size=14, face="bold"),
        axis.text.x = element_text(face="bold",size=12),
        axis.title.x.bottom = element_text(size=14, face="bold"),
        axis.line.x.bottom=element_line(),
        axis.line.y.left=element_line(),
        strip.text.x = element_text(size = 14,colour = "black", face="bold"),
        panel.background = element_blank(),
        panel.grid.major = element_line(colour="light gray"),
        axis.text.y = element_text(face="bold",size=12 ))
#distribution of age with log10 scale
graph4<-ggplot(data = chi, aes(x= log_age, fill=sex)) + geom_histogram(color = 'black') + 
  scale_x_continuous(name="age (in log10 scale)", limits = c(0.5, 2.5), breaks = seq(0.5, 2.5, 0.5)) +
  scale_y_continuous(name="count", breaks=seq(0,60000,5000)) +
  labs(fill="sex") +
  scale_fill_manual(values=c("#023FA5", "#8E063B")) +
 facet_wrap(~sex)+
  #ggtitle("Approximate log(age) by Sex")+
  theme(legend.justification = c("right", "top"),
        legend.box.just = "right",
        legend.box.background = element_rect(color="black", size=1),
        legend.text = element_text(size = 12, colour = "black"),
        legend.title = element_text(size=14, face="bold"),
        axis.title.y = element_text(size=16, face="bold"),
        axis.text.y.left = element_text(size=14, face="bold"),
        plot.title = element_text(hjust = 0.5, size=18, face="bold"),
        axis.text.x = element_text(face="bold",size=12),
        axis.title.x.bottom = element_text(size=14, face="bold"),
        strip.text.x = element_text(size = 14,colour = "black", face="bold"),
        axis.line.x.bottom=element_line(),
        axis.line.y.left=element_line(),
        panel.background = element_blank(),
        panel.grid.major = element_line(colour="light gray"),
        axis.text.y = element_text(face="bold",size=12 ))

#age by sex transformed and non transformed
grid.arrange(graph3, graph4, nrow = 2)



##answer: age is also skewed, but when log10 transformed, looks more centrally distributed as well. 


#subsetting, so I can obtain skewness for log_trip_minutes by sex
s1<-subset(chi$log_trip_minutes, chi$sex=="Male")
s2<-subset(chi$log_trip_minutes, chi$sex=="Female")
s3<-subset(chi$log_trip_minutes, is.na(chi$sex))

#----------------------------------------------------------------------------------------------------------------#
#there is a large amount of missing data, so I used the mice package to experiment with different approaches
#for imputing the age and sex from this data


#QUESTION 3: What is the impact of treating the data differently with the mice package when performing multiple imputation?
#3 approaches:
#1: ignore the extremes in age and see how sex and age is imputed
#2: set the extreme ages to missing and impute age and sex all at once, even though setting age to missing makes the data non-monotone
#3: do a sequential multiple imputation to satisfy monotonicity. Impute sex first. then impute age using imputed sex dataset


#approach for imputation 1: be sloppy in the analysis and ignore the extreme ages to impute age and sex

#selecting columns of data for chi2 from original dataset, so it takes less time
chi2<-chi[,c(12,13, 14)]

#is a monotone missing data pattern, so both sex and log age can be imputed
missing_pattern<-md.pattern(chi2,plot=TRUE)

#going to impute for both sex and log(age)->this takes awhile (~10 minutes) since it's being done 3 times with a large dataset
#I am doing this so I can compare the imputation techniques
#if you click on imp, you can see the methods of imputation are correct
#pmm=predictive mean matching, log_reg=logistic regression
imp<-mice(chi2,visit="monotone", maxit=1, m=3, seed=12, print=FALSE)

#this will now output the values for each of the three iterations for sex and log_age
fit<-with(imp, lm(log_trip_minutes ~sex+log_age))

#this shows the overall estimate that was obtained for each of the 3 imputations
est<-pool(fit)

#complete dataset with no values missing 
chi_complete_1<-mice::complete(imp)


#transforming log_age back to something more understandable
chi_complete_1$age1<-10^(chi_complete_1$log_age)
chi_complete_1$trip_min1<-10^(chi_complete_1$log_trip_minutes)




#computing summary statistics for each variable categorized by sex, including those that are missing
summary_1<-chi_complete_1 %>%
  group_by(sex) %>%
  summarise_each(funs(mean = mean(., na.rm = TRUE),
                      sd = sd(., na.rm = TRUE),
                      n = n(),
                      min = min(., na.rm = TRUE),
                      max = max(., na.rm = TRUE)))

summary_1$sex1<-summary_1$sex
summary1a<-summary_1[,c(32,16,6,12,7,13)]

#so before I did the first multiple imputation, I noticed there were some outrageous values. 
# setting them to na since they're fake
chi$appoximate_age2=chi$approximate_age
chi$appoximate_age2[chi$approximate_age < 5] <- NA
chi$appoximate_age2[chi$approximate_age > 90] <- NA
chi$logage2<-log10(chi$appoximate_age2)



#Imputation 2

#selecting columns 12, 13 and 16 for input into the multiple imputation.
chi2<-chi[,c(12,13, 16)]

#so you can see this is not a monotone pattern and that the people that faked their age, is causing a problem.
missing_pattern2<-md.pattern(chi2,plot=TRUE)

#I want to see how this performs, even though it's not the correct method, This will also take awhile...
imp2<-mice(chi2,visit="monotone", maxit=1, m=3,seed=54, print=FALSE)
fit2<-with(imp2, lm(log_trip_minutes ~sex + logage2))
est2<-pool(fit2)
chi_complete_2<-mice::complete(imp2)

#transforming for summary statistics
chi_complete_2$age2<-10^(chi_complete_2$logage2)
chi_complete_2$trip_min2<-10^(chi_complete_2$log_trip_minutes)


summary_2<-chi_complete_2 %>%
  group_by(sex) %>%
  summarise_each(funs(mean = mean(., na.rm = TRUE),
                      sd = sd(., na.rm = TRUE),
                      n = n(),
                      min = min(., na.rm = TRUE),
                      max = max(., na.rm = TRUE)))

summary_2$sex2<-summary_2$sex
summary2a<-summary_2[,c(32,16,6,12,7,13)]


#Imputation 3-2 parts, so they're part of the same thing

#I am now going to try the multiple imputations sequentially, analyzing for sex first, then logage2
chi3<-chi[,c(12,13)]
missing_pattern3<-md.pattern(chi3,plot=TRUE)

#imputing sex first
#this imputation is way faster
imp3<-mice(chi3,visit="monotone", maxit=1, m=3,seed=54, print=FALSE)

#fit
fit3<-with(imp3, lm(log_trip_minutes ~sex ))

#estimates
est3<-pool(fit3)

#complete data set with sex imputed
chi_complete_3<-mice::complete(imp3)

#making a new dataset, for the second part of the imputation
chi4<-mice::complete(imp3)

#adding in logage2 to the imputed dataset, so I can now impute log age
chi4$log_age<-chi$logage2

#missing data pattern
missing_pattern4<-md.pattern(chi4,plot=TRUE)

#now imputing log_age, is taking a lot longer due to mean matching
imp4<-mice(chi4,visit="monotone", maxit=1, m=3,seed=623, print=FALSE)
fit4<-with(imp4, lm(log_trip_minutes ~sex+log_age ))
est4<-pool(fit4)
chi_complete_4<-mice::complete(imp4)

#transformeing back the age as well as the trip minutes from the imputation so they'r in a more understandable form
chi_complete_4$age3<-10^(chi_complete_4$log_age)
chi_complete_4$tripmin3<-10^(chi_complete_4$log_trip_minutes)

summary_3<-chi_complete_4 %>%
  group_by(sex) %>%
  summarise_each(funs(mean = mean(., na.rm = TRUE),
                      sd = sd(., na.rm = TRUE),
                      n = n(),
                      min = min(., na.rm = TRUE),
                      max = max(., na.rm = TRUE)))

summary_3$sex3<-summary_3$sex
summary_3
summary3a<-summary_3[,c(27,16,5,10,6,11)]


#comparing it to the approximate_age obtained previously, so I can also see who WAS missing
chi_complete_overall<-chi_complete_4
chi_complete_overall$trip_minutes<-chi_complete_4$tripmin3
chi_complete_overall$orig_age<-chi$approximate_age
chi_complete_overall$imp1_age<-10^(chi_complete_1$log_age)
chi_complete_overall$imp2_age<-10^(chi_complete_2$logage2)
chi_complete_overall$imp3_age<-chi_complete_4$log_t_age3
chi_complete_overall$orig_sex<-chi$sex
chi_complete_overall$imp_sex1<-chi_complete_1$sex
chi_complete_overall$imp_sex2<-chi_complete_2$sex
chi_complete_overall$imp_sex3<-chi_complete_4$sex #I want to make sure this is clear that this is imputed

#this is a nice data_table that can be looked at to compare between people with missing data
chi_complete_overall2<-chi_complete_overall[,c(7:15)]

#QUESTION 3 answers: What is the impact of treating the data differently with the mice package when performing multiple imputation?
#3 approaches:
#1: ignoring the extreme ages had less of an impact than what I anticipated on mean age by sex
#2: they all appeared to behave similarly in improving the ability to detect trip minutes by sex


#--------------------------------------------------------------------------------------------------------------#
#Question 4: How did each imputation impact the mean age within each sex, as well as the amount of error?



#original data
summary_aa<-summary_a[,c(1,13,3,8,4,9)]
#imputation 1
summary1a<-summary_1[,c(32,16,6,12,7,13)]
#imputation 2
summary2a<-summary_2[,c(32,16,6,12,7,13)]
#imputation 3
summary3a<-summary_3[,c(27,16,6,11,5,10)]



#Mean age with each imputation
#original dataset
grapha<-ggplot(data = chi_complete_overall2, aes(y=orig_age, x=orig_sex, na.rm=TRUE)) + 
  geom_boxplot(fill="#8E063B", alpha=0.6 )  +  
  stat_summary(fun="mean", geom="point", shape=23, size=3, color="black", fill="white")+
  scale_x_discrete(name="sex") +
  scale_y_continuous(name="Age in years", limits = c(0, 120), breaks = seq(0, 120, 20)) +
  labs(fill="sex") +
  scale_fill_manual(values=c("#A3041C","#F5636B")) +
  ggtitle("Original data") +
  theme(legend.justification = c("right", "top"),
        legend.box.just = "right",
        legend.box.background = element_rect(color="black", size=1),
        legend.text = element_text(size = 12, colour = "black"),
        legend.title = element_text(size=14, face="bold"),
        axis.title.y = element_text(size=14, face="bold"),
        axis.text.y.left = element_text(size=12, face="bold"),
        plot.title = element_text(hjust = 0.5, size=14, face="bold"),
        axis.text.x = element_text(face="bold",size=12),
        axis.title.x.bottom = element_text(size=12, face="bold"),
        axis.line.x.bottom=element_line(),
        axis.line.y.left=element_line(),
        panel.background = element_blank(),
        panel.grid.major = element_line(colour="light gray"),
        axis.text.y = element_text(face="bold",size=10 ))

#imputation 1
graphb<-ggplot(data = chi_complete_overall2, aes(y=imp1_age, x=imp_sex1)) + 
  geom_boxplot(color="black", fill="#DA8459" )  +  
  stat_summary(fun="mean", geom="point", shape=23, size=3, color="black", fill="white")+
  scale_x_discrete(name="sex") +
  scale_y_continuous(name="Age in years", limits = c(0, 120), breaks = seq(0, 120, 20)) +
  labs(fill="sex") +
  scale_fill_manual(values=c("#A3041C","#F5636B")) +
  ggtitle("Imputation 1") +
  theme(legend.justification = c("right", "top"),
        legend.box.just = "right",
        legend.box.background = element_rect(color="black", size=1),
        legend.text = element_text(size = 12, colour = "black"),
        legend.title = element_text(size=14, face="bold"),
        axis.title.y = element_text(size=14, face="bold"),
        axis.text.y.left = element_text(size=12, face="bold"),
        plot.title = element_text(hjust = 0.5, size=14, face="bold"),
        axis.text.x = element_text(face="bold",size=12),
        axis.title.x.bottom = element_text(size=12, face="bold"),
        axis.line.x.bottom=element_line(),
        axis.line.y.left=element_line(),
        panel.background = element_blank(),
        panel.grid.major = element_line(colour="light gray"),
        axis.text.y = element_text(face="bold",size=10 ))


#imputation 2 graph
graphc<-ggplot(data = chi_complete_overall2, aes(y=imp2_age, x=imp_sex2)) + 
  geom_boxplot(color="black", fill="#F6C971" )  +  
  stat_summary(fun="mean", geom="point", shape=23, size=3, color="black", fill="white")+
  scale_x_discrete(name="sex") +
  scale_y_continuous("Age in years", limits = c(0, 120), breaks = seq(0, 120, 20)) +
  labs(fill="sex") +
  scale_fill_manual(values=c("#A3041C","#F5636B")) +
  ggtitle("Imputation 2") +
  theme(legend.justification = c("right", "top"),
        legend.box.just = "right",
        legend.box.background = element_rect(color="black", size=1),
        legend.text = element_text(size = 12, colour = "black"),
        legend.title = element_text(size=14, face="bold"),
        axis.title.y = element_text(size=14, face="bold"),
        axis.text.y.left = element_text(size=12, face="bold"),
        plot.title = element_text(hjust = 0.5, size=14, face="bold"),
        axis.text.x = element_text(face="bold",size=12),
        axis.title.x.bottom = element_text(size=12, face="bold"),
        axis.line.x.bottom=element_line(),
        axis.line.y.left=element_line(),
        panel.background = element_blank(),
        panel.grid.major = element_line(colour="light gray"),
        axis.text.y = element_text(face="bold",size=10 ))
#imputation 3 graph
graphd<-ggplot(data = chi_complete_overall2, aes(y=imp3_age, x=imp_sex3)) + 
  geom_boxplot(color="black", alpha=1.0, fill="#E2E6BD")  +  
  stat_summary(fun="mean", geom="point", shape=23, size=3, color="black", fill="white")+
  scale_x_discrete(name="sex") +
  scale_y_continuous("Age in years", limits = c(0, 120), breaks = seq(0, 120, 20)) +
  ggtitle("Imputation 3") +
  theme(legend.justification = c("right", "top"),
        legend.box.just = "right",
        legend.box.background = element_rect(color="black", size=1),
        legend.text = element_text(size = 12, colour = "black"),
        legend.title = element_text(size=12, face="bold"),
        axis.title.y = element_text(size=14, face="bold"),
        axis.text.y.left = element_text(size=12, face="bold"),
        plot.title = element_text(hjust = 0.5, size=14, face="bold"),
        axis.text.x = element_text(face="bold",size=12),
        axis.title.x.bottom = element_text(size=12, face="bold"),
        axis.line.x.bottom=element_line(),
        axis.line.y.left=element_line(),
        panel.background = element_blank(),
        panel.grid.major = element_line(colour="light gray"),
        axis.text.y = element_text(face="bold",size=10 ))

#putting these graphs together, so they can be compared for age by imputation or original data
grid.arrange(grapha,graphb,graphc, graphd, nrow = 1, ncol=4)


#original data t-test for age by sex-while significant due to the number of obs
#there is really not that much of a difference in age, even though it is significant
t0<-t.test(chi_complete_overall2$orig_age ~ chi_complete_overall2$orig_sex, na.rm=FALSE) 

#imputation 1 t-test for age by sex-note that the extreme ages are still present
#significant, note that the ages are almost spot on to original data
t1<-t.test(chi_complete_overall2$imp1_age ~ chi_complete_overall2$imp_sex1, var.equal=FALSE) 

#imputation t-test imputing for age and sex at the same time even when setting extreme ages to missing
#this surprised me. Mean age continued to be the same, even though the extreme ages were removed and imputed
#stil significant
t2<-t.test(chi_complete_overall2$imp2_age ~ chi_complete_overall2$imp_sex2, var.equal=FALSE) 

#t-test imputing for age and sex sequentially  
#again, same means are obtained, statistically significant.
#practical significance is limited. 
t3<-t.test(chi_complete_overall2$imp3_age~chi_complete_overall2$imp_sex3, var.equal=FALSE) 

#that wasn't very interesting.....
#a better question is whether there was a significant change in the mean age. 
#original data
summary_aa<-summary_a[,c(1,13,3,8,4,9)]
#imputation 1
summary1a<-summary_1[,c(32,16,6,12,7,13)]
#imputation 2
summary2a<-summary_2[,c(32,16,6,12,7,13)]
#imputation 3
summary3a<-summary_3[,c(27,16,6,11,5,10)]


#subsetting each imputed dataset to perform one sample t-test of mean age with each imputation against 
#the mean of the original data

#male subset for imputation 1
ss1a<-subset(chi_complete_1, chi_complete_1$sex=="Male")
#female subset for imputation 1
ss1b<-subset(chi_complete_1, chi_complete_1$sex=="Female")

#imputation 1 male age versus original data set age for male-is sig, but this is due to large n numbers
m1<-t.test(ss1a$age1, mu = 36.6 , alternative = "two.sided")

#imputation 1 female age versus original data set age for female- N/S
f1<-t.test(ss1b$age1, mu = 34.6 , alternative = "two.sided")


#male subset for imputation 2
ss2a<-subset(chi_complete_2, chi_complete_2$sex=="Male")
#female subset for imputation 2
ss2b<-subset(chi_complete_2, chi_complete_2$sex=="Female")

#imputation 1 male age versus original data set age for male-is technically significant
m2<-t.test(ss2a$age2, mu = 36.6 , alternative = "two.sided")

#imputation 1 female age versus original data set age for female-is also sig
f2<-t.test(ss2b$age2, mu = 34.6 , alternative = "two.sided")


#male subset for imputation 3/4, (3 and 4 are combined together since 
#sex is imputed to obtain dataset and then age is imputed)
ss4a<-subset(chi_complete_4, chi_complete_4$sex=="Male")

#female subset for imputation 3/4
ss4b<-subset(chi_complete_4, chi_complete_4$sex=="Female")

#imputation 4 male age versus original data set age for male-N/S
m4<-t.test(ss4a$age3, mu = 36.6 , alternative = "two.sided")

#imputation 4 female age versus original data set age for female-also N/S
f4<-t.test(ss4b$age3, mu = 34.6 , alternative = "two.sided")

#Answer to question 4: I would generally say there was very little difference in the 
#estimates obtained for the average age by sex with imputation. Even though there is statistical significance
#the practical significance has to be kept in mind. There was not any difference

#--------------------------------------------------------------------------------------------------------------#
#Question 5: How did each imputation impact the average trip distance within each sex, as well as the amount of error?


#an easier way of seeing all of the data a bit more easily

#original data
summary_aa<-summary_a[,c(1,13,3,8,4,9)]
#imputation 1
summary1a<-summary_1[,c(32,16,6,12,7,13)]
#imputation 2
summary2a<-summary_2[,c(32,16,6,12,7,13)]
#imputation 3
summary3a<-summary_3[,c(27,16,6,11,5,10)]


# standard deviation calculation for average trip minutes for each group of sex for error bars for plot
#I wanted to be able to visualize the amount of error with each imputation, which is better captured by the 
#standard deviation, over the sem

#mean +/- std deviation for sex
x1<-(summary_aa$trip_minutes_mean - summary_aa$trip_minutes_sd) 
x2<-(summary_aa$trip_minutes_mean + summary_aa$trip_minutes_sd) 

#mean +/- sem original data for sex. I thought about using the SEM, but it is difficult to see what is
#occurring with the error since the SEM becomes very small with the number of obs, as you can see below
x1a<-(summary_aa$trip_minutes_mean - (summary_aa$trip_minutes_sd)/sqrt(summary_aa$approximate_age_n))
x2a<-(summary_aa$trip_minutes_mean + (summary_aa$trip_minutes_sd)/sqrt(summary_aa$approximate_age_n)) 


#stdev forimputation 1 to add to graph
xa1<-(summary1a$trip_min1_mean -summary1a$trip_min1_sd) 
xa2<-(summary1a$trip_min1_mean +summary1a$trip_min1_sd) 

#sem imputation 2
xa1a<-(summary1a$trip_min1_mean -(summary1a$trip_min1_sd)/sqrt(summary1a$complete_age_n)) 
xa2a<-(summary1a$trip_min1_mean +(summary1a$trip_min1_sd)/sqrt(summary1a$complete_age_n))

#stdev for imputation 2 to add to graph
xb1<-(summary2a$trip_min2_mean - summary2a$trip_min2_sd) 
xb2<-(summary2a$trip_min2_mean + summary2a$trip_min2_sd) 

#stdev for imputation3 to add to graph
xc1<-(summary3a$tripmin3_mean - summary3a$tripmin3_sd) 
xc2<-(summary3a$tripmin3_mean + summary3a$tripmin3_sd) 


# mean as a dot with standard deviation in the error bars
#original data mean trip minutes plus standard deviation by sex
#I placed a reference line for mean trip minutes for male (in blue) and female (in red),
#relative to this plot, for easier comparison
plot1 <- ggplot(summary_aa, aes(x=sex, y=trip_minutes_mean, na.rm=FALSE)) + 
  geom_point(stat="identity", size=3.5, color="black") +
  geom_errorbar(aes(ymin=x1,ymax=x2), width=.2, size=1.5, position=position_dodge(.9))+
  geom_hline(data=summary_aa, aes(yintercept=trip_minutes_mean, color=sex),
              size=1,linetype="dashed")+
  scale_y_continuous(name="average trip in minutes (+/-) stdev",limits = c(-20,80), breaks=c(-20,0,20,40,60,80))+
  labs(fill = "sex", alpha=0.5)+
  ggtitle("Original data")+
  scale_color_aaas()+
  theme_minimal(base_size = 14) +
  theme(legend.position="top",
        legend.box.just = "center",
        #legend.box.background = element_rect(color="black", size=1),
        legend.text = element_text(size = 8, colour = "black"),
        legend.title = element_text(size=8, face="bold"),
        axis.title.y = element_text(size=16, face="bold"),
        axis.text.y.left = element_text(size=14, face="bold"),
        plot.title = element_text(hjust = 0.5, size=18, face="bold"),
        axis.text.x = element_text(face="bold",size=10.5),
        axis.title.x.bottom = element_text(size=14, face="bold"),
        axis.line.x.bottom=element_line(),
        axis.line.y.left=element_line(),
        panel.background = element_blank(),
        panel.grid.major = element_line(colour="light gray"),
        axis.text.y = element_text(face="bold",size=12 ))

#imputation 1: mean trip minutes plus standard deviation by sex
plot2 <- ggplot(summary1a, aes(x=sex1, y=trip_min1_mean)) + 
  geom_point(stat="identity", size=3.5, color="black") +
  geom_errorbar(aes(ymin=xa1,ymax=xa2), width=.2, color="blue",size=1.5, position=position_dodge(.9), alpha=0.8)+
  scale_x_discrete(name="sex") +
  scale_y_continuous(name="average trip in minutes (+/-) stdev",limits = c(-20,80), breaks=c(-20,0,20,40,60,80)) +
  scale_color_aaas()+
  geom_hline(data=summary_aa, aes(yintercept=trip_minutes_mean, color=sex),
             size=1,linetype="dashed")+
  labs(color = "sex", alpha=0.6)+
  ggtitle("Imputation 1")+
  theme_minimal(base_size = 14) +
  theme(legend.position="top",
        legend.box.just = "center",
        legend.text = element_text(size = 8, colour = "black"),
        legend.title = element_text(size=8, face="bold"),
        axis.title.y = element_text(size=16, face="bold"),
        axis.text.y.left = element_text(size=14, face="bold"),
        plot.title = element_text(hjust = 0.5, size=18, face="bold"),
        axis.text.x = element_text(face="bold",size=14),
        axis.title.x.bottom = element_text(size=14, face="bold"),
        axis.line.x.bottom=element_line(),
        axis.line.y.left=element_line(),
        panel.background = element_blank(),
        panel.grid.major = element_line(colour="light gray"),
        axis.text.y = element_text(face="bold",size=12 ))

#imputation 2 mean trip minutes plus standard deviation by sex
plot3<-ggplot(summary2a, aes(x=sex2, y=trip_min2_mean)) + 
  geom_point(stat="identity", size=3.5, color="black") +
  geom_errorbar(aes(ymin=xb1,ymax=xb2), width=.2, size=2, color="red",position=position_dodge(.8), alpha=0.7)+
  scale_x_discrete(name="sex") +
  geom_hline(data=summary_aa, aes(yintercept=trip_minutes_mean, color=sex),
             size=1,linetype="dashed")+
  ggtitle("Imputation 2")+
  scale_y_continuous(name="average trip in minutes(+/-) stdev",limits = c(-20,80), breaks=c(-20,0,20,40,60,80))+
  theme_minimal(base_size = 12) +
  scale_color_aaas()+
  theme(legend.position="top",
        legend.box.just = "center",
        #legend.box.background = element_rect(color="black", size=1),
        legend.text = element_text(size = 8, colour = "black"),
        legend.title = element_text(size=8, face="bold"),
        axis.title.y = element_text(size=16, face="bold"),
        axis.text.y.left = element_text(size=14, face="bold"),
        plot.title = element_text(hjust = 0.5, size=18, face="bold"),
        axis.text.x = element_text(face="bold",size=14),
        axis.title.x.bottom = element_text(size=14, face="bold"),
        axis.line.x.bottom=element_line(),
        axis.line.y.left=element_line(),
        panel.background = element_blank(),
        panel.grid.major = element_line(colour="light gray"),
        axis.text.y = element_text(face="bold",size=12 ))

#Imputation 3 mean trip minutes plus standard deviation by sex
plot4<-ggplot(summary3a, aes(x=sex3, y=tripmin3_mean)) + 
  geom_point(stat="identity", size=3.5, color="black") +
  geom_errorbar(aes(ymin=xc1,ymax=xc2), size=1.5, width=.2, color="orange",alpha=0.8,position=position_dodge(.9))+
  scale_x_discrete(name="sex") +
  geom_hline(data=summary_aa, aes(yintercept=trip_minutes_mean, color=sex),
             size=1,linetype="dashed")+
  scale_y_continuous(name="average trip in minutes (+/-) stdev",limits = c(-20,80), breaks=c(-20,0,20,40,60,80))+
  scale_color_aaas()+
  labs(color = "sex", alpha=0.6)+
  ggtitle("Imputation 3")+
  theme_minimal(base_size = 14) +
  theme(legend.position="top",
        legend.box.just = "center",
        #legend.box.background = element_rect(color="black", size=1),
        legend.text = element_text(size = 8, colour = "black"),
        legend.title = element_text(size=8, face="bold"),
        axis.title.y = element_text(size=16, face="bold"),
        axis.text.y.left = element_text(size=14, face="bold"),
        plot.title = element_text(hjust = 0.5, size=18, face="bold"),
        axis.text.x = element_text(face="bold",size=14),
        axis.title.x.bottom = element_text(size=14, face="bold"),
        axis.line.x.bottom=element_line(),
        axis.line.y.left=element_line(),
        panel.background = element_blank(),
        panel.grid.major = element_line(colour="light gray"),
        axis.text.y = element_text(face="bold",size=12 )) 

#putting all these graphs together, so they can be compared
grid.arrange(plot1,plot2, plot3, plot4, nrow = 1, ncol=4)

#performing independent t-tests to see if there was a significant difference in trip minutes
#I am not assuming equal variances since it's a safter assumption
#since 4 tests, alpha=0.05, 0.05/4, p must be less than 0.0125 for significance

#original data t-test for trip minutes by sex-->is significant
t0a<-t.test(chi_complete_overall2$trip_minutes ~ chi_complete_overall2$orig_sex, na.rm=FALSE) 

#imputation 1 t-test for trip min by sex-note that the difference is much larger, although the p-value is the same
t1a<-t.test(chi_complete_overall2$trip_minutes ~ chi_complete_overall2$imp_sex1, var.equal=FALSE) 

##imputation 2 t-test for trip min by sex-similar to last one
t2a<-t.test(chi_complete_overall2$trip_minutes ~ chi_complete_overall2$imp_sex2, var.equal=FALSE) 

##imputation 3 t-test for trip min by sex-diff similar to previous imputations
t3a<-t.test(chi_complete_overall2$trip_minutes ~chi_complete_overall2$imp_sex3, var.equal=FALSE) 

#Question 5 answer:imputation of sex did have an impact on detetcing differences in mean trip distance

#--------------------------------------------------------------------------------------------------------#

##Question 6: was there a significant change in the mean trip distance with sex?. 

#performing one sample t-test of mean trip minutes by sex with each imputation against 
#the mean of the original data

#data are already subsetted
#imputation 1 male trip distance versus original data set  for male-is sig
m1a<-t.test(ss1a$trip_min1, mu = 11.2 , alternative = "two.sided")

#imputation 1 female age versus original data set age for female- also sig
f1a<-t.test(ss1b$trip_min1, mu = 13.0 , alternative = "two.sided")

#also did log trip minutes by sex, it is hard to interpret though. 
m1b<-t.test(ss1a$log_trip_minutes, mu = 0.95 , alternative = "two.sided")
#performed log_trip min since it is skewed, more difficult to interpret
f1b<-t.test(ss1a$log_trip_minutes, mu = 1.018 , alternative = "two.sided")

#imputation 1 male trip min versus original data male trip min
m2a<-t.test(ss2a$trip_min2, mu = 11.2 , alternative = "two.sided")

#imputation 1 female trip min versus original data female trip min-is also sig
f2a<-t.test(ss2b$trip_min2, mu = 13.0 , alternative = "two.sided")


#imputation 3 male trip minutes versus trip minutes for male from the original dataset-sig
m4a<-t.test(ss4a$tripmin3, mu = 11.2 , alternative = "two.sided")

#imputation 3 female trip minutes versus trip minutes for female in original dataset-sig
f4a<-t.test(ss4b$tripmin3, mu = 13.0 , alternative = "two.sided")


#Answer question 6: There was a significant increase in the mean trip minutes for each sex compared 
#to the original data,making it easier to detect differences.




