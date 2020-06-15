import time
import pandas as pd
import numpy as np
import sys
import datetime

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
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    # Defind arrays to valid the choices of the user 
    cities = ["chicago", "new york city", "washington"]    
    months = ["february","march","april","may","june","july","august","september","october","november","december"]
    days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
    
    # Validation Varabile 
    valid = False
    
    # loop for taking the days input from the user and validate it
    while(not valid):
        valid = True
        day = input("Enter a day: ").strip().lower()
        if day not in days:
            valid= False
            print("Day not found, try again")
            
    # Validation Varabile
    valid = False
    
    # loop for taking the city input from the user and validate it
    while(not valid):
        valid = True
        city = input("Enter a city: ").strip().lower()
        if city not in cities:
            valid = False
            print("city not found, try again")
    
    # Validation Varabile
    valid = False
    
    # loop for taking the month input from the user and validate it
    while(not valid):
        valid = True
        month = input("Enter a month: ").strip().lower()
        if month not in months:
            valid = False
            print("month not found, try again")
    
    # TO DO: get user input for month (all, january, february, ... , june)


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)


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
    
    # reads the csv file
    df = pd.read_csv(city+'.csv')
    
    #make month and day column using datetime() to extract month and day from start time
    df["Month"] = df['Start Time'].apply(lambda x : datetime.datetime.strptime(x,'%Y-%m-%d %H:%M:%S').strftime('%B').lower())
    df["Day"] = df['Start Time'].apply(lambda x : datetime.datetime.strptime(x,'%Y-%m-%d %H:%M:%S').strftime('%A').lower())
    
    # filter the data frame with the designated user input  
    df = df[df['Month']==month]
    df = df[df['Day']==day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    
    #Using the value_counts function and taking the first head from the list 
    print("Most common month is: ", df['Month'].value_counts().head(1).to_string()) 
    # TO DO: display the most common day of week
    
    #Using the value_counts function and taking the first head from the list
    print("Most common day is: ", df['Day'].value_counts().head(1).to_string())
    # TO DO: display the most common start hour
    
    #make an hour column using datetime() to extract month and day from start time
    df["Hour"] = df['Start Time'].apply(lambda x : datetime.datetime.strptime(x,'%Y-%m-%d %H:%M:%S').strftime('%H'))
    
    #Using the value_counts function and taking the first head from the list
    print("Most common hour is: ", df['Hour'].value_counts().head(1).to_string())
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    
    #Using the value_counts function and taking the first head from the list
    print("Most common Start Station is: ", df['Start Station'].value_counts().head(1).to_string())

    # TO DO: display most commonly used end station
    
    #Using the value_counts function and taking the first head from the list
    print("Most common End Station is: ", df['End Station'].value_counts().head(1).to_string())

    # TO DO: display most frequent combination of start station and end station trip
    
    #Making a temp variable to merge both end and start values into one variable
    tmp = df['Start Station']+','+df['End Station']
    
    #Using the value_counts function and taking the first head from the list
    print("Most frequent combination of start and end Stations are: ", tmp.value_counts().head(1).to_string())
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    
    #Calculating the sum trip duration using sum()
    print("Total Travle Time = ",df["Trip Duration"].sum())
   

    # TO DO: display mean travel time
    
    #Calculating the sum trip duration using sum()
    print("Mean Travle Time = ",df["Trip Duration"].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
    #Using the value_counts function 
    print("Counts of user types: ",df['User Type'].value_counts().to_string())

    # TO DO: Display counts of gender
    
    #Using the value_counts function 
    print("Counts of gender: ",df['Gender'].value_counts().to_string())

    # TO DO: Display earliest, most recent, and most common year of birth
    
    #Using the min function 
    print("Earliest Birth: ",df['Birth Year'].min())
    #Using the max function
    print("Most Recent Birth: ",df['Birth Year'].max())
    #Using the value_counts function and taking the first head from the list
    print("Most Common Birth: ",df['Birth Year'].value_counts().head(1).to_string())
                                        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        answer = input("Do you want to see raw data? (y/n): ")
        if answer == "y":
            print(df.head())
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
