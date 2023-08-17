a = 36 *2
b = 35
from datetime import datetime

def add(a,b):
    return a+b

print(add(a,b))

def calculate_time_in_seconds_between_two_dates(start_date, end_date):
    #input date format is yy-mm-dd
    start_date = datetime.strptime(start_date, '%y-%m-%d')
    end_date = datetime.strptime(end_date, '%y-%m-%d')
    return (end_date - start_date).total_seconds()

print(calculate_time_in_seconds_between_two_dates('20-01-01', '20-01-02'))
