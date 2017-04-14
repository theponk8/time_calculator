# import the library
from appJar import gui

import time
### http://appjar.info/pythonWidgets/
### http://appjar.info/pythonWidgetGrouping/
def initialise():
	print "initialising variables"
	global name, seconds, minutes, hours, timerstarted
	name = "NULL"
	seconds = 0
	minutes = 0
	hours = 0
	timerstarted = 0
	
init = 0

if init == 0:
    initialise()
    init = 1
	
print "blah"


# top slice - CREATE the GUI
app = gui("Timecalc - GUI V01")

#our timer has not started yet
#we have not counted any seconds, minutes or hours
#set our customer name to null if we just started
#tie all of these into a def, so it does not get called and reset our variables every loop

	
#A loop that is supposed to count our seconds
def mainloop():
	print "Executing main loop"
	#this if statement refuses to trigger
	#don't know how to make an interruptable loop with a gui
	#check if our timer is on or off, if it's on then do the stuff
	print timerstarted
	while timerstarted == 1:
		print "timestuff happened"
		seconds = seconds + 1
		time.sleep(1)
		#needs an interrupt of some description, realistically the if statement should work, but it does not
		mainloop()

	
		
			
#this is what happens when we click the submit button for name
#it must accept an input, even if you don't need one			
def submitname(var):
	print "Submitted name:"
	#here we grab the data from the input field entitled 'customername'
	name = app.getEntry("customername")
	#then we print it out
	print (name)
	
#this triggers when you click the start button
def starttimer(var):
	print "Start Clicked"
	#this is the control variable for the timer, setting it to one should turn it on
	#for some reason, it keeps being set to 0
	timerstarted = 1
	print timerstarted
	#update the start time in the gui with the current time as we just started
	starttime = time.ctime()
	app.setLabel("label_starttime", starttime)
	print starttime
	#not sure if this should be called elsewhere
	mainloop()
	
		


#this is what happens when we click the stop button
def stoptimer(var):
	print "Stop Clicked"
	#our timer control variable is set to zero, off
	timerstarted = 0
	


### fillings go here ###
#addLabel ([ident],[text])
#setLabelBg ([ident],[colour])
#addButton ([ident],[function to to call])

app.addLabel("title", "Time Calculator")
app.setLabelBg("title", "red")
app.startTabbedFrame("TabbedFrame")
app.startTab("Customer")
app.addLabel("label_custname", "Name:")
app.addEntry("customername")
app.addButton("Submit", submitname)
app.stopTab()

app.startTab("Time Calculation")
app.addLabel("label_starttime_prefix", "Start time:")
app.addLabel("label_starttime", "<get current start time here>")
app.addLabel("elapsed_time_prefix", "Elapsed time:")
app.addLabel("label_currentime", "<store time elapsed here>")
app.addButton("Start", starttimer)
app.addButton("Stop", stoptimer)
app.stopTab()

app.stopTabbedFrame()


# bottom slice - START the GUI
mainloop()
app.go()
