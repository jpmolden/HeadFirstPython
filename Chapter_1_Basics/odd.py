from datetime import datetime
    #from os       import getcwd
import time
    # importing modules as a specific name
import os as MYOS
    # Importing like this allows ranint() without random.randint
from random import randint


odds = [ 1,   3,  5,  7,  9,11,  13, 15, 17, 19,
         21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
         41, 43, 45, 47, 49, 51, 53, 55, 57, 59 ]


for i in range(6):
    right_this_minute = datetime.today().minute

    if right_this_minute in odds:
        print("This minute seems a little odd.")
        # print(getcwd())
        
    else:
        print("Not an odd minute.")
        # print(getcwd())

    wait_time = randint(1,3)
    print("Waiting " + str(wait_time) )
    time.sleep(wait_time)


    
print(MYOS.getcwd())
today = time.strftime("%A")

print(today)
