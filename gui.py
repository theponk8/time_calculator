# import the library
from appJar import gui
### http://appjar.info/pythonWidgets/
### http://appjar.info/pythonWidgetGrouping/

# top slice - CREATE the GUI
app = gui("Timecalc - GUI V01")

#set our customer name to null if we just started
name = "NULL"
#this is what happens when we click the submit button for name
#it must accept an input, even if you don't need one
def submitname(var):
	print "Submitted name:"
	name = app.getEntry("customername")
	print (name)



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
app.stopTab()

app.stopTabbedFrame()


# bottom slice - START the GUI
app.go()