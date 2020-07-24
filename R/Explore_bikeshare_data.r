
ny = read.csv('new_york_city.csv')
wash = read.csv('washington.csv')
chi = read.csv('chicago.csv')

head(ny)

head(wash)

head(chi)

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

##Loading relevant r-packages
library(magrittr)
library(dplyr)

##Finding the gender which spends the most riding time
average.travel.ny = ny %>% group_by(Gender) %>% summarise(Total.Trip.Duration = mean(Trip.Duration) )  
average.travel.ny

##Ploting a Pie Chart for the representation
slices = c(1811, 875.9785, 768.9179)
lbls = c("Unknown", "Female", "Male")
parts = round(slices)
lbls = paste(lbls, parts)
pie(slices,labels = lbls, col=rainbow(length(lbls)),
    main="Average Ride Time per trip by Gender")

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


##Reading the Chicago bikeshare data
chi = read.csv('chicago.csv')

##Loading relevant r-packages
library(magrittr)
library(dplyr)

##Finding the percentage of the top three start points and the rest out of the total data
total = nrow(chi)
numbik = c(210,140,120,total-(210+140+120))
    

    ##Using a function to find the percentage 
    numbik_to_percent = function(temp_N) {
      temp_P = (temp_N/total)*100
      return(temp_P)
    }

    ##Generating the values from the function
    slice_for_pie=numbik_to_percent(numbik)
    slice_for_pie

##Ploting a Pie Chart for the representation
slices = slice_for_pie
lbls = c("Clinton St & Washington Blvd", "Lake Shore Dr & Monroe St", "Streeter Dr & Grand Ave", "The Rest")

parts = round(slices/sum(slices)*100, digits=2)
lbls = paste(lbls, parts)
lbls = paste(lbls,"%",sep="")
pie(slices,labels = lbls, col=rainbow(length(lbls)),
    main="Percentage Representation of the Preferred Start Points")
legend("topright",legend=lbls, col=rainbow(length(lbls)),fill=rainbow(length(lbls)))


##Loading relevant r-packages
library(magrittr)
library(dplyr)



##Finding the user with the average ride per User Type
low.rides.wash = wash %>% group_by(User.Type) %>% summarise(Total.Trip.Duration = mean(Trip.Duration) )  
low.rides.wash

##Plotting a Bar Graph
numbik=c(2635,736)
barplot(numbik, main = "Total Ride Time of User Types", xlab = "User Type", ylab = "Total Time",las=1,names.arg = c("Customer","Subscriber") )



system('python -m nbconvert Explore_bikeshare_data.ipynb')
