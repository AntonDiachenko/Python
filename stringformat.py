
#person = {'name': 'Jenn', 'age': 23}
myList = ["Peppa", 23]

 # Option 1 - not effective
# sentence = 'My name is ' + person['name'] + ' and I am ' + str(person['age']) + ' years old.'
# print(sentence)

 # Option 2 
# sentence = 'My name is {} and I am {} years old.'.format(person['name'], person['age'])
# print(sentence)

 # Option 3
# sentence = 'My name is {0} and I am {1} years old.'.format(person['name'], person['age'])
# print(sentence)

 # Option 4
#sentence = 'My name is {0[name]} and I am {1[age]} years old.'.format(person, person)
#print(sentence)

 # Option 5- most effective - person is passed only once
#sentence = 'My name is {0[name]} and I am {0[age]} years old.'.format(person)
#print(sentence)

# List example
#sentence = 'My name is {0[0]} and I am {0[1]} years old.'.format(myList)
#print(sentence)



# tag = 'h1'
# text = 'This is a headline'
# sentence = '<{0}>{1}</{0}>'.format(tag, text)
# print(sentence)


# Using class example
class Person():

    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('Jack', '33')

sentence = 'My name is {0.name} and I am {0.age} years old.'.format(p1)
print(sentence)

# sentence = 'My name is {name} and I am {age} years old.'.format(name='Jenn', age='30')
# print(sentence)

    # Unpacking person dictionary - most convenient way
# sentence = 'My name is {name} and I am {age} years old.'.format(**person)
# print(sentence)

    # Format output to certain type (in this case 3 digits with zero pads)
# for i in range(1, 11):
#     sentence = 'The value is {:03}'.format(i)
#     print(sentence)

 # Decimal places format
# pi = 3.14159265
# sentence = 'Pi is equal to {:.2f}'.format(pi)
# print(sentence)

    # Format large numbers with comma separator 
# sentence = '1 MB is equal to {:,.2f} bytes'.format(1000**2)
# print(sentence)


    # Datetime formatting for print-out
"""
import datetime
my_date = datetime.datetime(2016, 9, 24, 12, 30, 45)
# print(my_date)

# March 01, 2016
sentence = '{:%B %d, %Y}'.format(my_date)
print(sentence)

# March 01, 2016 fell on a Tuesday and was the 061 day of the year.
sentence = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(my_date)
print(sentence)

"""