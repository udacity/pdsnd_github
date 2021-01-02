### Project Created Dtae  
This project was crated on 11th December, 2020 and the README.md file was created on 2nd January, 2021.

### Basic Data Exploration with pandas on Bikeshare Data
Basic Udacity project using pandas library in Python for their bikeshare data exploration.

### Project Overview
Use Python to explore data related to bicycle sharing systems in three major US cities: Chicago, New York, and Washington, DC. Write code to import data and answer interesting questions by calculating descriptive statistics. Write a script that accepts the original input and creates an interactive experience in the terminal to present these statistics.

###Running the program:
You can input 'python bikeshare.py' on your terminal to run this program. I use Anaconda's command prompt on a Windows 8.1 machine.

###Program Details:
The program takes user input for the city (e.g. Chicago), month for which the user wants to view data (e.g. January; also includes an 'all' option), and day for which the user wants to view data (e.g. Monday; also includes an 'all' option).
Upon receiving the user input, it goes ahead and asks the user if they want to view the raw data (5 rows of data initially) or not. Following the input received, the program prints the following details:
1. Which month is the most common in the start time (Start Time column)?
2. Which day of the week (such as Monday, Tuesday) is the most common in the starting time?
3. Which hour of the day is most common during the start time?
4. How long is the Trip Duration and how long is the average ride duration?
5. Which Start Station is the most popular, and which end station is the most popular?
6. Which one is the most popular (ie, which combination of the starting and ending sites is the most popular)?
7. How many people are there for each user type?
8. How many people are there for each gender?
9. Which year is the earliest year of birth, and which year is the latest. Which year is the most common?

Finally, the user is prompted with the choice of restarting the program or not.

### Project Data set
Data for the first half of 2017 for three cities was provided. The three data files all contain the same core six columns:
Start time Start Time (eg 2017-01-01 00:07:57)
End time End Time (eg 2017-01-01 00:20:53)
Duration of the ride Trip Duration (for example, 776 seconds)
Start station Start Station (eg Broadway Street and Barry Avenue)
End station End Station (eg Sedgwick Street and North Avenue)
User Type User Type (Subscriber Subscriber/Registered or Customer Customer/Casual)
The Chicago and New York City files also contain the following two columns (the data format can be viewed below):
Gender Gender
Year of Birth Birth Year

Built with:
•	Python 3.6.6 - The language used to develop this.
•	pandas - One of the libraries used for this.
•	numpy - One of the libraries used for this.
•	time - One of the libraries used for this.

Author:
•	Mastaer_Math - Sole author for this program. Mentioned all the help received in 'Acknowledgements' section.

### Acknowledgements
•	Aritra96 - Aritra96's repository helped with understanding the structure and details of certain functions.
•	pandas docs - pandas documentation was immensely helpful in understanding the implemention of pandas methods used in this project.
•	Udacity - Udacity's Data Analyst Nanodegree program and their instructors were extremely helpful while I was pursuing this project.
