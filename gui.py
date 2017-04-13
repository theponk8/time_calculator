# import the library
from appJar import gui

# top slice - CREATE the GUI
app = gui("Timecalc - GUI V01")
name = "NULL"
def submitname(var):
	print "Submitted name:"
	name = app.getEntry("customername")
	print (name)



### fillings go here ###
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
app.stopTab()

app.stopTabbedFrame()


# bottom slice - START the GUI
app.go()