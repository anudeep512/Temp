
## For calculating current week

import datetime

# Get today's date
today = datetime.date.today()

# Calculate the most recent Monday (0=Monday, 1=Tuesday, ..., 6=Sunday)
current_weekday = today.weekday()
monday_of_this_week = today - datetime.timedelta(days=current_weekday)

# Generate dates from Monday to today
week_dates = [monday_of_this_week + datetime.timedelta(days=i) for i in range(current_weekday + 1)]

# Format dates in MM-DD-YYYY
formatted_dates = [date.strftime('%m-%d-%Y') for date in week_dates]

print(formatted_dates)

## For previous week

import datetime

# Get today's date
today = datetime.date.today()

# Calculate the most recent Monday (0=Monday, 1=Tuesday, ..., 6=Sunday)
current_weekday = today.weekday()
monday_of_this_week = today - datetime.timedelta(days=current_weekday)

# Calculate the Monday of the previous week
monday_of_last_week = monday_of_this_week - datetime.timedelta(days=7)
# Calculate the Sunday of the previous week
sunday_of_last_week = monday_of_last_week + datetime.timedelta(days=6)

# Generate dates from Monday to Sunday of the previous week
week_dates = [monday_of_last_week + datetime.timedelta(days=i) for i in range(7)]

# Format dates in MM-DD-YYYY
formatted_dates = [date.strftime('%m-%d-%Y') for date in week_dates]

print(formatted_dates)


## For current month 
import datetime

# Get today's date
today = datetime.date.today()

# Calculate the first day of the current month
first_day_of_month = today.replace(day=1)

# Generate dates from the first day of the month to today
month_dates = [first_day_of_month + datetime.timedelta(days=i) for i in range((today - first_day_of_month).days + 1)]

# Format dates in MM-DD-YYYY
formatted_dates = [date.strftime('%m-%d-%Y') for date in month_dates]

print(formatted_dates)


## previous month
import datetime

# Get today's date
today = datetime.date.today()

# Calculate the first day of the previous month
first_day_of_last_month = (today.replace(day=1) - datetime.timedelta(days=1)).replace(day=1)

# Calculate the last day of the previous month
last_day_of_last_month = today.replace(day=1) - datetime.timedelta(days=1)

# Generate dates from the first day of the previous month to the last day of the previous month
previous_month_dates = [first_day_of_last_month + datetime.timedelta(days=i) for i in range((last_day_of_last_month - first_day_of_last_month).days + 1)]

# Format dates in MM-DD-YYYY
formatted_dates = [date.strftime('%m-%d-%Y') for date in previous_month_dates]

print(formatted_dates)

--------------------------------------------------------------------

from datetime import datetime, timedelta

def generate_date_strings(start_date_str, end_date_str):
    # Convert the start and end date strings to datetime objects
    start_date = datetime.strptime(start_date_str, "%d/%m/%Y")
    end_date = datetime.strptime(end_date_str, "%d/%m/%Y")
    
    # Initialize an empty list to store the date strings
    date_strings = []
    
    # Generate the date strings between start_date and end_date
    current_date = start_date
    while current_date <= end_date:
        # Convert the current date to the desired format and append to the list
        date_strings.append(current_date.strftime("%y%m%d"))
        # Increment the current date by one day
        current_date += timedelta(days=1)
    
    return date_strings

# Example usage
start_date_str = "01/07/2024"
end_date_str = "05/07/2024"
date_strings = generate_date_strings(start_date_str, end_date_str)
print(date_strings)  # Output: ['240701', '240702', '240703', '240704', '240705']


--------------------------------------------------------------------