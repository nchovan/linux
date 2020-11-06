from datetime import date
current_date = date.today()
dob = input('please enter your date of birth (mm-dd-yyyy): ')
age = (current_date.year - int(dob[6:10]))
print("Age: " + age)
