# SKJHA Bikeshare Project. Code formatted using Black Playground - https://black.now.sh/
# Referred to these resources when got stuck on some coding issues- Udacity modules and peer chat, Stackoverflow.com, W3Schools.com
# Revised version now prints 5 new rows of data everytime the user selects- yes
import time
import pandas as pd
import numpy as np


CITY_DATA = {
    "chicago": "chicago.csv",
    "new york city": "new_york_city.csv",
    "washington": "washington.csv",
}
# Gets input from the user for the city, month and day data user is interested in
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print("Hello! Let's explore some US bikeshare data!")

    # Get user input for city (chicago, new york city, washington)
    while True:
        city = input(
            "Hello! Which city do you live in? Chicago, New York city or Washington?\n"
        )
        city = city.lower()  # converts the input into lower case
        if city not in ("chicago", "new york city", "washington"):
            print("Not an appropriate choice. Please try again.\n")
        else:
            break

    # Get user input for month (all, january, february, ... , june)

    while True:
        month = input(
            "Thanks! Please enter the month: 'All' for all available months or enter any month from January through June.\n"
        )
        month = month.lower()  # converts the input into lower case
        if month not in ("all", "january", "february", "march", "april", "may", "june"):
            print("Not an appropriate choice. Please try again\n")
        else:
            break

    # Get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day = input(
            "Thanks! Please enter the day of the week: 'All' for all week days, or enter any day from Monday to Sunday\n"
        )
        day = day.lower()  # converts the input into lower case
        if day not in (
            "all",
            "monday",
            "tuesday",
            "wednesday",
            "thursday",
            "friday",
            "saturday",
            "sunday",
        ):
            print("Not an appropriate choice. Please try again\n")
        else:
            break

    print("-" * 40)
    return city, month, day


# Loads the data into this function to read from the specific city file and creates the data frame.
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # Load city data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # Convert the Start Time column to datetime
    df["Start Time"] = pd.to_datetime(
        df["Start Time"]
    )

    # converts End Time to datetime64[ns] datatype
    df["End Time"] = pd.to_datetime(
        df["End Time"]
    )

    # Extract month from Start Time to create new columns
    df["month"] = df[
        "Start Time"
    ].dt.month

    # Extract the day from the Start Time Column and creates new day_of_week column
    df["day_of_week"] = df[
        "Start Time"
    ].dt.weekday_name

    # Filter by month if applicable
    if month != "all":
        # Use the index of the months list to get the corresponding int
        months = ["january", "february", "march", "april", "may", "june"]
        month = months.index(month) + 1

        # Filter by month to create the new dataframe
        # Changes the month from the word to the integer
        df = df[df["month"] == month]

    # Filter by day of week if applicable
    if day != "all":

        # Filter by day of week to create the new dataframe
        df = df[df["day_of_week"] == day.title()]

    return df


# Asks the user if they want to see raw data. If yes, return the  5 new rows of the data everytime.
    """
    Asks the user if they want to see raw data. Displays first 5 rows of the raw data

    Args:
        df - Pandas DataFrame containing city data filtered by month and day
    Returns:
        for yes: df - Pandas dataframe with all the columns and the first 5 rows
        for no: (str) - prints message that calculations will now be performed
    """
    while True:
      display_data = input("Do you want to see first 5 lines of the data?. Please type 'yes' or 'no'\n")
      if display_data not in ('yes', 'no'):
        print("Not the right choice. Try again.\n")
      while True:
          display_data = input(
      "Do you want to see 5 more lines of the data?. Please type 'yes' or 'no'\n"
          )
          if display_data == "yes":
              df = df.iloc[4:]
              print(df.head())

          elif display_data == "no":
              print("Thanks! Continuing to calculations.\n")
              break
      break

