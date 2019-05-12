### Date created
May 11, 2019

### Project Title
Udacity BikeShare project using python and git

### Description
Analyse bikeshare data from [Motivate]( https://www.motivateco.com/) using python along with git to gather data from the files.

### Files used
Bikeshare files (https://s3.amazonaws.com/video.udacity-data.com/topher/2018/March/5aab379c_bikeshare-2/bikeshare-2.zip)
Includes `bikeshare.py`, a udacity template to assist students with their project. Data files in csv format, _`chicago.csv`_, _`washington.csv`_, _`new york city.csv`_ can be accessed in the bikeshare files.

### My Files Included
Included all the files related to my work with the [Udacity](https://www.udacity.com/) bikeshare project.  Some python files, such as [city_input.py](udacity_project/city_input.py) or [user_types.py](udacity_project/user_types.py), show my attempts at gathering and interpreting aspects of the data files. The files with [bp](udacity_project/bp5.py), [bs](udacity_project/bs_4.py), [bikeshare](udacity_project/bikeshare_2.py), or [bike_project](udacity_project/bike_project.py) show the various ways I tried to put the data gathered from the city files and represent it in a form that could be understood by the user.

### Project Submission
The final [project_submission](udacity_project/project_submission.py) takes 3 user inputs: **City**, **Month** and **Day**.  After processing the inputs the program returns information related to:
1. trip duration
1. gender stats
1. stations beginning and end
1. popular days and months

### Credits
I used many examples from [pandas](https://pandas.pydata.org/pandas-docs/stable/) and [numpy][https://docs.scipy.org/doc/numpy-1.13.0/contents.html] documentation.  
I explored questions already asked in [Stackoverflow](https://stackoverflow.com/) to find examples.
[Jonathonsoma.com](http://jonathansoma.com/), classnotes on replacing values and strings helped with filling in missing values from washington.csv, on bikeshare lines 121 to 127.
[towardsdatascience.com](towardsdatascience.com), data cleaning with python and pandas:detecting missing values. An article on Oct 5, 2018, helped me explore data and missing values

#### Future Features
1. add plots
2. run in html window
3. compare multiple city data
