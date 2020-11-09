from datetime import date
current_date = date.today()


name = input('please enter the name: ')
dob = input('please enter the date of birth (mm-dd-yyyy): ')
address = input('please enter the address: ')
email = input('please enter the email address: ')

# sets the variable age to the current yer minus the birth year from the variable dob, this is done by using the index
# position [6:10] (which is the 7th position through the 10th) while using int to set that to an integer for subtraction
age = current_date.year - int(dob[6:10])

contact_listing = (f'\nName: {name}'
                   f'\nDate of birth: {dob}'
                   f'\nAge: {str(age)}'
                   f'\nAddress: {address}'
                   f'\nEmail: {email}')


print(contact_listing)