def time_stats(df):
    """
    Displays statistics on the most frequent times of travel.
    Changes the user input of month in words to the corresponding integer number.

    Args:
        df - Pandas DataFrame containing city data filtered by month and day
    Returns:
        (int64) - month
        (int64) - hour
        object - day_of_week (eg.: friday) based on (int64) - max counts for day_of_week
    """

    print("\nCalculating The Most Frequent Times of Travel...\n")
    start_time = time.time()

    # Display the most common month
    months = ["january", "february", "march", "april", "may", "june"]
    month = df["month"].mode()[0] - 1
    popular_month = months[
        month
    ].title()  # converts the month number to month word (eg.: number 3 converted to March after decreasing the index by 1)

    # Display the most common day of week
    popular_week_day = df.groupby(["day_of_week"]).size().nlargest(1)

    # Display the most common start hour
    df["hour"] = df["Start Time"].dt.hour
    popular_hour = df["hour"].mode()[0]
    print("Popular Month: ", popular_month)
    print("Popular Start Hour: ", popular_hour)
    print("Popular Week Day: ", popular_week_day.idxmax())
    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip.

    Args:
       df - Pandas DataFrame containing city data filtered by month and day
    Output:
       (int64) - max count of start station
       object -  Start Station (eg.: Clinton St & Washington Blvd)
       (int64) - max count of End Station
       object - End station (eg.: Clinton St & Washington Blvd)
       (int64): max count of combination Start and End Stations
       object - Start and End Stations (eg.: 'Streeter Dr & Grand Ave', 'Streeter Dr & Grand Ave')
    """

    print("\nCalculating The Most Popular Stations and Trip...\n")
    start_time = time.time()

    # TO DO: display most commonly used start station
    # retuns the counts of the start station and then returns the station name with the maximum total counts

    start_station = df.groupby(["Start Station"]).size().nlargest(1)

    # TO DO: display most commonly used end station
    # Returns the counts of the start station and then returns the station name with the maximum total counts

    end_station = df.groupby(["End Station"]).size().nlargest(1)

    # TO DO: display most frequent combination of start station and end station trip
    # Returns the most frequent combination of the start and end station. Referred to Udacity peer chat to understand and get the correct code
    combination_end_start_station = (
        df.groupby(["Start Station", "End Station"]).size().nlargest(1)
    )

    print("Most common start station: ", start_station.idxmax())
    print("Most common end station: ", end_station.idxmax())
    print(
        "Most common start and end station:\n ", combination_end_start_station.idxmax()
    )
    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


# Function to convert seconds into days, hours, minutes and seconds. Looked up various formaulas on https://www.stackoverflow.com/
def convert(seconds):
    """
    Converts Trip Duration values(which are in seconds) to days, hours, minutes and seconds.

    Args:
       (int64) - time in seconds
    Returns:
       (str) - day, hours, mins, secs for time value
    """

    min, sec = divmod(seconds, 60)
    hour, min = divmod(min, 60)
    day, hour = divmod(hour, 24)
    if day == 0:
        return "%d:%02d:%02d" % (hour, min, sec)
    return ("%d days and  " + "%d:%02d:%02d") % (day, hour, min, sec)


def trip_duration_stats(df):
    """
    Displays statistics on the total and average trip duration.

    Args:
       df - Pandas DataFrame containing city data filtered by month and day
       function - convert to convert trip duration values to days, hours, mins, secs
    Returns:
       (str) - day, hours, mins, secs for total trip duration value
       (str) - day, hours, mins, secs for total trip duration value
    """

    print("\nCalculating Trip Duration...\n")
    start_time = time.time()

    # Display total travel time
    # Converts the Trip Duration to datatype int64. Calculates the sum of all the trip durations
    df["Trip Duration"] = df["Trip Duration"].astype(int)
    total_travel_duration = df["Trip Duration"].sum()
    # Calls the convert function
    new_total_trip_duration = convert(total_travel_duration)

    # Display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    new_mean_travel_time = convert(mean_travel_time)

    print(
        "\nThe total travel time was: ", new_total_trip_duration + " hours: mins: secs"
    )
    print("\nThe mean travel time was: ", new_mean_travel_time + " hours: mins: secs")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def user_stats(df):
    """
    Displays statistics on bikeshare users.

    Args:
       df - Pandas DataFrame containing city data filtered by month and day

    Returns:
       (int64) - max counts of all User Type
       object - value of all user types
       (int64) - counts of Gender by values
       object - Gender values
       (int64) - value of Trip Duration which is the most common
       object - value of most common User Type
       (int64) - value of earliest Birth Year
       (int64) - value of most recent Birth Year
       (int64) - value of the most common Birth Year
    """

    print("\nCalculating User Stats...\n")
    start_time = time.time()

    # Display counts of user types
    user_types = df["User Type"].value_counts()

    # Display counts of gender
    if "Gender" in df:
        gender_types = df["Gender"].value_counts()

    else:
        gender_types = "Data not available"

    # Display earliest, most recent, and most common year of birth
    if "Birth Year" in df:
        earliest_birth_year = df["Birth Year"].min().round().astype(int)
        most_recent_birth_year = df["Birth Year"].max().round().astype(int)
        most_common_birth_year = df["Birth Year"].value_counts().idxmax().astype(int)

    else:
        earliest_birth_year = "Data not available"
        most_recent_birth_year = "Data not available"
        most_common_birth_year = "Data not available"

    print("\nThe various user types and their counts are:\n", user_types)
    print("\nThe various gender types and their counts are:\n", gender_types)
    print("\nThe earliest birth year was: ", earliest_birth_year)
    print("\nThe most recent birth year was: ", most_recent_birth_year)
    print("\nThe most common birth year was: ", most_common_birth_year)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)

# Added an additional function display_raw_data() and also inlcuded a print for printing dataframe datatypes
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        display_raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        print("DATAFRAME COLUMN DATATYPES\n")
        print("-" * 40)
        print(df.dtypes) # Allows user to see the datatypes for each Column in Dataframe

        restart = input("\nWould you like to restart? Enter yes or no.\n")
        if restart.lower() != "yes":
            break


if __name__ == "__main__":
    main()
