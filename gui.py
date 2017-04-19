# import the library
from appJar import gui
var = 0
import datetime
### http://appjar.info/pythonWidgets/
### http://appjar.info/pythonWidgetGrouping/
global name, seconds, minutes, hours, timerstarted, ispaused, pausetime, stoppause, startpause, starttime, todo


# top slice - CREATE the GUI
app = gui("Timecalc - GUI V0.02")

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
	global name, seconds, minutes, hours, timerstarted, ispaused, pausetime, stoppause, startpause, starttime, todo
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
	todo = open('todo.txt', 'r').read()
	
	

init = 0
def debug(var):
	#fill this out as needed
	global name, seconds, minutes, hours, timerstarted, ispaused, pausetime, stoppause, startpause, starttime
	app.setLabel("debug_timerstarted", timerstarted)
	app.setLabel("debug_ispaused", ispaused)
	app.setTextArea("todo_1", todo)
	
	
if init == 0:
    initialise(var)
    init = 1
	
#might swap over to this rather than in each function
'''
def updategui():
	app.setLabel("label_starttime", starttime)
	app.setLabel("label_pausetime", pausetime)
	app.setLabel("label_stoptime", stoptime)
	app.setLabel("label_elapsedtime", result)
	app.setLabel("label_finaltime", strresult)
'''

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
	z = 0
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
	#calculate the cost
	z = result /60 /30
	#always charge $49.50 - This would appear to round up
	if z < 1:
		z = z + 1
	#calculates the price
	cost = z * 49.50
	app.setLabel("label_cost", '${:,.2f}'.format(cost))
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
app.addLabel("cost_prefix", "Fee:",7)
app.addLabel("label_cost", "",7,1)
app.startLabelFrame("Controls")
app.addButton("Start", starttimer, 1, 0)
app.addButton("Pause", pause,1,2)
app.addButton("Stop", stoptimer,1,3)
app.addButton("Clear", initialise,1,4)
app.stopLabelFrame()

app.stopTab()

app.startTab("Debug & Tests")
app.startLabelFrame("Debug Data",1,0)
app.addButton("debug", debug)
app.addLabel("debug_1", "timerstarted: ")
app.addLabel("debug_timerstarted", "")
app.addLabel("debug_2", "ispaused: ")
app.addLabel("debug_ispaused", "")
app.addLabel("debug_3", "etc")


app.stopLabelFrame()
app.startLabelFrame("Logging Tests",1,1)
app.addLabel("logging_1", "Put logging stuff here (hint: nothing to do with wood)")
app.stopLabelFrame()
app.stopTab()
app.startTab("Todo")
app.addScrolledTextArea("todo_1")
app.stopTab()




app.startTab("Help")
app.addLabel("label_help1", "Press the start button to start the timer.",2)
app.addLabel("label_help2", "Press the pause button to start the pause timer.",3)
app.addLabel("label_help3", "Press pause again to stop the pause timer.",4)
app.addLabel("label_help4", "Upon pressing stop, the program will calculate the total time",5)
app.addLabel("label_help5", "Pressing the debug button loads the todolist",5)
app.stopTab()

app.stopTabbedFrame()




# bottom slice - START the GUI

app.go()
