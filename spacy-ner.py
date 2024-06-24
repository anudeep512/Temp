from ctparse import ctparse
from dateparser import parse
from datetime import datetime

def parse_dates(input_text):
    # Using ctparse
    ct_result = ctparse(input_text)
    ct_date = None
    if ct_result:
        # Check if the result is a range
        if hasattr(ct_result.resolution, 'start') and hasattr(ct_result.resolution, 'end'):
            # Return immediately if a range is found
            return {'ctparse': (ct_result.resolution.start, ct_result.resolution.end)}
        elif hasattr(ct_result.resolution, 'value'):
            ct_date = ct_result.resolution.value

    # Using dateparser
    dp_date = parse(input_text)

    # Determine which result to use
    results = {}
    if ct_date and isinstance(ct_date, datetime):
        results['ctparse'] = ct_date
    if dp_date and isinstance(dp_date, datetime):
        results['dateparser'] = dp_date

    # Choose based on presence of valid outputs
    if 'ctparse' in results and 'dateparser' in results:
        return results  # Both are valid
    elif 'ctparse' in results:
        return {'ctparse': results['ctparse']}
    elif 'dateparser' in results:
        return {'dateparser': results['dateparser']}
    return {}  # None are valid

# Example usage
input_text = "Meet me from June 25th to June 30th, or maybe on July 3rd."
parsed_dates = parse_dates(input_text)
print("Parsed Dates:", parsed_dates)

import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_trf")

def extract_date_entities(text):
    # Process the text
    doc = nlp(text)
    # Extract entities identified as dates
    dates = [ent.text for ent in doc.ents if ent.label_ == "DATE"]
    return dates

# Example usage
input_text = "I have an appointment on June 25th, and another important meeting on July 3rd."
dates = extract_date_entities(input_text)
print("Extracted Date Entities:", dates)
