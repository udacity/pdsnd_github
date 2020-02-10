### Date created
09 February 2020

### Project Title
bikeshare.py

### Description
## Bike Share Data

Over the past decade, bicycle-sharing systems have been growing in number and popularity in cities across the world. Bicycle-sharing systems allow users to rent bicycles on a very short-term basis for a price. This allows people to borrow a bike from point A and return it at point B, though they can also return it to the same location if they'd like to just go for a ride. Regardless, each bike can serve several users per day.

Thanks to the rise in information technologies, it is easy for a user of the system to access a dock within the system to unlock or return bicycles. These technologies also provide a wealth of data that can be used to explore how these bike-sharing systems are used.

In this project, you will use data provided by  [Motivate](https://www.motivateco.com/), a bike share system provider for many major cities in the United States, to uncover bike share usage patterns. You will compare the system usage between three large cities: Chicago, New York City, and Washington, DC.

## The Datasets

Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core  **six (6)**  columns:

-   Start Time (e.g., 2017-01-01 00:07:57)
-   End Time (e.g., 2017-01-01 00:20:53)
-   Trip Duration (in seconds - e.g., 776)
-   Start Station (e.g., Broadway & Barry Ave)
-   End Station (e.g., Sedgwick St & North Ave)
-   User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:

-   Gender
-   Birth Year

[](https://classroom.udacity.com/nanodegrees/nd104/parts/53470233-d93c-4a31-a59f-11388272fe6b/modules/0f8a717f-4ac2-49d7-9ac4-15ae692793fa/lessons/ee7d089a-4a92-4e5d-96d2-bb256fae28e9/concepts/87034580-6b86-4f45-9981-88f5c86d21bf#)

![](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/March/5aa771dc_nyc-data/nyc-data.png)

_Data for the first 10 rides in the  **new_york_city.csv**  file_

The original files are much larger and messier, and you don't need to download them, but they can be accessed here if you'd like to see them ([Chicago](https://www.divvybikes.com/system-data),  [New York City](https://www.citibikenyc.com/system-data),  [Washington](https://www.capitalbikeshare.com/system-data)). These files had more columns and they differed in format in many cases. Some  [data wrangling](https://en.wikipedia.org/wiki/Data_wrangling)  has been performed to condense these files to the above core six columns to make your analysis and the evaluation of your Python skills more straightforward. In the Data Wrangling course that comes later in the Data Analyst Nanodegree program, students learn how to wrangle the dirtiest, messiest datasets, so don't worry, you won't miss out on learning this important skill!

## Statistics Computed

You will learn about bike share use in Chicago, New York City, and Washington by computing a variety of descriptive statistics. In this project, you'll write code to provide the following information:

**#1 Popular times of travel**  (i.e., occurs most often in the start time)

-   most common month
-   most common day of week
-   most common hour of day

**#2 Popular stations and trip**

-   most common start station
-   most common end station
-   most common trip from start to end (i.e., most frequent combination of start station and end station)

**#3 Trip duration**

-   total travel time
-   average travel time

**#4 User info**

-   counts of each user type
-   counts of each gender (only available for NYC and Chicago)
-   earliest, most recent, most common year of birth (only available for NYC and Chicago)

## The Files

To answer these questions using Python, you will need to write a Python script. To help guide your work in this project, a template with helper code and comments is provided in a  **bikeshare.py**  file, and you will do your scripting in there also. You will need the three city dataset files too:

-   **chicago.csv**
-   **new_york_city.csv**
-   **washington.csv**

All four of these files are zipped up in the  **Bikeshare**  file in the resource tab in the sidebar on the left side of this page. You may download and open up that zip file to do your project work on your local machine.

Some versions of this project also include a Project Workspace page in the classroom where the bikeshare.py file and the city dataset files are all included, and you can do all your work with them there.


### Files used
chicago.csv
bikeshare.gitignore

Add links to any repo that inspired you or blogposts you consulted.
udacity learning classroom

