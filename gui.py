# import the library
from appJar import gui
var = 0
import datetime, csv, webbrowser
### http://appjar.info/pythonWidgets/
### http://appjar.info/pythonWidgetGrouping/
global name, seconds, minutes, hours, timerstarted, ispaused, pausetime, stoppause, startpause, starttime, todo


# top slice - CREATE the GUI
app = gui("Timecalc - GUI V0.02")
#####################
# CLASS & OTHER OOP #
#####################
class Customer:
	name = "Default"
	starttime = ""
	stoptime = ""
	cost = ""
	time = ""

###############
# ORPHAN CODE #
###############

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

#might swap over to this rather than in each function

def updategui():
	app.setLabel("label_starttime", starttime)
	app.setLabel("label_pausetime", pausetime)
	app.setLabel("label_stoptime", stoptime)
	app.setLabel("label_elapsedtime", result)
	app.setLabel("label_finaltime", strresult)
'''
###################
# OTHER FUNCTIONS #
###################
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

	
if init == 0:
    initialise(var)
    init = 1
	

####################
# BUTTON FUNCTIONS #
####################

#Dumps the content of our data class to csv
def log_out(var):
	print "Begin Logging"
	global filename
	#Generate the filename by using the customer name
	filename = Customer.name
	filename += ".csv"
	f =open(filename, 'w')


	f.write(str (Customer.name))
	f.write(",")
	f.write(str (Customer.starttime))
	f.write(",")
	f.write(str (Customer.stoptime))
	f.write(",")
	f.write(str (Customer.cost))
	f.write(",")
	f.write(str (Customer.time))
### not implemented
def log_in(var):
	global filename
	filename = Customer.name
	filename += ".csv"
	f = open(filename, 'r') 
	readfile = csv.reader(f, delimiter=' ', quotechar='|')
	#Customer.name = readfile[0]
	for row in readfile:
		print ','.join(row)
	
	
	
	
	
#Dumps the content of our data class to terminal
def log_dump(var):
	print (Customer.name)
	print (Customer.starttime)
	print (Customer.stoptime)
	print (Customer.cost)

### Debug Button
# For testing partially implemented stuff and displaying various variables
# Should write this into a function that accepts a list of globals
def debug(var):
	#fill this out as needed
	global name, seconds, minutes, hours, timerstarted, ispaused, pausetime, stoppause, startpause, starttime
	app.setLabel("debug_timerstarted", timerstarted)
	app.setLabel("debug_ispaused", ispaused)
	app.setTextArea("todo_1", todo)
	
### Submit Button
#this is what happens when we click the submit button for name
#it must accept an input, even if you don't need one			
def submitname(var):
	
	print "Submitted name:"
	#here we grab the data from the input field entitled 'customername'
	name = app.getEntry("customername")
	#then we print it out
	print (name)
	#add to our class
	Customer.name = name
	

### Start Button	
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
	Customer.starttime = starttime

	

### Pause Button	
#triggers when pause is clicked
#this is virtually the same as the start/stop function
'''
ispaused 0 = error
ispaused 2 = initial/have not clicked yet *set on initialise function
ispaused 1 = we have clicked it
'''
def pause(var):	
	global ispaused, startpause, stoppause, pausetime
	print "pause function called"
	#this is our first time clicking pause so do this:
	if ispaused == 2:
		#grab initial time
		startpause = datetime.datetime.now().replace(microsecond=0)
		print "pause clicked"
		#we have now clicked pause
		ispaused = 1
		#get us out of here, because we only want to click once
		return
	#if we have clicked pause once already, do this:
	if ispaused == 1:
		print "pause clicked again"
		#grab pause time, work out the difference, add it to our total pause time, update label, reset pause button
		stoppause = datetime.datetime.now().replace(microsecond=0)
		endtime = startpause - stoppause
		endtimepos = -endtime
		pausetime = pausetime + datetime.timedelta.total_seconds(endtimepos)
		app.setLabel("label_pausetime", pausetime)
		ispaused = 2
		
	print "endofpause"
	print "time paused for:"
	print pausetime
	Customer.pausetime = pausetime
#???
def rick(var):
	webbrowser.open("https://youtu.be/Gc2u6AFImn8")
	
### Stop Button	
#this is what happens when we click the stop button
def stoptimer(var):
	global stoptime, endtime, result, pausetime
	#theponk's placeholder cost variable:
	z = 0
	
	#grab our stop time
	stoptime = datetime.datetime.now().replace(microsecond=0)
	print "Stop Time: "
	print stoptime
	#update stoptime on the ui
	#do the math, figure out resulting time
	app.setLabel("label_stoptime", stoptime)
	endtime = starttime - stoptime
	result = datetime.timedelta.total_seconds(endtime)
	result = -result
	#sends the total amount of time elapsed
	app.setLabel("label_elapsedtime", result)
	result = result - pausetime
	strresult = str (result)
	print "seconds: "
	print result
	print "Stop Clicked"
	#sends the actual time elapsed (time elapsed - pause time)
	app.setLabel("label_finaltime", strresult)
	Customer.time = strresult
	#thanks for this
	#calculate the cost
	z = result /60 /30
	#always charge $49.50 - This would appear to round up
	if z < 1:
		z = z + 1
	#calculates the price
	cost = z * 49.50
	#update the label for cost, complete with free formatting
	app.setLabel("label_cost", '${:,.2f}'.format(cost))
	Customer.cost = cost
	Customer.stoptime = stoptime

##############
# UI SECTION #
##############
#addLabel ([ident],[text])
#setLabelBg ([ident],[colour])
#addButton ([ident],[function to to call])
#set our icon and resolution

app.setGeometry(640, 480)
app.setIcon('icon.ico')


#we have the whole thing in a frame
app.startTabbedFrame("TabbedFrame",0,0)
#customer tab


#time calculation tab
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
#control grouping
app.startLabelFrame("Controls")
app.addButton("Start", starttimer, 1, 0)
app.addButton("Pause", pause,1,2)
app.addButton("Stop", stoptimer,1,3)
app.addButton("Clear", initialise,1,4)
app.addLabel("label_custname", "Name:")
app.addEntry("customername")
app.addButton("Submit Name", submitname)
app.addButton("Save", log_out)
app.addButton("Load", log_in)
app.addButton("?", rick)
app.stopLabelFrame()

app.stopTab()

#debug tab
app.startTab("Debug & Tests")
#debug
app.startLabelFrame("Debug Data",1,0)
app.addButton("debug", debug)
app.addLabel("debug_1", "timerstarted: ")
app.addLabel("debug_timerstarted", "")
app.addLabel("debug_2", "ispaused: ")
app.addLabel("debug_ispaused", "")
app.addLabel("debug_3", "etc")
app.stopLabelFrame()
#logging
app.startLabelFrame("Logging Tests",1,1)
app.addLabel("logging_1", "Put logging stuff here (hint: nothing to do with wood)")
app.addButton("log", log_out)
app.addButton("dumpdata", log_dump)
app.stopLabelFrame()
app.stopTab()
app.startTab("Todo")
app.addScrolledTextArea("todo_1")
app.stopTab()



#help tab
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
