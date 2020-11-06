# imports the date class from datetime module
from datetime import date
# sets variable current_date to today's date
current_date = date.today()

# sets variable name to the user's input
name = input('please enter the name: ')
dob = input('please enter the date of birth (mm-dd-yyyy): ')
address = input('please enter the address: ')
email = input('please enter the email address: ')

# sets the variable age to the current yer minus the birth year from the variable dob, this is done by using the index
# position [6:10] (which is the 7th position through the 10th) while using int to set that to an integer for subtraction
age = current_date.year - int(dob[6:10])

# uses a formatted string (f) to print results in an easier to read code file,
# this uses place holders {} for the variable
contact_listing = (f'\nName: {name}'
                  f'\nDate of birth: {dob}'
                  f'\nAge: {str(age)}'
                  f'\nAddress: {address}'
                  f'\nEmail: {email}')

print(contact_listing)