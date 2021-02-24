# Explore US Bikeshare Data

## Overview
In this project, I used Python to explore data related to bike share systems for three major cities in the United States — Chicago, New York City, and Washington. It is required to write a code to (a) import the data and answer interesting questions about it by computing descriptive statistics, and (b) write a script that takes in raw input to create an interactive experience in the terminal to present these statistics.

## Project Submission
The developed CLI program allows the user to explore an US bikeshare system database and retrieve statistics information from the database. The user is able filter the information by city, month and weekday, in order to visualize statistics information related to a specific subset of data. The user is also able to chose to view raw data and to sort this data by columns, in ascending or descending order.

## How to run the script?
You can run the script using a Python integrated development environment (IDE) such as Spyder, or any other text editor. Personally I used [Atom](https://atom.io/) software. This script is written in Python 3, so you will need the [Python 3.x](https://www.python.org/downloads/) version of the installer. You will also need a terminal application to run the written script on it.

### Requirements
This program was written in Python (version 3.7.1) and relies on the following libraries:
- pandas==0.23.4
- numpy==1.15.4

## Datasets
The datasets used for this script contain bike share data for the first six months of 2017. Some data wrangling has been performed by Udacity's staff before being provided to the students of the nanodegree. The data is provided by [Motivate](https://www.motivateco.com/), which is a bike share system provider for many cities in the United States. The data files for all three cities contain the same six columns:
- Start Time
- End Time
- Trip Duration (in seconds)
- Start Station
- End Station
- User Type (Subscriber or Customer)

The Chicago and New York City files also contain the following two columns:
- Gender
- Birth Year

### Files Used

The required files for running this program are:
* washington.csv
* new_york_city.csv
* chicago.csv

## Questions explored
The script answers the following questions about the bike share data:
* What is the most popular month for start time?
* What is the most popular day of week (Monday, Tuesday, etc.) for start time?
* What is the most popular hour of day for start time?
* What is the total trip duration and average trip duration?
* What is the most popular start station and most popular end station?
* What is the most popular trip?
* What are the counts of each user type?
* What are the counts of gender?
* What are the earliest (i.e. oldest person), most recent (i.e. youngest person), and most popular birth years?
