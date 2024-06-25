import ctparser
import dateparser

def parse_date(input_date):
    ctparser_result = ctparser.parse(input_date)
    start_date = ctparser_result.get('start_date')
    end_date = ctparser_result.get('end_date')
    
    if start_date and end_date:
        # ctparser returned a range of dates
        return [start_date, end_date]
    elif start_date:
        # ctparser returned a single date occurrence
        dateparser_result = dateparser.parse(input_date)
        if dateparser_result:
            return [dateparser_result]
        return [start_date]
    else:
        # ctparser returned None
        dateparser_result = dateparser.parse(input_date)
        if dateparser_result:
            return [dateparser_result]
    
    return None  # Both ctparser and dateparser returned None

# Example usage
result = parse_date("10th January 2023")
print(result)

def remove_substrings(strings):
    # Step 1: Sort the list based on the length of the strings
    strings_sorted = sorted(strings, key=len)
    
    # Step 2: Remove elements that are substrings of other elements
    result = []
    for i in range(len(strings_sorted)):
        is_substring = False
        for j in range(i + 1, len(strings_sorted)):
            if strings_sorted[i] in strings_sorted[j]:
                is_substring = True
                break
        if not is_substring:
            result.append(strings_sorted[i])
    
    return result

# Example usage
strings = ["apple", "app", "pineapple", "pie", "applepie"]
result = remove_substrings(strings)
print(result)


