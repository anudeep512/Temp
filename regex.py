# Define the string and the substring
main_string = "This is a sample string."
substring = "sample "

# Remove the substring
result_string = main_string.replace(substring, "")

# Print the result
print(result_string)

# (M/m)on[th] DD[th] [,] [YYYY]
# \b([Jj]anuary|[Ff]ebruary|[Mm]arch|[Aa]pril|[Mm]ay|[Jj]une|[Jj]uly|[Aa]ugust|[Ss]eptember|[Oo]ctober|[Nn]ovember|[Dd]ecember)\s*\d{1,2}(st|nd|rd|th)?\s*(,?\s*\d{4})?\b

# DD[th] (M/m)on[th] [,] [YYYY]
# \b\d{1,2}(st|nd|rd|th)?\s+[Jj]anuary|[Ff]ebruary|[Mm]arch|[Aa]pril|[Mm]ay|[Jj]une|[Jj]uly|[Aa]ugust|[Ss]eptember|[Oo]ctober|[Nn]ovember|[Dd]ecember\s*\d{1,2}(st|nd|rd|th)?\s*(,?\s*\d{4})?\b

# YYYY (M/m)on[th] DD[th]
# \b(\d{4})?\s*([Jj]anuary|[Ff]ebruary|[Mm]arch|[Aa]pril|[Mm]ay|[Jj]une|[Jj]uly|[Aa]ugust|[Ss]eptember|[Oo]ctober|[Nn]ovember|[Dd]ecember)\s+\d{1,2}(st|nd|rd|th)?\b

import re

# List of regex patterns
regex_patterns = [
    r'\b(\d{4})?\s*([Jj]anuary|[Ff]ebruary|[Mm]arch|[Aa]pril|[Mm]ay|[Jj]une|[Jj]uly|[Aa]ugust|[Ss]eptember|[Oo]ctober|[Nn]ovember|[Dd]ecember)\s+\d{1,2}(st|nd|rd|th)?\b',
    # Add more patterns as needed
]

# Sample text
text = "I have an appointment on 2022 January 1st and another on February 2nd, 2023. Also, March 3rd and April 4th."

# List to store all matches
all_matches = []

# Loop through each regex pattern
for pattern in regex_patterns:
    # Find all matches for the current regex pattern
    matches = re.findall(pattern, text)
    
    # Store the matches in the all_matches list
    for match in matches:
        # Join the match tuple into a single string (if there are multiple groups)
        match_str = ''.join(match)
        all_matches.append(match_str)
        
        # Use .replace() to remove the found string from the text
        text = text.replace(match_str, '')

# Print the final modified text
print("Modified text:", text)

# Print all matches
print("All matches:", all_matches)

substring_list = [
    "a mini cooper",
    # Add more substrings as needed
]

def normalize_text(text):
    return re.sub(r'\s+', '', text)
  
for substring in substring_list:
    # Normalize the substring to remove spaces
    normalized_substring = normalize_text(substring)
    
    # Normalize the text for comparison
    normalized_text = normalize_text(text)
    
    # Find the position of the normalized substring in the normalized text
    pos = normalized_text.find(normalized_substring)
    
    while pos != -1:
        # Find the actual substring in the original text
        original_substring = text[pos:pos + len(normalized_substring)]
        
        # Use re.sub to replace the original substring in the text
        text = re.sub(re.escape(original_substring), '', text, count=1)
        
        # Normalize the updated text for the next comparison
        normalized_text = normalize_text(text)
        
        # Find the next occurrence
        pos = normalized_text.find(normalized_substring)

# Print the final modified text
print("Modified text:", text)

# Print all matches
print("All matches:", all_matches)