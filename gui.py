# import the library
from appJar import gui

# top slice - CREATE the GUI


def press(btnName):
    if btnName == "quit":
        app.stop()
        return
    if btnName == "starttimer":
        starttimer()
        return
    if btnName == "stoptimer":
        stoptimer()
        return
    if btnName == "submitname":
		name = userEnt
		print(name)
		return

app = gui("Timecalc - GUI V01")
### fillings go here ###
app.addLabel("title", "Time Calculator")
app.setLabelBg("title", "red")
app.addLabel("custname", "Customer Name:", 0, 0)
app.addEntry("userEnt", 0, 1)
app.addButton("Submit Name", submitname)


# bottom slice - START the GUI
app.go()