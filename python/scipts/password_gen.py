#!/usr/bin/python3
 
import string, random	#import needed libraries

uppercase = []	#create blank list called upercase
lowercase = []
numbers = []
symbols = []
for x in range(3): #runs command 3 times
	uppercase.append(random.choice(string.ascii_uppercase)) #appends (adds to end of specified list) a random uppercase letter
	lowercase.append(random.choice(string.ascii_lowercase))
	numbers.append(random.choice(string.digits))
	symbols.append(random.choice("!@#$%^&*"))

password=(uppercase + lowercase + numbers + symbols) #combines the lists

random.shuffle(password) #randomly shuffle the list contents around

print(''.join(password)) #joins the list to be a single string
