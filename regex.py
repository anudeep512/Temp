# (M/m)on[th] DD[th] [,] [YYYY]
# r'\b(?:[Jj]anuary|[Ff]ebruary|[Mm]arch|[Aa]pril|[Mm]ay|[Jj]une|[Jj]uly|[Aa]ugust|[Ss]eptember|[Oo]ctober|[Nn]ovember|[Dd]ecember)\s*\d{1,2}(?:st|nd|rd|th)?\s*(?:,?\s*\d{4})?\b',

# DD[th] (M/m)on[th] [,] [YYYY]
# r'\b\d{1,2}(?:st|nd|rd|th)?\s*(?:[Jj]anuary|[Ff]ebruary|[Mm]arch|[Aa]pril|[Mm]ay|[Jj]une|[Jj]uly|[Aa]ugust|[Ss]eptember|[Oo]ctober|[Nn]ovember|[Dd]ecember)\s*\d{1,2}(?:st|nd|rd|th)?\s*(?:,?\s*\d{4})?\b',

# YYYY (M/m)on[th] DD[th]
# r'\b(?:\d{4})?\s*(?:[Jj]anuary|[Ff]ebruary|[Mm]arch|[Aa]pril|[Mm]ay|[Jj]une|[Jj]uly|[Aa]ugust|[Ss]eptember|[Oo]ctober|[Nn]ovember|[Dd]ecember)\s*\d{1,2}(?:st|nd|rd|th)?\b',

# MM-DD-YYYY
# r'\b(?:0[1-9]|1[0-2])-(?:0[1-9]|[12][0-9]|3[01])-(?:19|20)\d{2}\b'

import re

def normalize_text(text):
    return re.sub(r'\s+', ' ', text)

# List of regex patterns
regex_patterns = [
    r'\b(?:[Jj]anuary|[Ff]ebruary|[Mm]arch|[Aa]pril|[Mm]ay|[Jj]une|[Jj]uly|[Aa]ugust|[Ss]eptember|[Oo]ctober|[Nn]ovember|[Dd]ecember)\s*\d{1,2}(?:st|nd|rd|th)?\s*(?:,?\s*\d{4})?\b',
    r'\b\d{1,2}(?:st|nd|rd|th)?\s*(?:[Jj]anuary|[Ff]ebruary|[Mm]arch|[Aa]pril|[Mm]ay|[Jj]une|[Jj]uly|[Aa]ugust|[Ss]eptember|[Oo]ctober|[Nn]ovember|[Dd]ecember)\s*(?:,?\s*\d{4})?\b',
    r'\b(?:\d{4})?\s*(?:[Jj]anuary|[Ff]ebruary|[Mm]arch|[Aa]pril|[Mm]ay|[Jj]une|[Jj]uly|[Aa]ugust|[Ss]eptember|[Oo]ctober|[Nn]ovember|[Dd]ecember)\s*\d{1,2}(?:st|nd|rd|th)?\b',
    r'\b(?:0[1-9]|1[0-2])-(?:0[1-9]|[12][0-9]|3[01])-(?:19|20)\d{2}\b'
]

text = "notional traded from 02-09-2013 until 26th    may   2016 and 2017   January 30th , june 28th, 2018"
text = normalize_text(text)
all_matches = []
txt_lst = [
    'what is the notional traded from 02-09-2013 until 30th june 2019'
]
for text in txt_lst:
    for pattern in regex_patterns:
        matches = re.findall(pattern, text)
        
        for match in matches:
            match_str = ''.join(match)
            all_matches.append(match_str)
            
            text = text.replace(match_str, '')

    print("Modified text:", text)

    print("All matches:", all_matches)


    

