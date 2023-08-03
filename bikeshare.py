import time
import datetime
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'newyork': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

        

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
    while True:
        try:# Insusceptibility to white spaces in-between input letters and whatever letter cases!
            # i.e: (New York = newyork = NeWyoRK = N  ew YO   r k)
            city = input('Enter City Name "Chicago", "New York", "Washington": ').lower().replace(' ', '')
            # If input isn't exist within City_DATA Keys, raise an exception and prompt for a new input!
            if city not in CITY_DATA:
                raise Exception
            break
        except:
            print('Invalid Input!!')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:# Insusceptibility to white spaces in-between input letters and whatever letter cases!
            # i.e: (January = january = jAnUArY = j  an U a Ry   )
            month = input('Enter Month(s) value "january", "February", ... , "June" or "All": ').lower().replace(' ', '')
            # If input isn't exist within months list, raise an exception and prompt for a new input!
            if month not in months:
                raise Exception
            break
        except:
            print('Invalid Input!!')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:# Insusceptibility to white spaces in-between input letters and whatever letter cases!
            # i.e: (Monday = monday = MoNdAy = M  on D a   y )
            day = input('Enter Day value "Monday", "Tuesday", ... , "Sunday" or "All": ').lower().replace(' ', '')
            # If input isn't exist within days list, raise an exception and prompt for a new input!
            if day not in days:
                raise Exception
            break
        except:
            print('Invalid Input!!')

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
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA.get(city))

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, day of week and Hour from Start Time to create new columns
    df['hour'] = df['Start Time'].dt.hour
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == days.index(day)]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = (df['month'].mode())[0]
    print('Most Common Month:', months[common_month - 1].title())

    # TO DO: display the most common day of week
    common_day_of_week = (df['day_of_week'].mode())[0]
    print('Most Common Day Of Week:', days[common_day_of_week].title())

    # TO DO: display the most common start hour
    common_start_hour = (df['hour'].mode())[0]
    print('Most Common Start Hour:', common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = (df['Start Station'].mode())[0]
    print('Most Common Start Station:', common_start_station)
    
    # TO DO: display most commonly used end station
    common_end_station = (df['End Station'].mode())[0]
    print('Most Common End Station:', common_end_station)
    
    # TO DO: display most frequent combination of start station and end station trip
    most_start_and_end_station = (df['Start Station']).str.cat(df['End Station'], sep=" to ").mode()[0]
    print('Most Frequent Combination of Start Station & End Station Trip:', most_start_and_end_station)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    # Get the sum in (sec) then convert it to a comprehensive time format!
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time:', datetime.timedelta(seconds = int(total_travel_time)))
    
    # TO DO: display mean travel time
    # Get the average in (sec) then convert it to a comprehensive time format!
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time:', datetime.timedelta(seconds = int(mean_travel_time)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_of_user_types = df['User Type'].value_counts()
    print('Counts of User Type:')
    print(counts_of_user_types)

    # TO DO: Display counts of gender 
    # Only New York City and Chicago have 'Gender' and 'Year of Birth' Columns!
    if (city != 'washington'):
        counts_of_gender = df['Gender'].value_counts()
        print('\nCounts of Gender:')
        print(counts_of_gender)

    # TO DO: Display earliest, most recent, and most common year of birth(Only New York City and Chicago)
        earliest_year = int(df['Birth Year'].min())
        print('\nEarliest Year of Birth:', earliest_year)
    
        most_recent_year = int(df['Birth Year'].max())
        print('Most Recent Year of Birth:', most_recent_year)
    
        most_common_year = int((df['Birth Year'].mode())[0])
        print('Most Common Year of Birth:', most_common_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def print_sample(city): 
    """Print 5 Random Rows of RAW-DATA"""
    
    df = pd.read_csv(CITY_DATA.get(city))
    # Prompt user to allow the program to print 5 random rows of raw-data!
    while ((input('IF YOU WOULD YOU like to SEE A RANDOM SAMPLE OF RAW-DATA, Enter "Yes": ').lower().replace(' ','')) == 'yes'):
        print(df.sample(n=5))


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        print_sample(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower().replace(' ', '') != 'yes':
            break


if __name__ == "__main__":
	main()
