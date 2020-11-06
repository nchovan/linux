# imports the date class from datetime module
from datetime import date
# sets variable current_date to today's date
current_date = date.today()

# sets vaiable name to the user's input
name = input('please enter your name: ')
dob = input('please enter your date of birth (mm-dd-yyyy): ')
address = input('please enter your address: ')
email = input('please enter your email address: ')

# sets the varibale age to the current yer minus the birth year from the variable dob, this is done by using the index
# position [6:10] (which is the 7th position through the 10th) while using int to set that to an integer for subtraction
age = current_date.year - int(dob[6:10])

# uses \n to return a new line and then print the word "Name:" followed by the user input defined by the variable name
print('\nName: ' + name,
      '\nDate of birth: ' + dob,
      '\nAge: ' + str(age),   # sets age to print as a string, this prevents error: can only concatenate str (not "int") to str
      '\nAddress: ' + address,
      '\nEmail: ' + email)
