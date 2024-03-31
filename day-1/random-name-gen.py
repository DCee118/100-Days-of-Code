print('Welcome to the random name generator!')

month_names = {
    'january': 'Moon',
    'february': 'Storm',
    'march': 'Fire',
    'april': 'Master',
    'may': 'Lord',
    'june': 'King',
    'july': 'Queen',
    'august': 'Sun',
    'september': 'Knight',
    'october': 'Hero',
    'november': 'Saint',
    'december': 'Dark'
}

month = input('What month were you born in?\n').lower()
name = input('What is your nickname?\n')
print(month_names[month] + ' ' + name)