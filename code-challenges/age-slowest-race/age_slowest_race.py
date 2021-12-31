# Source of data: https://www.arrs.run/
# This dataset has race times for women 10k runners from the Association of Road Racing Statisticians
# Assume a year has 365.25 days

from datetime import datetime, time, timedelta
import re

def main():
    result = get_age_slowest_times()
    print(result)

def get_data():
    with open('10k_racetimes.txt', 'rt') as file:
        content = file.read()
    return content

def get_event_time(line):
    """Given a line with Jennifer Rhines' race times from 10k_racetimes.txt, 
       parse it and return a tuple of (age at event, race time).
       Assume a year has 365.25 days"""

    #print(f"**{line}**")
    race_time = str(re.findall(r'\d{2}:\d{2}[.\d+\s]*', line)[0]).strip()
    dates = re.findall(r'\d{2}\s{1}\D{3}\s{1}\d{4}', line)
    race_date_ = dates[0].split(' ')
    birth_date_ = dates[1].split(' ')
    race_date = datetime(day=int(race_date_[0]), month=datetime.strptime(race_date_[1], "%b").month, year=int(race_date_[2]))
    birth_date = datetime(day=int(birth_date_[0]), month=datetime.strptime(birth_date_[1], "%b").month, year=int(birth_date_[2]))
    #print(race_date,birth_date)
    age_at_event_days = (race_date-birth_date).days  
    return (age_at_event_days, race_time)
    
def get_age_slowest_times():
    '''Return a tuple (age, race_time) where:
       age: AyBd is in this format where A and B are integers'''
    races = get_data()
    list_races = races.splitlines()
    # index 0=TIME, 1=Athlete, 2 =Race date, 3=Date of birth, 4 = Location
    rhines_times = [get_event_time(row) for row in list_races[1:] if row.count('Jennifer Rhines') > 0] #skip header (row index = 0)            
    #print(rhines_times)
    race_times = []
    for element in rhines_times:
        te = element[1].split(':') #time elements
        race_time = timedelta()
        if element[1].count(".") > 0: #time contains miliseconds
            race_time = timedelta(minutes=int(te[0]), seconds=int(te[1].split('.')[0]), milliseconds=int(te[1].split('.')[1]))
        else:
            race_time = timedelta(minutes=int(te[0]),seconds=int(te[1]))
        race_times.append(race_time.total_seconds() * 1000)
    #print(race_times)   
    slowest_time_idx = race_times.index(max(race_times))
    #print(rhines_times[slowest_time_idx])        
    age_years = int(rhines_times[slowest_time_idx][0] // 365.25)
    age_days = int(rhines_times[slowest_time_idx][0] - (age_years * 365.25))
    formatted_age = f'{age_years}y{age_days}d'
    return (formatted_age, rhines_times[slowest_time_idx][1])

if __name__ == "__main__":
    main()
