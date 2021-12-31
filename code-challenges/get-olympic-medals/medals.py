from collections import namedtuple

medal = namedtuple('medal', ['City', 'Edition', 'Sport', 'Discipline', 'Athlete', 'NOC', 'Gender',
       'Event', 'Event_gender', 'Medal'])
medals = [] #Complete this - medals is a list of medal namedtuples

def main():
    result = get_medals(Athlete='LEWIS, Carl', Event='100m')
    print(result)

def get_data():
    with open('olympics.txt', 'rt', encoding='utf-8') as file:    
        olympics = file.read()
    return olympics

def get_medals(**kwargs):
    '''Return a list of medal namedtuples '''
    olympics = get_data()
    medals = [medal(*row.split(';')) for row in olympics.splitlines()[1:]] #skip header (row index = 0)
    result = [medal for medal in medals if all(getattr(medal, key) == value for key,value in kwargs.items())]
    return result

if __name__ == "__main__":
    main()