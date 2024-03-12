months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november',
'december']
print(months)
abbreviation = []
for x in months:
    abbreviation.append(x[0:3]) #appends the first three letters of each month to the list "abbreviation"
print(abbreviation)

for x in abbreviation:
    print(x.upper(), end="|") #prints each element in the list abbreviation in one line and with the seperator "|"