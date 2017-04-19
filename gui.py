# import the library
from appJar import gui
var = 0
import datetime
### http://appjar.info/pythonWidgets/
### http://appjar.info/pythonWidgetGrouping/



# top slice - CREATE the GUI
app = gui("Timecalc - GUI V01")

#our timer has not started yet
#we have not counted any seconds, minutes or hours
#set our customer name to null if we just started
#tie all of these into a def, so it does not get called and reset our variables every loop

	
#A loop that is supposed to count our seconds
'''
def mainloop():
	global timerstarted
	global name, seconds, minutes, hours, timerstarted
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
'''
	
def initialise(var):
	print "initialising variables"
	global name, seconds, minutes, hours, timerstarted, ispaused, pausetime, stoppause, startpause, starttime
	name = "NULL"
	seconds = 0
	minutes = 0
	hours = 0
	timerstarted = 0
	ispaused = 2
	pausetime = 0
	stoppause = 0
	startpause = 0
	starttime = 0

init = 0

if init == 0:
    initialise(var)
    init = 1
	
def updategui():
	app.setLabel("label_starttime", starttime)
	app.setLabel("label_pausetime", pausetime)
	app.setLabel("label_stoptime", stoptime)
	app.setLabel("label_elapsedtime", result)
	app.setLabel("label_finaltime", strresult)
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
	global starttime
	#global timerstarted
	print "Start Clicked"
	#this is the control variable for the timer, setting it to one should turn it on
	#for some reason, it keeps being set to 0
	#timerstarted = 1
	#print timerstarted
	#update the start time in the gui with the current time as we just started
	starttime = datetime.datetime.now().replace(microsecond=0)
	app.setLabel("label_starttime", starttime)
	print "Start Time: "
	print starttime
	#not sure if this should be called elsewhere
	#mainloop()
	
def pause(var):	
	global ispaused, startpause, stoppause, pausetime
	print "paused"

	if ispaused == 2:
		startpause = datetime.datetime.now().replace(microsecond=0)
		print "pause clicked"
		ispaused = 1
		return
	if ispaused == 1:
		print "pause clicked again"
		stoppause = datetime.datetime.now().replace(microsecond=0)
		endtime = startpause - stoppause
		endtimepos = -endtime
		pausetime = pausetime + datetime.timedelta.total_seconds(endtimepos)
		app.setLabel("label_pausetime", pausetime)
		ispaused = 2
		
	print "endofpause"
	print "time paused for:"
	print pausetime
	
		
	
	
	
		


#this is what happens when we click the stop button
def stoptimer(var):
	global stoptime, endtime, result, pausetime
	#global timerstarted
	stoptime = datetime.datetime.now().replace(microsecond=0)
	print "Stop Time: "
	print stoptime
	app.setLabel("label_stoptime", stoptime)
	endtime = starttime - stoptime
	result = datetime.timedelta.total_seconds(endtime)
	result = -result
	app.setLabel("label_elapsedtime", result)
	result = result - pausetime
	strresult = str (result)
	print "seconds: "
	print result
	print "Stop Clicked"
	app.setLabel("label_finaltime", strresult)
	#our timer control variable is set to zero, off
	#timerstarted = 0
	
### fillings go here ###
#addLabel ([ident],[text])
#setLabelBg ([ident],[colour])
#addButton ([ident],[function to to call])
app.setGeometry(640, 480)
app.setIcon('icon.ico')



app.startTabbedFrame("TabbedFrame",0,0)

app.startTab("Customer")
app.addLabel("label_custname", "Name:")
app.addEntry("customername")
app.addButton("Submit", submitname)
app.stopTab()

app.startTab("Time Calculation")
app.addLabel("label_starttime_prefix", "Start time:",2)
app.addLabel("label_starttime", "",2,1)
app.addLabel("stoptime_time_prefix", "Stop time:",3)
app.addLabel("label_stoptime", "",3,1)
app.addLabel("pausetime_time_prefix", "Time paused:",4)
app.addLabel("label_pausetime", "",4,1)
app.addLabel("elapsed_time_prefix", "Time elapsed:",5)
app.addLabel("label_elapsedtime", "",5,1)
app.addLabel("finaltime_time_prefix", "Total time:",6)
app.addLabel("label_finaltime", "",6,1)
app.addButton("Start", starttimer, 1, 0)
app.addButton("Pause", pause,1,2)
app.addButton("Stop", stoptimer,1,3)
app.addButton("Clear", initialise,1,4)
app.stopTab()

app.stopTabbedFrame()




# bottom slice - START the GUI

app.go()
