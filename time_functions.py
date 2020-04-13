#https://docs.python.org/5/library/datetime.html?highlight=strftime#strftime-and-strptime-behavior
#date format -> Day_of_week day-month_string-year (Mon 06-April-2020)
#time format -> H:m am/pm
#date / time -> not formatted with strftime
#date_dmy / time_hm -> formatted to string (dmy -> day month year / hm -> hour min)
"""
time functions
"""
import datetime

date = datetime.datetime.now()
date_30 = date + datetime.timedelta(days=30)
time = datetime.datetime.now()

#def date_format_dmy():
#    return date.strftime("%a %d-%B-%Y")

#def date_end_membership():
#    return date_30.strftime("%a %d-%B-%Y")

def time_imp():
    return time.strftime("%I:%M %p")
