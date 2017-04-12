
import time
import webbrowser

#writes to 'log.txt' when 'f' is called. i think 'w' is write
f =open('log.txt', 'w')

#variable for time in seconds
y = 0

def count_time():
    global y
    global f
    #allows the loop to run until exception, keyboardinterrupt, ctrl + c, is pressed
    try:
        #loop that counts time in seconds and stores it in 'y' variable
        while True:
            time.sleep(1)
            y = y + 1
            print y
    except KeyboardInterrupt:
        #what happens after 'ctrl + c' is pressed
        print ("\nPaused at:" +time.ctime())
        f.write("\nPaused at:" +time.ctime())
        x = input ("What would you like to do?\n1:start 2:finish")
        if x == 1:
            print ("\nRestarted at:" +time.ctime())
            f.write("\nRestarted at:" +time.ctime())
            count_time()
        elif x == 2:
            print "Job finished at:" +time.ctime()
            f.write("\nJob finished at:" +time.ctime())
        else:
            webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
            count_time()


print "############################################"
print "############### TIME_COUNTER ###############"
print "############################################\n\n"
name = raw_input ("Please enter a the customer's name.")

print name
f.write("Customer Name: " +name)
    

print "Press \"Ctrl + C\" to PAUSE the counter\nPress any key to START."
raw_input ("")

print ("\nStarted at:" +time.ctime())
f.write("\n\nStarted at:" +time.ctime())


count_time()

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

