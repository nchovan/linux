# sets varibale to empty string
command = ""

# sets begging booleans
started = False
stopped = True
true = True

while true:
    command = input(">").lower()
    if command == "start":
        if started:
            print("the car is already started")
        else:
            started = True  # changes started to True now that the car is started so you cant start it again
            print("The car has started....")
    elif command == "stop":
        if stopped:
            print("the car is already stopped")
        else:
            stopped = True  # changes stop to True so you cant stop the car again cause its already stopped
            print("The car has stopped....")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit
        """)
    elif command == "quit":
        print("your have quit")
        break   # break / end the while loop