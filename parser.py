import ctparser
import dateparser

def parse_date(input_date):
    # Parse date using ctparse
    ctparse_result = ctparse(input_date)
    
    # Check if ctparse gave both a start and an end date
    if ctparse_result and hasattr(ctparse_result, 'span'):
        start_date, end_date = ctparse_result.span
        return [start_date, end_date]

    # Parse date using dateparser if ctparse did not give a clear interval
    dateparser_result = dateparse(input_date)
    
    if dateparser_result:
        return [dateparser_result]
    
    # Return result of ctparse if dateparser also fails
    if ctparse_result and hasattr(ctparse_result, 'resolution'):
        return [ctparse_result.resolution]

    # If both parsers return None, return None
    return None

# Example usage
input_date = "from 10th January 2022 to 15th January 2022"
print(parse_date(input_date))


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


