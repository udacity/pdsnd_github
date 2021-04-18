# Project Title
US Bikeshare Data Analysis Project

## Date created
April 17, 2021

## Description
This Python script is written for Project 2 of Udacity's Data Analyst Nanodegree and is used to explore data related to bikeshare systems for Chicago, New York City, and Washington. It imports data from csv files and computes descriptive statistics from the data. It also takes in users' raw input to create an interactive experience in the terminal to present these statistics.

## Files used
### python file:
---------------------------
	* bikeshare.py
---------------------------

### csv files:	
---------------------------
[csv_data](https://drive.google.com/drive/folders/1_W0hCnaJucHeIy-G0esooo9oHDI8eMID?usp=sharing)
	* chicago.csv
	* new_york_city.csv
	* washington.csv
---------------------------

## **Code explained in Detail:**
### **How the program works:**
The code developed takes in raw input to create an interactive experience in the terminal that answers questions about the dataset. The experience is interactive because depending on a user's input, the answers to the questions will change! There are four questions that will change the answers:

* Would you like to see data for _Chicago_, _New York_, or _Washington_?
* Would you like to filter the data by month, day, or not at all?
* (If they chose month) Which month - _January_, _February_, _March_, _April_, _May_, or _June_?
* (If they chose day) Which day - _Monday_, _Tuesday_, _Wednesday_, _Thursday_, _Friday_, _Saturday_, or _Sunday_?

The answers to the questions above will determine the city and timeframe on which you'll do data analysis. After filtering the dataset, users will see the statistical result of the data, and choose to start again or exit.

### **The Datasets:**
Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:

* Start Time (e.g., 2017-01-01 00:07:57)
* End Time (e.g., 2017-01-01 00:20:53)
* Trip Duration (in seconds - e.g., 776)
* Start Station (e.g., Broadway & Barry Ave)
* End Station (e.g., Sedgwick St & North Ave)
* User Type (Subscriber or Customer)

The _Chicago_ and _New York City_ files also have the following two columns:

* Gender
* Birth Year

### **Statistics Computed:**
The code helps user to tell about bike share use in _Chicago_, _New York City_ and _Washington_ by computing a variety of descriptive statistics. In this project, the code output will provide the following information:

* Popular times of travel (i.e., occurs most often in the start time):

  - most common month
  - most common day of week
  - most common hour of day

* Popular stations and trip:

  - most common start station
  - most common end station
  - most common trip from start to end (i.e., most frequent combination of start station and end station)

* Trip duration:

  - total travel time
  - average travel time

* User info:

  - counts of each user type
  - counts of each gender (only available for _NYC_ and _Chicago_)
  - earliest, most recent, most common year of birth (only available for _NYC_ and _Chicago_)

## Credits

Richard Kalehoff (Udacity mentor):
-------------------------------------------
	[github](https://github.com/richardkalehoff)
	[twitter](https://twitter.com/richardkalehoff)
-------------------------------------------

Juno Lee (Udacity Mentor):
-------------------------------------------
	[github](https://github.com/junolee)
	[twitter](https://www.linkedin.com/in/junoleelj)
-------------------------------------------

