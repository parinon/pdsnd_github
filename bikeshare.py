#import libraries
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
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Would you like to see data for Chicago, New York City or Washington?').lower()
    while city not in ['chicago', 'new york city','washington']:
        print('Your input is not in database.')
        city = input('Would you like to see data for Chicago, New York City or Washington?').lower()
        if city in ['chicago', 'new york city','washington']:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Which month you would like see the data (January - June or All)?').lower()
    while month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
        print('Your input is not in database.')
        month = input('Which month you would like see the data (January - June or All)?').lower()
        if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Which day you would like see the data (Monday - Sunday or All)?').lower()
    while day not in ['monday','tuesday','wednesday','thursday','friday','saturday','sunday', 'all']:
        print('Your input is not in database.')
        day = input('Which day you would like see the data (Monday - Sunday or All)?').lower()
        if day in ['monday','tuesday','wednesday','thursday','friday','saturday','sunday', 'all']:
            break
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    popular_month = df['month'].mode()[0]
    print('The most common month is: {}'.format(months[popular_month-1]))

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('The most common day of week is: {}'.format(popular_day))
    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('The most common start hour is: {}'.format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is: {}'.format(most_start_station))

    # TO DO: display most commonly used end station
    most_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station is: {}'.format(most_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['Start Station to End Station'] = df['Start Station']+' to '+df['End Station']
    most_com = df['Start Station to End Station'].mode()[0]
    print('The most frequent combination of start station and end station trip are: {}'.format(most_com))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time is: {}'.format(total_travel_time))
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time is: {}'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Count of User Types\n', user_types)

    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print('Count of Gender\n', gender)
    except KeyError:
        print('Count of gender is only available for NYC and Chicago')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest = df['Birth Year'].min()
        print('Earliest year of birth is: ', earliest)
        most_recent = df['Birth Year'].max()
        print('Most recent year of birth is: ', most_recent)
        most_common = df['Birth Year'].mode()[0]
        print('Most common year of birth is: ', most_common)
    except KeyError:
        print('Earliest, most recent, and most common year of birth are only available for NYC and Chicago')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#Create Raw Data Function
def raw_data(df):
    while True:
        data = input('\nWould you like to see the 5 raw datas? Enter Yes or No.\n').lower()
        if data not in ['yes','no']:
            print('\nNot Define')
            continue
        elif data == 'yes':
            print(df.sample(n = 5))
            continue
        elif data == 'no':
            break
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter Yes or No.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
