

import time
import webbrowser
import os

#writes to 'log.txt' when 'f' is called. i think 'w' is write
f =open('log.txt', 'w')
#grab the starting time for the session, this may have to be shifted
starttime = time.ctime()
#variable for time in seconds
y = 0

#example of a labour saving functon
def clear():
	#clear away the previous menu
	os.system('cls' if os.name == 'nt' else 'clear')
	
def count_time():
    global y
    global f
    #allows the loop to run until exception, keyboardinterrupt, ctrl + c, is pressed
    try:
        #loop that counts time in seconds and stores it in 'y' variable
        while True:
			#Virtually the same function as before, except we are drawing the required info, then clearing it and drawing the new required info - et infinum
			y = y + 1
			print "Press \"Ctrl + C\" to PAUSE the counter"
			print "Session start time: "
			print starttime
			print "Customer name: "
			print name
			print "Seconds elapsed: "
			print y
			
			time.sleep(1)
			clear()
    except KeyboardInterrupt:
	clear()
		#what happens after 'ctrl + c' is pressed
        print ("\nPaused at:" +time.ctime())
        f.write("\nPaused at:" +time.ctime())
        x = input ("What would you like to do?\n1:resume 2:finish 3:change time \n")
        if x == 1:
            print ("\nRestarted at:" +time.ctime())
            f.write("\nRestarted at:" +time.ctime())
            count_time()
        elif x == 2:
			clear()	
			print "Job finished at:" +time.ctime()
			f.write("\nJob finished at:" +time.ctime())
			

        else:
            webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
            

#this needs wrapping up into a series of functions, but I don't want this merge to be too edit heavy
#additionally, consider wrapping up all of the logging stuff in a seperate function as we don't want bits of code being lost
#EG, this could be a start function
print "############################################"
print "############### TIME_COUNTER ###############"
print "############################################\n\n"
name = raw_input ("Please enter a the customer's name:")

print name
f.write("Customer Name: " +name)
    

print "\nPress any key to START."
raw_input ("")
clear()
print ("\nStarted at:" +time.ctime())
f.write("\n\nStarted at:" +time.ctime())


count_time()
#EG, this could be a cost calculation function
#finds how many half hours have passed
z = y /60 /30
#always charge $49.50
if z < 1:
    z = z + 1
#calculates the price
cost = z * 49.50

'''The :, adds a comma as a thousands separator, and the .2f limits the string to
two decimal places (or adds enough zeroes to get to 2 decimal places, as the case
may be) at the end.'''
print "\n\n\n\nThe cost for this repair comes to " +'${:,.2f}'.format(cost)
f.write("\n\n\n\nThe cost for this repair comes to " +'${:,.2f}'.format(cost))

#need to close the logfile.txt
f.close()
