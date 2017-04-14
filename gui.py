# import the library
from appJar import gui

import time
### http://appjar.info/pythonWidgets/
### http://appjar.info/pythonWidgetGrouping/


# top slice - CREATE the GUI
app = gui("Timecalc - GUI V01")

#our timer has not started yet
timerstarted = 0

#we have not counted any seconds, minutes or hours
seconds = 0
minutes = 0
hours = 0

#set our customer name to null if we just started
name = "NULL"

#A loop that is supposed to count our seconds
def mainloop():
	print "Executing main loop"
	#this if statement refuses to trigger
	#don't know how to make an interruptable loop with a gui
	if timerstarted == '1':
		print "timestuff happened"
		seconds = seconds + 1
		time.sleep(1)
		mainloop()
	
		
			
#this is what happens when we click the submit button for name
#it must accept an input, even if you don't need one			
def submitname(var):
	print "Submitted name:"
	#here we grab the data from the input field entitled 'customername'
	name = app.getEntry("customername")
	#then we print it out
	print (name)
	
def starttimer(var):
	print "Started timer"
	timerstarted = 1;
	starttime = time.ctime()
	app.setLabel("label_starttime", starttime)
	print starttime
	mainloop()
	
		


	
def stoptimer(var):
	print "Stopped timer"
	timerstarted = 0;
	


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
