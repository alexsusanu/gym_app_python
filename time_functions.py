#https://docs.python.org/3/library/datetime.html?highlight=strftime#strftime-and-strptime-behavior
import datetime

date_dmy = datetime.datetime.now().strftime("%a %d-%B-%Y")
time_hm = datetime.datetime.now().strftime("%I:%m%p")

'''
datetime functions

strftime() -> converts time in string
format codes:
%a -> Sat
%A -> Saturday
%b -> Jan
%B -> January
%p -> am/pm
'''
