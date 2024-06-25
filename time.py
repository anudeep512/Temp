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
