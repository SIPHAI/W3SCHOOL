from enum import Enum
class Country(Enum):
    Cambodia = 854
    China = 882
    Vietnam = 883
    Thai = 885
    Australia = 658
print('\nCountry name: {}'.format(Country.Cambodia.name))
print('\nCode value: {}'.format(Country.Cambodia.value))