import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    month_chickList=["all", "january", "february","march","april","may","june"]
    day_chickList=["all", "monday", "tuesday","wednesday", "thursday","friday","saturday","sunday"]
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Please Enter city Name (chicago, new york city, washington) : \n ").lower()
    while city not in CITY_DATA.keys():
        print("Incorrect input ... \n")
        print("You should Enter city of this list :[chicago, new york city or  washington] \n")
        city = input("Please Enter city Name (chicago, new york city, washington) : \n ").lower()

        # get user input for month (all, january, february, ... , june)

    while True:

        month = input("Please Enter name of the month to filter by, or (all) to apply no month filter : \n ").lower()
        if month in month_chickList:

            break
        else:

            print("Incorrect input! \n")
            print("You should enter month between (january and june )to filtre  or (all)  to apply no month filter\n")
        # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:

        day= input("Please Enter name of the day of week to filter by, or (all) to apply no day filter: \n ").lower()

        if day in day_chickList:
            break
        else:

            print("Incorrect input , please check your input day   \n")
            print("please enter the correct day to filter or all to apply no filter : \n  ")

    print('-'*40)
    return city, month, day


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
    print("Data is loading now ...\n")
    df = pd.read_csv(CITY_DATA[city])
    df["Start Time"]=pd.to_datetime( df["Start Time"])
    df["Month"]= df["Start Time"].dt.month
    df["Day of week"]=df["Start Time"].dt.day_name()

    if month != "all" :
        month_chickList = ["january", "february", "march", "april", "may", "june"]
        # filter by Month to create the new dataframe

        month = month_chickList.index(month)+1
        df = df.loc[df["Month"] == month]


    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df.loc[df["Day of week"] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df["Start Time"]=pd.to_datetime(df["Start Time"])

    # display the most common month

    most_commonMonth = df["Month"].mode()[0]
    print("The most common month is : ",most_commonMonth )

    # display the most common day of week

    most_commonDay = df["Day of week"].mode()[0]
    print("\n The most common day is : ", most_commonDay)

    # display the most common start hour
    df['Hour']=df["Start Time"].dt.hour
    most_commonHour=df['Hour'].mode()[0]
    print("\nThe most common hour is : ", most_commonHour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    commonUsed_startStation=df["Start Station"].mode()[0]
    print("The most most commonly used start station is : " ,commonUsed_startStation)
    # display most commonly used end station
    commonUsed_endStation = df["End Station"].mode()[0]
    print("\nThe most most commonly used end station is : ",  commonUsed_endStation )


    # display most frequent combination of start station and end station trip
    #df["Combination ٍٍStations"]=
    most_combination_station=(df["Start Station"] +" : " +df["End Station"]).mode()[0]
    print("\n The  most frequent combination of start station and end station trip is :  ",most_combination_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travelTime=df["Trip Duration"].sum()
    print("Total travel time is : ",total_travelTime )


    # display mean travel time
    mean_travelTime=df["Trip Duration"].mean()
    print("Average travel time is  : " ,mean_travelTime)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    user_types_count=df["User Type"].value_counts()
    print("Counts of user types customer\subscriber is :\n " ,user_types_count)

    # Display counts of gender
    try:
        gender_count = df["Gender"].value_counts()
        print("\nCounts of gender is :\n",gender_count)
    except:
        print("\n No such column that contains the gender data for this city \n")


    # Display earliest, most recent, and most common year of birth
    try:
        earliest_year=int(df["Birth Year"].min())
        print("The earliest year of birth is : ",earliest_year)
        most_recent_year=int(df["Birth Year"].max())
        print("\nThe most recent year of birth is : " ,most_recent_year )
        most_common_year=int(df["Birth Year"].mode()[0])
        print("\nThe most common year of birth is : ",most_common_year)
    except:
        print("\n No such column that contains year birth data for this city \n")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def display_raw_data(df):

    #The fuction takes the name of the city produced by the get_filters fuction as
    #input and returns the raw data of that city as chunks of 5 rows based upon user input.

    print("\nRaw data is available to check... \n")
    count=0
    while True:
        userInput = input("Do you want display more 5 rows of data yes or no : ").lower()
        if userInput not in ["yes","no"]:
            print("\nInvalid input please enter yes or no \n")
        elif userInput =="yes":
            print(df.iloc[count:count+5])
            count+=5
        elif userInput=="no":
            print("\nthanks for your time ^_^")
            print("\n ----we wish using this application again--- ")
            print("\nExisting ...\n")
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
