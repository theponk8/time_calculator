#needs to print the cost out in full as in $49.50
#needs to log the information in a file
#needs to save variable for after restart
#could add in a input for customer name
#fix bug where program crashes if you type anything before pausing


import time
import webbrowser

#variable for time in seconds
y = 0

def count_time():
    global y
    #allows the loop to run until exception, keyboardinterrupt, ctrl + c, is pressed
    try:
        #loop that counts time in seconds and stores it in 'y' variable
        while True:
            time.sleep(1)
            y = y + 1
            print y
    except KeyboardInterrupt:
        #what happens after 'ctrl + c' is pressed
        print ("Paused at:" +time.ctime())
        x = input ("What would you like to do?\n1:start 2:finish")
        if x == 1:
            print ("Restarted at:" +time.ctime())
            count_time()
        elif x == 2:
            print""
        else:
            webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
            count_time()
            
        

print "############################################"
print "############### TIME_COUNTER ###############"
print "############################################\n\n"
print "Press \"Ctrl + C\" to stop pause the counter\n Any key to start."
raw_input ("")

print ("\nStarted at:" +time.ctime())
count_time()

#finds how many half hours have passed
z = y /60 /30
#always charge $49.50
if z < 1:
    z = z + 1
#calculates the price
cost = z * 49.50


print "\n\n\n\nThe cost for this repair comes to to $ %s." %(cost)
