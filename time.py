import parsedatetime as pdt
from datetime import datetime

def find_latest_date(date_list):
    cal = pdt.Calendar()
    latest_date = None

    for date_str in date_list:
        try:
            parsed_date, status = cal.parse(date_str)
            
            # Check if parsing was successful
            if status != 0:
                # Convert parse result to datetime if it's not already one
                if isinstance(parsed_date, tuple):
                    parsed_date = datetime(*parsed_date[:6])
                
                # Initialize latest_date or update if the new date is later
                if latest_date is None or parsed_date > latest_date:
                    latest_date = parsed_date
        except Exception as e:
            print(f"Error parsing '{date_str}': {str(e)}")

    # Return the latest date as a string formatted as YYYY-MM-DD
    if latest_date:
        return latest_date.strftime('%Y-%m-%d')
    else:
        return "No valid dates found or could not parse any dates."

# Example usage
date_list = ["10th January 2022", "15th February 2022", "12th December 2021", "invalid date", "30th February 2019"]
print(find_latest_date(date_list))

# Splitting by whitespace
parts = text.split()

# Further splitting each part by comma
split_by_comma = []
for part in parts:
    split_by_comma.extend(part.split(','))

# Removing any empty strings that might result from splitting
final_parts = [part for part in split_by_comma if part]


def safe_index(my_list, element):
    """Returns the index of 'element' in 'my_list' or -1 if it is not found."""
    try:
        return my_list.index(element)
    except ValueError:
        return -1

# Example usage
my_list = ['apple', 'banana', 'cherry']

# Get the index of an element
index_banana = safe_index(my_list, 'banana')
print('Index of "banana":', index_banana)

# Get the index of an element that is not in the list
index_orange = safe_index(my_list, 'orange')
print('Index of "orange":', index_orange)

import re

def find_substring_occurrences(main_string, substrings):
    occurrences = []
    for substring in substrings:
        # Find all start positions of the substring in the main string
        starts = [m.start() for m in re.finditer('(?={})'.format(re.escape(substring)), main_string)]
        # Append each found position along with the substring to the result list
        occurrences.extend((substring, start) for start in starts)
    return occurrences

# Example usage:
main_string = "the quick brown fox jumps over the lazy dog"
substrings = ["the", "o"]
result = find_substring_occurrences(main_string, substrings)
print(result)





