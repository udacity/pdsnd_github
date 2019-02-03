John Meehan
January 22nd 2019

Data analysis performed on Bikeshare CSV's

#1 Filter data (city, month, and day of week) based on user input

#2 Display raw data of filtered data

>allow user to see 5 additional lines at each prompt

#3 Popular times of travel (i.e., occurs most often in the start time)

>most common month
>most common day of week
>most common hour of day

#4 Popular stations and trip

>most common start station
>most common end station
>most common trip from start to end (i.e., most frequent combination of start station and end station)
 Additional resources used:
    >https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.idxmax.html
    >Needed to figure out how to display only the stations from the most
    >popular station combination.

#3 Trip duration

>total travel time
>average travel time

#4 User info

>counts of each user type
>counts of each gender (only available for NYC and Chicago)
>earliest, most recent, most common year of birth (only available for NYC and Chicago)

 #5 User stat plot

 >scatterplot of trip duration vs. user age
  Additional resources used:
    >https://stackoverflow.com/questions/20130227/matplotlib-connect-scatterplot-points-with-line-python
    >Wanted to display a scatterplot using bike share data
    >https://matplotlib.org/tutorials/introductory/pyplot.html
