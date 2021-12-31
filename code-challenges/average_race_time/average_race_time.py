# Source of data: https://www.arrs.run/
# This dataset has race times for women 10k runners from the Association of Road Racing Statisticians

from datetime import timedelta

def main():
    result = get_average()
    print(result)

def get_data():
    """Return content from the 10k_racetimes.txt file"""
    with open('10k_racetimes.txt', 'rt') as file:
        content = file.read()
    return content

def get_rhines_times():
    """Return a list of Jennifer Rhines' race times"""
    races = get_data()
    list_races = races.splitlines()
    #print(list_races)
    # index 0=TIME, 1=Athlete, 2 =Race date, 3=Date of birth, 4 = Location
    rhines_times = [row.split()[0] for row in list_races[1:] if row.count('Jennifer Rhines') > 0] #skip header (row index = 0)
    return rhines_times

def get_average():
    """Return Jennifer Rhines' average race time in the format:
       mm:ss.M where :
       m corresponds to a minutes digit
       s corresponds to a seconds digit
       M corresponds to a milliseconds digit (no rounding, just the single digit)"""
    racetimes = get_rhines_times()
    #print(racetimes)
    sum_time = timedelta()
    for element in racetimes:
        te = element.split(':') #time elements
        #print(te) 
        if element.count(".") > 0: #time contains miliseconds
            sum_time += timedelta(minutes=int(te[0]), seconds=int(te[1].split('.')[0]), milliseconds=int(te[1].split('.')[1]))
        else:
            sum_time += timedelta(minutes=int(te[0]),seconds=int(te[1]))
        
    avg_time = str(sum_time / len(racetimes))
    #print(avg_time)
    result = avg_time[2:9] 
    #print(result)
    return result

if __name__ == "__main__":
    main()