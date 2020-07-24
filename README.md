### Date created
Project was created on July 24th, 2020 and README file.

### Project Title
Project consists of the the works done on Udacity 


### Description
The Project is for the course on 'Programming for Data Science with R'. The first part used SQL to analyse a film rental data.
The second part used R to analyse a bikeshare data.

### Files used
Files used includes the Bikeshare Data for the Project on R. The Relational Database for the DVD Rentals were done using the Udacity Workspace

### Explore Bikeshare Data

Explore Bike Share Data
For this project, your goal is to ask and answer three questions about the available bikeshare data
from Washington, Chicago, and New York. 

##Below are the details of the work and the codes used

ny = read.csv('new_york_city.csv')
wash = read.csv('washington.csv')
chi = read.csv('chicago.csv')

head(ny)
head(wash)
head(chi)


Question 1

Which gender from New York spend the most total time riding? What is the average time spent
per ride by gender?

##Loading relevant r-packages
library(magrittr)
library(dplyr)

##Finding the gender with the most rides
highest.rider.ny = ny %>% group_by(Gender) %>% summarise(Total.Trip.Duration = sum(Trip.Duration) )
highest.rider.ny

##Ploting a Pie Chart for the representation
slices = c(52884891, 59218793, 157801564)
lbls = c("Unknown", "Female", "Male")
parts = round(slices/sum(slices)*100)
lbls = paste(lbls, parts)
lbls = paste(lbls,"%",sep="")
pie(slices,labels = lbls, col=rainbow(length(lbls)),
main="Total Ride Time by Gender")


Question 2

What are the top three start locations that bikers in Chicago frequently start their riding journey?
Based on the proportion of trips starting from there, are they the favourite starting points for bike
trips in Chicago?

##Reading the Chicago bikeshare data
chi = read.csv('chicago.csv')

##Loading relevant r-packages
library(magrittr)
library(dplyr)

##Finding the top three(3) favourite Start Stations
oldest.rider.chi = chi %>% group_by(Start.Station) %>% summarise(Number.of.bike.trips=n())
arranged.oldest.rider.chi=oldest.rider.chi %>% arrange(desc(Number.of.bike.trips))
top.arranged.oldest.rider.chi = arranged.oldest.rider.chi %>% top_n(3)
top.arranged.oldest.rider.chi

##Plotting a Bar Graph
numbik = c(210,140,120)
barplot(numbik, main = "Top Three Start Points", xlab = "Number of Starts", ylab = "Station", horiz=T, xlim = c(0,250), col=c("red2", "green3", "slateblue4"),legend.text = c("Streeter Dr & Grand Ave","Lake Shore Dr & Monroe St","Clinton St & Washington Blvd"),args.legend=list(cex=0.75,x="topright") )


Question 3
Which type of rider from Washington rides less?

##Loading relevant r-packages
library(magrittr)
library(dplyr)

##Finding the user with the average ride per User Type
low.rides.wash = wash %>% group_by(User.Type) %>% summarise(Total.Trip.Duration = mean(Trip.Duration) )
low.rides.wash

##Plotting a Bar Graph
numbik=c(2635,736)
barplot(numbik, main = "Total Ride Time of User Types", xlab = "User Type", ylab = "Total Time",las=1,names.arg = c("Customer","Subscriber") )


