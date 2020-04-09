import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

CITIES = ['chicago', 'new york city', 'washington']
MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']
DAYS = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday' ]

# Filter data
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington)
    while True:
            city = input("In which city are you interested? Please enter Chicago, New York City or Washington: ").lower()
            if city in CITIES:
                break
            else: print('That is not a valid input. Please insert exactly Chicago, New York City or Washington')

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("Are you interested in a particular month? Please insert all or the respective month: ").lower()
        if month in MONTHS or month == 'all':
            break
        else: print('That is not a valid input. Please enter a month starting in January until June.')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Are you interested in a particular day of the week? Please insert all or the respective day of the week: ").lower()
        if day in DAYS or day == 'all':
            break
        else: print('That is not a valid input. Please insert a weekday from Monday till Sunday.')

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
        (str) hour - hour of the day to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # create data frame based on the csv
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
#         months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = MONTHS.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Please note: Searched for a solution to get the max value during the practice problem 1  - found some info on argmax and changed it           idxmac since it did not longer work with argmax

    # display the most common month
    popular_month = df['month'].value_counts().idxmax()
    print('The most common month is: \n', popular_month)

    # display the most common day of week
    popular_day = df['day'].value_counts().idxmax()
    print('The most common day of the week is (if filtered one day, the respective day is shown): \n', popular_day)

    # display the most common start hour
    popular_hour = df['hour'].value_counts().idxmax()
    print('The most common start hour is: \n', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_startstation = df['Start Station'].value_counts().idxmax()
    print('The most commonly used start station is: \n', popular_startstation)

    # display most commonly used end station
    popular_endstation = df['End Station'].value_counts().idxmax()
    print('The most commonly used used end station is: \n', popular_endstation)

    # display most frequent combination of start station and end station trip
    popular_combistation = (df['Start Station'] + ' to ' + df['End Station']).value_counts().idxmax()
    print('The most commonly trip is: \n', popular_combistation)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is: \n', total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean travel time is: \n', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('The ounts of user types: \n', user_types)

    while True:
        try:
            # Display counts of genderexit

             gender = df['Gender'].value_counts()
             print('The counts of gender: \n', gender)

            # Trip duration per gender
             trip_per_gender = df.groupby(['Gender'])['Trip Duration'].mean()
             print('The trip duration on average for male and female: \n', trip_per_gender)


             # Display earliest, most recent, and most common year of birth
             earliest = df['Birth Year'].min()
             most_recent = df['Birth Year'].max()
             most_common = df['Birth Year'].value_counts().idxmax()
             print('The earliest birth year is {}, the most recent {} and the most common {}.\n'.format(earliest,most_recent, most_common))

             # Trip duration per year
             trip_per_year = df.groupby(['Birth Year'])['Trip Duration'].mean()
             print('Per year with have the following trip duration average: \n',trip_per_year)
             break

        except:
            print('For Washington is no data regarding gender and year of birth available \n')
            break

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def nan(df):
    print('Check for NaN values in data frame. \n')

    nan_vaules = df.isnull().sum()
    print('The number of NaN values is : \n', nan_vaules)

def show_head(df):
    """Displays first 5 lines of raw data."""

    show = input('Would you like to see the first 5 lines of raw input? Yes or no? \n')
    if show.lower() == 'yes':
        print('The first 5 lines of raw data are: \n', df.head())

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        show_head(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        nan(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
