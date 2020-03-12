### Date created
12th March 2020

### Project Title
US Bikeshare Data Project

### Description
In this project, I will make use of Python to explore data related to bike share systems for three major cities in the United States—Chicago, New York City, and Washington. I used python code to import the data and answered interesting questions about it by computing descriptive statistics.I was able to also write a script that takes in raw input to create an interactive experience in the terminal to present these statistics. Some of the stats that will be displayed include:

1. Popular times of travel (i.e., occurs most often in the start time)
  * most common month,
  * most common day of week,
  * most common hour of day,

2. Popular stations and trip:
  * most common start station,
  * most common end station,
  * most common trip from start to end (i.e., most frequent combination of start station and end station).

3. Trip duration:
  * total travel time,
  * average travel time.

4. User info:
  * counts of each user type,
  * counts of each gender (only available for NYC and Chicago),
  * earliest, most recent, most common year of birth (only available for NYC and Chicago),

5. Displaying 5 rows of data at a time to enable users to view raw data from these cities.

### Files used
* chicago.csv,
* new_york_city.csv,
* washington.csv.

### Credits
A. Before running bikeshare.py please run this in terminal
* $ pip install bullet

Menus depend on bullet library and thus the need to install it.

Bullet library was gotten from:
https://github.com/Mckinsey666/bullet/blob/master/examples/star.py

B. I used code from lectures on Project to develop my 'load_data(city, month, day)' function

C. To be able to effectively display most frequent combination of start station and end station trip, I used information from:
https://knowledge.udacity.com/questions/74297

D. To be able to effectively display most user stats for all cities including Washington which lacked a column for 'Gender' and 'Birth Year' I used code to develop the 'def user_stats(df,city)' function  from:
https://github.com/Ramya-PR/Python_projects/blob/master/bikeshare/bikeshare.py

E. Developed the function def more_stats(df,city) by using some of the code from:
1. https://stackoverflow.com/questions/22362165/i-want-to-have-a-yes-no-loop-in-my-code-but-im-having-trouble-doing-it-python

2. https://github.com/Ramya-PR/Python_projects/blob/master/bikeshare/bikeshare.

