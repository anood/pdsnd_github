import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    city = ""
    month = ""
    day = ""
    filter = ""


    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print('\n \n Would you like to see data for \n Chicago \n New York \n Washington? \n \n')
    while True:
        city = input(" Enter the city that you want to see the data:  ")
        if city.lower() not in ('chicago', 'new york', 'washington'):
            print("Not an appropriate choice.")
        else:
            city = city.lower()
            break

    # get user input for month (all, january, february, ... , june)

    while True:
        month = input("\n Which month would you like to filter by? \n (January, February, March, April, May, or June) or all? ")
        if month.lower() not in ('january', 'february', 'march', 'april','may', 'june', 'all'):
            print("Not an appropriate choice.")
        else:
            month = month.lower()
            break

    while True:
        day = input("Which day would you like to filter by? \n (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday) or all? ")
        if day.lower() not in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'):
            print("Not an appropriate choice.")
        else:
            day = day.lower()
            break




    return city, month, day



def load_data(city, month, day):

    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])


    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
# find the most popular hour
    df['hour'] = df['Start Time'].dt.hour

    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('Most Common Month: {}'.format(df['month'].mode()[0]))


    # display the most common day of week
    print('Most Common day of week: {}'.format(df['day_of_week'].mode()[0]))


    # display the most common start hour
    print('Most Common start hour: {}'.format(df['hour'].mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station = df['Start Station'].value_counts().idxmax()
    print('Most Commonly used start station:', start_station)
    # display most commonly used end station
    end_station = df['End Station'].value_counts().idxmax()
    print('Most Commonly used end station:', end_station)

    # display most frequent combination of start station and end station trip
    combination_stations = df.groupby(['Start Station', 'End Station']).count()
    print('Most frequent combination of start station and end station trip:', start_station, 'and', end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = sum(df['Trip Duration'])
    print('Total travel time:', total_travel_time/86400, " Days")

    # display mean travel time
    mean_travel_time = (df['Trip Duration'].mean())
    print('Mean travel time:', mean_travel_time/60, " Minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of user types:\n', user_types)


    # Display counts of gender
    if 'Gender' in df.columns:

        genders = df['Gender'].value_counts()
        print('\nCounts of gender:\n', genders)

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:

        print('\nearliest year of birth: {}'.format(int(df['Birth Year'].min())))
        print('Most recent year of birth: {}'.format(int(df['Birth Year'].max())))
        print('Most Common year of birth: {}'.format(int(df['Birth Year'].mode())))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def show_data(df):
    show_rows = 5
    start_rows = 0
    end_rows = show_rows - 1
    while True:
        row_data = input("Would you like to see some more data? (y or n): ")
        if row_data.lower() == 'y':
            print(df.iloc[start_rows : end_rows + 1])
            start_rows += show_rows
            end_rows += show_rows
            print('.'*40)
            continue
        else:
            break

def main():
   while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_data(df)

        restart = input('\n Would you like to restart? Enter yes or no. \n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
