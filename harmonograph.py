# ------------------ First section: import statements -----------------
from tkinter import *
import random
import math
import turtle
# ------------------ Second section: global variables -----------------
firstWindow = None
secondWindow = None
errorWindow = None


# ------------------ Third section: function definitions --------------

# ------------------ GUI functions-------------------------------------
    
def nextProgram():
    global Next
    global xentry
    global yentry
    global xPens
    global yPens    
    global firstWindow
    xPens=int(xentry.get())
    yPens=int(yentry.get())
    if 0<= xPens <=3 and 0<= yPens <=3:
        firstWindow.destroy()
        secondGUI()
    else:
        firstWindow.destroy()
        errorGUI()
        
        

        
        
    

def firstGUI():
    global quit
    global Next
    global xentry
    global yentry
    global firstWindow
    firstWindow = Tk()
    firstWindow.title("Welcome to the Turtle Harmonograph")
    firstWindow.config(bg="RosyBrown")
    label=Label(firstWindow)
    label["text"] = "Welcome to the Turtle Harmonograph Generator!"
    label["bg"] = "RosyBrown"
    label["fg"] = "LightYellow"
    label["relief"] = GROOVE
    label["padx"] = 10
    label["pady"] = 5
    label.grid(row=0, column=0)
    priminstr=Label(firstWindow)
    priminstr["bg"] = "RosyBrown"
    priminstr["fg"] = "LightYellow"
    priminstr["text"] = """This program will create a harmonograph
    based on your preferences. Let's get started!
    How many pendulums would you like? 
    Pick 1, 2, or 3 for both the x and y
    directions and then press Next to proceed."""
    priminstr["justify"] = CENTER
    priminstr["relief"] = SUNKEN
    priminstr["pady"] = 5
    priminstr["padx"] = 15
    priminstr.grid(row=1, column=0)
    
    #entryframe
    entryframe=Frame(firstWindow)
    entryframe["bg"] = "RosyBrown"
    entryframe.grid(row=2, column=0)
    
    #x pendulums label
    xlabel=Label(entryframe)
    xlabel["bg"] = "RosyBrown"
    xlabel["fg"] = "LightYellow"
    xlabel["text"] = "# of X-axis Pendulums:"
    xlabel["justify"] = LEFT
    xlabel.grid(row=0, column=0)
    
    #x pendulums entry
    xentry=Entry(entryframe)
    xentry["bg"] = "LightYellow"
    xentry["fg"] = "RosyBrown"
    xentry["justify"] = LEFT
    xentry.grid(row=0, column=1)
    
    #y pendulums label
    ylabel=Label(entryframe)
    ylabel["bg"] = "RosyBrown"
    ylabel["fg"] = "LightYellow"
    ylabel["text"] = "# of Y-axis Pendulums:"
    ylabel["justify"] = LEFT
    ylabel.grid(row=1, column=0)
    
    #y pendulums entry
    yentry=Entry(entryframe)
    yentry["bg"] = "LightYellow"
    yentry["fg"] = "RosyBrown"
    yentry["justify"] = LEFT
    yentry.grid(row=1, column=1)
    
    #Next button
    Next=Button(entryframe)
    Next["bg"] = "LightYellow"
    Next["fg"] = "RosyBrown"
    Next["text"] = "Next"
    Next["relief"] = RAISED
    Next["command"] = nextProgram
    Next.grid(row=2, column=0)
    
    #Quit button
    quit=Button(entryframe)
    quit["bg"] = "LightYellow"
    quit["fg"] = "RosyBrown"
    quit["text"] = "Quit"
    quit["relief"] = RAISED
    quit["command"] = quitProgram
    quit.grid(row=2, column=1)    
    firstWindow.mainloop()
    
    
def quitProgram():
    global quit
    global firstWindow
    firstWindow.destroy()
    
def errorGUI():
    global errorButt
    global errorWindow
    errorWindow=Tk()
    errorWindow.title("Error!")
    errorWindow.config(bg="RosyBrown")
    errorLabel=Label(errorWindow)
    errorLabel["bg"] = "LightYellow"
    errorLabel["fg"] = "RosyBrown"
    errorLabel["relief"] = SUNKEN
    errorLabel["text"] = "Error! variable(s) out of range. Press Quit and run again!"
    errorLabel.grid(row=0, column=0)
    errorButt=Button(errorWindow)
    errorButt["text"] = "Quit"
    errorButt["command"] = errorQuit
    errorButt.grid(row=1, column=0)
    errorWindow.mainloop()
    
def errorQuit():
    global errorButt
    global errorWindow
    errorWindow.destroy()
    
def Quit2():
    global quit2
    global secondWindow
    secondWindow.destroy()
    
def runProgram():
    global secondWindow
    global xPens
    global yPens
    global run
    global freqEntryx1
    global freqEntryx2
    global freqEntryx3
    global ampEntryx1
    global ampEntryx2
    global ampEntryx3
    global phaseEntryx1
    global phaseEntryx2
    global phaseEntryx3
    global freqEntryy1
    global freqEntryy2
    global freqEntryy3
    global ampEntryy1
    global ampEntryy2
    global ampEntryy3
    global phaseEntryy1
    global phaseEntryy2
    global phaseEntryy3
    global f1
    global f2
    global f3
    global f4
    global f5
    global f6
    global a1
    global a2
    global a3
    global a4
    global a5
    global a6
    global p1
    global p2
    global p3
    global p4
    global p5
    global p6
    if xPens==1:
        f1=int(freqEntryx1.get())
        a1=int(ampEntryx1.get())
        p1=int(phaseEntryx1.get())
    if xPens==2:
        f1=int(freqEntryx1.get())
        a1=int(ampEntryx1.get())
        p1=int(phaseEntryx1.get())
        f2=int(freqEntryx2.get())
        a2=int(freqEntryx2.get())
        p2=int(phaseEntryx2.get())
    if xPens==3:
        f1=int(freqEntryx1.get())
        a1=int(ampEntryx1.get())
        p1=int(phaseEntryx1.get())
        f2=int(freqEntryx2.get())
        a2=int(ampEntryx2.get())
        p2=int(phaseEntryx2.get())
        f3=int(freqEntryx3.get())
        a3=int(ampEntryx3.get())
        p3=int(phaseEntryx3.get())
    if yPens==1:
        f4=int(freqEntryy1.get())
        a4=int(ampEntryy1.get())
        p4=int(phaseEntryy1.get())
    if yPens==2:
        f4=int(freqEntryy1.get())
        a4=int(ampEntryy1.get())
        p4=int(phaseEntryy1.get())
        f5=int(freqEntryy2.get())
        a5=int(ampEntryy2.get())
        p5=int(phaseEntryy2.get())
    if yPens==3:
        f4=int(freqEntryy1.get())
        a4=int(ampEntryy1.get())
        p4=int(phaseEntryy1.get())
        f5=int(freqEntryy2.get())
        a5=int(ampEntryy2.get())
        p5=int(phaseEntryy2.get())
        f6=int(freqEntryy3.get())
        a6=int(ampEntryy3.get())
        p6=int(phaseEntryy3.get())
    secondWindow.destroy()
    
def Randomize():
    global secondWindow
    global randomize 
    global xPens
    global yPens
    global f1
    global f2
    global f3
    global f4
    global f5
    global f6
    global a1
    global a2
    global a3
    global a4
    global a5
    global a6
    global p1
    global p2
    global p3
    global p4
    global p5
    global p6
    if xPens==1:
        f1=random.randrange(0, 10)
        a1=random.randrange(0,250)
        p1=random.randrange(0, 2*3)
    if xPens==2:
        f1=random.randrange(0, 10)
        a1=random.randrange(0,250)
        p1=random.randrange(0, 2*3)
        f2=random.randrange(0, 10)
        a2=random.randrange(0,250)
        p2=random.randrange(0, 2*3) 
    if xPens==3:
        f1=random.randrange(0, 10)
        a1=random.randrange(0,250)
        p1=random.randrange(0, 2*3)
        f2=random.randrange(0, 10)
        a2=random.randrange(0,250)
        p2=random.randrange(0, 2*3)
        f3=random.randrange(0, 10)
        a3=random.randrange(0,250)
        p3=random.randrange(0, 2*3) 
    if yPens==1:
        f4=random.randrange(0, 10)
        a4=random.randrange(0,250)
        p4=random.randrange(0, 2*3)
    if yPens==2:
        f4=random.randrange(0, 10)
        a4=random.randrange(0,250)
        p4=random.randrange(0, 2*3) 
        f5=random.randrange(0, 10)
        a5=random.randrange(0,250)
        p5=random.randrange(0, 2*3)   
    if yPens==3:
        f4=random.randrange(0, 10)
        a4=random.randrange(0,250)
        p4=random.randrange(0, 2*3)        
        f5=random.randrange(0, 10)
        a5=random.randrange(0,250)
        p5=random.randrange(0, 2*3)
        f6=random.randrange(0, 10)
        a6=random.randrange(0,250)
        p6=random.randrange(0, 6)    
    secondWindow.destroy()
        
        
        
    
    
    
    
    
        
    
    
        
    
    

    
        
    
    
def secondGUI():
    global secondWindow
    global xPens
    global yPens
    global quit2
    global run
    global randomize
    global freqEntryx1
    global freqEntryx2
    global freqEntryx3
    global ampEntryx1
    global ampEntryx2
    global ampEntryx3
    global phaseEntryx1
    global phaseEntryx2
    global phaseEntryx3
    global freqEntryy1
    global freqEntryy2
    global freqEntryy3
    global ampEntryy1
    global ampEntryy2
    global ampEntryy3
    global phaseEntryy1
    global phaseEntryy2
    global phaseEntryy3
    global f2
    global f3
    global a2
    global a3
    global p2
    global p3
    global f5
    global f6
    global a5
    global a6
    global p5
    global p6
    secondWindow=Tk()
    secondWindow.title("Pendulum Variables")
    secondWindow.config(bg="RosyBrown")
    entrydirections=Label(secondWindow)
    entrydirections["text"] = """Please enter the desired values
    for the Frequency, Amplitudes, and
    Phases of the Pendulums, or press
    randomize to generate random values!
    Ranges:
    1<Frequency<10
    0<Amplitude<300 (sum of x or y values cannot exceed 500)
    0<Phases<2*pi"""
    entrydirections["bg"] = "RosyBrown"
    entrydirections["fg"] = "LightYellow"
    entrydirections["relief"] = GROOVE
    entrydirections["justify"] = CENTER
    entrydirections.grid(row=0, column=0)
    ventry=Frame(secondWindow)
    ventry["bg"] = "RosyBrown"
    ventry.grid(row=1, column=0)
    if xPens==1:
        #label
        freqLabelx1=Label(ventry)
        freqLabelx1["text"] = "Fequency for x-axis Pendulum 1:"
        freqLabelx1["bg"] = "RosyBrown"
        freqLabelx1["fg"] = "LightYellow"
        freqLabelx1.grid(row=0, column=0)
        #entry
        freqEntryx1=Entry(ventry)
        freqEntryx1["bg"] = "LightYellow"
        freqEntryx1["fg"] = "RosyBrown"
        freqEntryx1.grid(row=0, column=1)
        #lbel
        ampLabelx1=Label(ventry)
        ampLabelx1["text"] = "Amplitude:"
        ampLabelx1["bg"] = "RosyBrown"
        ampLabelx1["fg"] = "LightYellow"        
        ampLabelx1.grid(row=0, column=2)
        #entry
        ampEntryx1=Entry(ventry)
        ampEntryx1["bg"] = "LightYellow"
        ampEntryx1["fg"] = "RosyBrown"        
        ampEntryx1.grid(row=0, column=3)
        #label
        phaseLabelx1=Label(ventry)
        phaseLabelx1["text"] = "Phases:"
        phaseLabelx1["bg"] = "RosyBrown"
        phaseLabelx1["fg"] = "LightYellow"        
        phaseLabelx1.grid(row=0, column=4)
        #entry
        phaseEntryx1=Entry(ventry)
        phaseEntryx1["bg"] = "LightYellow"
        phaseEntryx1["fg"] = "RosyBrown"        
        phaseEntryx1.grid(row=0, column=5)
        f2=0
        f3=0
        a2=0
        a3=0
        p2=0
        p3=0
        
    if xPens==2:
        #label
        freqLabelx1=Label(ventry)
        freqLabelx1["text"] = "Fequency for x-axis Pendulum 1:"
        freqLabelx1["bg"] = "RosyBrown"
        freqLabelx1["fg"] = "LightYellow"        
        freqLabelx1.grid(row=0, column=0)
        #entry
        freqEntryx1=Entry(ventry)
        freqEntryx1["bg"] = "LightYellow"
        freqEntryx1["fg"] = "RosyBrown"        
        freqEntryx1.grid(row=0, column=1)
        #lbel
        ampLabelx1=Label(ventry)
        ampLabelx1["text"] = "Amplitude:"
        ampLabelx1["bg"] = "RosyBrown"
        ampLabelx1["fg"] = "LightYellow"        
        ampLabelx1.grid(row=0, column=2)
        #entry
        ampEntryx1=Entry(ventry)
        ampEntryx1["bg"] = "LightYellow"
        ampEntryx1["fg"] = "RosyBrown"
        ampEntryx1.grid(row=0, column=3)
        #label
        phaseLabelx1=Label(ventry)
        phaseLabelx1["text"] = "Phases:"
        phaseLabelx1["bg"] = "RosyBrown"
        phaseLabelx1["fg"] = "LightYellow"        
        phaseLabelx1.grid(row=0, column=4)
        #entry
        phaseEntryx1=Entry(ventry)
        phaseEntryx1["bg"] = "LightYellow"
        phaseEntryx1["fg"] = "RosyBrown"
        phaseEntryx1.grid(row=0, column=5)
        #label
        freqLabelx2=Label(ventry)
        freqLabelx2["text"] = "Fequency for x-axis Pendulum 2:"
        freqLabelx2["bg"] = "RosyBrown"
        freqLabelx2["fg"] = "LightYellow"
        freqLabelx2.grid(row=1, column=0)
        #entry
        freqEntryx2=Entry(ventry)
        freqEntryx2["bg"] = "LightYellow"
        freqEntryx2["fg"] = "RosyBrown"
        freqEntryx2.grid(row=1, column=1)
        #lbel
        ampLabelx2=Label(ventry)
        ampLabelx2["text"] = "Amplitude:"
        ampLabelx2["bg"] = "RosyBrown"
        ampLabelx2["fg"] = "LightYellow"        
        ampLabelx2.grid(row=1, column=2)
        #entry
        ampEntryx2=Entry(ventry)
        ampEntryx2["bg"] = "LightYellow"
        ampEntryx2["fg"] = "RosyBrown"
        ampEntryx2.grid(row=1, column=3)
        #label
        phaseLabelx2=Label(ventry)
        phaseLabelx2["text"] = "Phases:"
        phaseLabelx2["bg"] = "RosyBrown"
        phaseLabelx2["fg"] = "LightYellow"        
        phaseLabelx2.grid(row=1, column=4)
        #entry
        phaseEntryx2=Entry(ventry)
        phaseEntryx2["bg"] = "LightYellow"
        phaseEntryx2["fg"] = "RosyBrown"
        phaseEntryx2.grid(row=1, column=5)
        f3=0
        a3=0
        p3=0
    if xPens==3:
        #label
        freqLabelx1=Label(ventry)
        freqLabelx1["text"] = "Fequency for x-axis Pendulum 1:"
        freqLabelx1["bg"] = "RosyBrown"
        freqLabelx1["fg"] = "LightYellow"          
        freqLabelx1.grid(row=0, column=0)
        #entry
        freqEntryx1=Entry(ventry)
        freqEntryx1["bg"] = "LightYellow"
        freqEntryx1["fg"] = "RosyBrown"          
        freqEntryx1.grid(row=0, column=1)
        #lbel
        ampLabelx1=Label(ventry)
        ampLabelx1["text"] = "Amplitude:"
        ampLabelx1["bg"] = "RosyBrown"
        ampLabelx1["fg"] = "LightYellow"         
        ampLabelx1.grid(row=0, column=2)
        #entry
        ampEntryx1=Entry(ventry)
        ampEntryx1["bg"] = "LightYellow"
        ampEntryx1["fg"] = "RosyBrown"        
        ampEntryx1.grid(row=0, column=3)
        #label
        phaseLabelx1=Label(ventry)
        phaseLabelx1["text"] = "Phases:"
        phaseLabelx1["bg"] = "RosyBrown"
        phaseLabelx1["fg"] = "LightYellow"          
        phaseLabelx1.grid(row=0, column=4)
        #entry
        phaseEntryx1=Entry(ventry)
        phaseEntryx1["bg"] = "LightYellow"
        phaseEntryx1["fg"] = "RosyBrown"        
        phaseEntryx1.grid(row=0, column=5)
        #label
        freqLabelx2=Label(ventry)
        freqLabelx2["text"] = "Fequency for x-axis Pendulum 2:"
        freqLabelx2["bg"] = "RosyBrown"
        freqLabelx2["fg"] = "LightYellow"        
        freqLabelx2.grid(row=1, column=0)
        #entry
        freqEntryx2=Entry(ventry)
        freqEntryx2["bg"] = "LightYellow"
        freqEntryx2["fg"] = "RosyBrown"        
        freqEntryx2.grid(row=1, column=1)
        #lbel
        ampLabelx2=Label(ventry)
        ampLabelx2["text"] = "Amplitude:"
        ampLabelx2["bg"] = "RosyBrown"
        ampLabelx2["fg"] = "LightYellow"        
        ampLabelx2.grid(row=1, column=2)
        #entry
        ampEntryx2=Entry(ventry)
        ampEntryx2["bg"] = "LightYellow"
        ampEntryx2["fg"] = "RosyBrown"        
        ampEntryx2.grid(row=1, column=3)
        #label
        phaseLabelx2=Label(ventry)
        phaseLabelx2["text"] = "Phases:"
        phaseLabelx2["bg"] = "RosyBrown"
        phaseLabelx2["fg"] = "LightYellow"        
        phaseLabelx2.grid(row=1, column=4)
        #entry
        phaseEntryx2=Entry(ventry)
        phaseEntryx2["bg"] = "LightYellow"
        phaseEntryx2["fg"] = "RosyBrown"
        phaseEntryx2.grid(row=1, column=5)
        #label
        freqLabelx3=Label(ventry)
        freqLabelx3["text"] = "Fequency for x-axis Pendulum 3:"
        freqLabelx3["bg"] = "RosyBrown"
        freqLabelx3["fg"] = "LightYellow"
        freqLabelx3.grid(row=2, column=0)
        #entry
        freqEntryx3=Entry(ventry)
        freqEntryx3["bg"] = "LightYellow"
        freqEntryx3["fg"] = "RosyBrown"
        freqEntryx3.grid(row=2, column=1)
        #lbel
        ampLabelx3=Label(ventry)
        ampLabelx3["text"] = "Amplitude:"
        ampLabelx3["bg"] = "RosyBrown"
        ampLabelx3["fg"] = "LightYellow"        
        ampLabelx3.grid(row=2, column=2)
        #entry
        ampEntryx3=Entry(ventry)
        ampEntryx3["bg"] = "LightYellow"
        ampEntryx3["fg"] = "RosyBrown"
        ampEntryx3.grid(row=2, column=3)
        #label
        phaseLabelx3=Label(ventry)
        phaseLabelx3["text"] = "Phases:"
        phaseLabelx3["bg"] = "RosyBrown"
        phaseLabelx3["fg"] = "LightYellow"        
        phaseLabelx3.grid(row=2, column=4)
        #entry
        phaseEntryx3=Entry(ventry)
        phaseEntryx3["bg"] = "LightYellow"
        phaseEntryx3["fg"] = "RosyBrown"
        phaseEntryx3.grid(row=2, column=5)
        
        #ypens
    if yPens==1:
        #label
        freqLabely1=Label(ventry)
        freqLabely1["text"] = "Fequency for y-axis Pendulum 1:"
        freqLabely1["bg"] = "RosyBrown"
        freqLabely1["fg"] = "LightYellow"        
        freqLabely1.grid(row=xPens, column=0)
        #entry
        freqEntryy1=Entry(ventry)
        freqEntryy1["bg"] = "LightYellow"
        freqEntryy1["fg"] = "RosyBrown"        
        freqEntryy1.grid(row=xPens, column=1)
        #lbel
        ampLabely1=Label(ventry)
        ampLabely1["text"] = "Amplitude:"
        ampLabely1["bg"] = "RosyBrown"
        ampLabely1["fg"] = "LightYellow"        
        ampLabely1.grid(row=xPens, column=2)
        #entry
        ampEntryy1=Entry(ventry)
        ampEntryy1["bg"] = "LightYellow"
        ampEntryy1["fg"] = "RosyBrown"        
        ampEntryy1.grid(row=xPens, column=3)
        #label
        phaseLabely1=Label(ventry)
        phaseLabely1["text"] = "Phases:"
        phaseLabely1["bg"] = "RosyBrown"
        phaseLabely1["fg"] = "LightYellow"        
        phaseLabely1.grid(row=xPens, column=4)
        #entry
        phaseEntryy1=Entry(ventry)
        phaseEntryy1["bg"] = "LightYellow"
        phaseEntryy1["fg"] = "RosyBrown"        
        phaseEntryy1.grid(row=xPens, column=5)
        f5=0
        f6=0
        a5=0
        a6=0
        p5=0
        p6=0
    if yPens==2:
        #label
        freqLabely1=Label(ventry)
        freqLabely1["text"] = "Fequency for y-axis Pendulum 1:"
        freqLabely1["bg"] = "RosyBrown"
        freqLabely1["fg"] = "LightYellow"        
        freqLabely1.grid(row=xPens, column=0)
        #entry
        freqEntryy1=Entry(ventry)
        freqEntryy1["bg"] = "LightYellow"
        freqEntryy1["fg"] = "RosyBrown"        
        freqEntryy1.grid(row=xPens, column=1)
        #lbel
        ampLabely1=Label(ventry)
        ampLabely1["bg"] = "RosyBrown"
        ampLabely1["fg"] = "LightYellow"        
        ampLabely1["text"] = "Amplitude:"
        ampLabely1.grid(row=xPens, column=2)
        #entry
        ampEntryy1=Entry(ventry)
        ampEntryy1["bg"] = "LightYellow"
        ampEntryy1["fg"] = "RosyBrown"        
        ampEntryy1.grid(row=xPens, column=3)
        #label
        phaseLabely1=Label(ventry)
        phaseLabely1["bg"] = "RosyBrown"
        phaseLabely1["fg"] = "LightYellow"        
        phaseLabely1["text"] = "Phases:"
        phaseLabely1.grid(row=xPens, column=4)
        #entry
        phaseEntryy1=Entry(ventry)
        phaseEntryy1["bg"] = "LightYellow"
        phaseEntryy1["fg"] = "RosyBrown"        
        phaseEntryy1.grid(row=xPens, column=5)
        #label
        freqLabely2=Label(ventry)
        freqLabely2["text"] = "Fequency for y-axis Pendulum 2:"
        freqLabely2["bg"] = "RosyBrown"
        freqLabely2["fg"] = "LightYellow"        
        freqLabely2.grid(row=xPens+1, column=0)
        #entry
        freqEntryy2=Entry(ventry)
        freqEntryy2["bg"] = "LightYellow"
        freqEntryy2["fg"] = "RosyBrown"        
        freqEntryy2.grid(row=xPens+1, column=1)
        #lbel
        ampLabely2=Label(ventry)
        ampLabely2["text"] = "Amplitude:"
        ampLabely2["bg"] = "RosyBrown"
        ampLabely2["fg"] = "LightYellow"        
        ampLabely2.grid(row=xPens+1, column=2)
        #entry
        ampEntryy2=Entry(ventry)
        ampEntryy2["bg"] = "LightYellow"
        ampEntryy2["fg"] = "RosyBrown"        
        ampEntryy2.grid(row=xPens+1, column=3)
        #label
        phaseLabely2=Label(ventry)
        phaseLabely2["text"] = "Phases:"
        phaseLabely2["bg"] = "RosyBrown"
        phaseLabely2["fg"] = "LightYellow"        
        phaseLabely2.grid(row=xPens+1, column=4)
        #entry
        phaseEntryy2=Entry(ventry)
        phaseEntryy2["bg"] = "LightYellow"
        phaseEntryy2["fg"] = "RosyBrown"        
        phaseEntryy2.grid(row=xPens+1, column=5)
        f6=0
        a6=0
        p6=0
    if yPens==3:
        #label
        freqLabely1=Label(ventry)
        freqLabely1["text"] = "Fequency for y-axis Pendulum 1:"
        freqLabely1["bg"] = "RosyBrown"
        freqLabely1["fg"] = "LightYellow"
        freqLabely1.grid(row=xPens, column=0)
        #entry
        freqEntryy1=Entry(ventry)
        freqEntryy1["bg"] = "LightYellow"
        freqEntryy1["fg"] = "RosyBrown"
        freqEntryy1.grid(row=xPens, column=1)
        #lbel
        ampLabely1=Label(ventry)
        ampLabely1["text"] = "Amplitude:"
        ampLabely1["bg"] = "RosyBrown"
        ampLabely1["fg"] = "LightYellow"
        ampLabely1.grid(row=xPens, column=2)
        #entry
        ampEntryy1=Entry(ventry)
        ampEntryy1["bg"] = "LightYellow"
        ampEntryy1["fg"] = "RosyBrown"
        ampEntryy1.grid(row=xPens, column=3)
        #label
        phaseLabely1=Label(ventry)
        phaseLabely1["text"] = "Phases:"
        phaseLabely1["bg"] = "RosyBrown"
        phaseLabely1["fg"] = "LightYellow"
        phaseLabely1.grid(row=xPens, column=4)
        #entry
        phaseEntryy1=Entry(ventry)
        phaseEntryy1["bg"] = "LightYellow"
        phaseEntryy1["fg"] = "RosyBrown"
        phaseEntryy1.grid(row=xPens, column=5)
        #label
        freqLabely2=Label(ventry)
        freqLabely2["text"] = "Fequency for y-axis Pendulum 2:"
        freqLabely2["bg"] = "RosyBrown"
        freqLabely2["fg"] = "LightYellow"
        freqLabely2.grid(row=xPens+1, column=0)
        #entry
        freqEntryy2=Entry(ventry)
        freqEntryy2["bg"] = "LightYellow"
        freqEntryy2["fg"] = "RosyBrown"
        freqEntryy2.grid(row=xPens+1, column=1)
        #lbel
        ampLabely2=Label(ventry)
        ampLabely2["text"] = "Amplitude:"
        ampLabely2["bg"] = "RosyBrown"
        ampLabely2["fg"] = "LightYellow"
        ampLabely2.grid(row=xPens+1, column=2)
        #entry
        ampEntryy2=Entry(ventry)
        ampEntryy2["bg"] = "LightYellow"
        ampEntryy2["fg"] = "RosyBrown"
        ampEntryy2.grid(row=xPens+1, column=3)
        #label
        phaseLabely2=Label(ventry)
        phaseLabely2["text"] = "Phases:"
        phaseLabely2["bg"] = "RosyBrown"
        phaseLabely2["fg"] = "LightYellow"
        phaseLabely2.grid(row=xPens+1, column=4)
        #entry
        phaseEntryy2=Entry(ventry)
        phaseEntryy2["bg"] = "LightYellow"
        phaseEntryy2["fg"] = "RosyBrown"
        phaseEntryy2.grid(row=xPens+1, column=5)
        #label
        freqLabely3=Label(ventry)
        freqLabely3["text"] = "Fequency for y-axis Pendulum 3:"
        freqLabely3["bg"] = "RosyBrown"
        freqLabely3["fg"] = "LightYellow"
        freqLabely3.grid(row=xPens+2, column=0)
        #entry
        freqEntryy3=Entry(ventry)
        freqEntryy3["bg"] = "LightYellow"
        freqEntryy3["fg"] = "RosyBrown"
        freqEntryy3.grid(row=xPens+2, column=1)
        #lbel
        ampLabely3=Label(ventry)
        ampLabely3["text"] = "Amplitude:"
        ampLabely3["bg"] = "RosyBrown"
        ampLabely3["fg"] = "LightYellow"
        ampLabely3.grid(row=xPens+2, column=2)
        #entry
        ampEntryy3=Entry(ventry)
        ampEntryy3["bg"] = "LightYellow"
        ampEntryy3["fg"] = "RosyBrown"
        ampEntryy3.grid(row=xPens+2, column=3)
        #label
        phaseLabely3=Label(ventry)
        phaseLabely3["text"] = "Phases:"
        phaseLabely3["bg"] = "RosyBrown"
        phaseLabely3["fg"] = "LightYellow"
        phaseLabely3.grid(row=xPens+2, column=4)
        #entry
        phaseEntryy3=Entry(ventry)
        phaseEntryy3["bg"] = "LightYellow"
        phaseEntryy3["fg"] = "RosyBrown"
        phaseEntryy3.grid(row=xPens+2, column=5)
        
    #buttons
    run=Button(ventry)
    run["text"] = "Run!"
    run["command"] = runProgram
    run.grid(row=xPens+yPens, column=0)
    randomize=Button(ventry)
    randomize["text"] = "Randomize!"
    randomize["command"] = Randomize
    randomize.grid(row=xPens+yPens, column=2)
    quit2=Button(ventry)
    quit2["text"] = "Quit"
    quit2["command"] = Quit2
    quit2.grid(row=xPens+yPens, column=5)
        
        
        
    secondWindow.mainloop()
    
    
# ------------------ Fourth section: script elements ------------------
firstGUI()

def harmonograph(f1, p1, a1, f2, p2, a2, f3, p3, a3, f4, p4, a4, f5, p5, a5, f6, p6, a6):
        wn = turtle.Screen()
        ronald = turtle.Turtle()
        ronald.speed(100)        
        def Pendulum1(t):
                return a1*math.sin(f1*float(t/30)+p1)*math.exp(-0.01*float(t/30))
        def Pendulum2(t):
                return a2*math.sin(f2*float(t/30)+p2)*math.exp(-0.01*float(t/30))
        def Pendulum3(t):
                return a3*math.sin(f3*float(t/30)+p3)*math.exp(-0.01*float(t/30))
        def Pendulum4(t):
                return a4*math.sin(f4*float(t/30)+p4)*math.exp(-0.01*float(t/30))
        def Pendulum5(t):
                return a5*math.sin(f5*float(t/30)+p5)*math.exp(-0.01*float(t/30))
        def Pendulum6(t):
                return a6*math.sin(f6*float(t/30)+p6)*math.exp(-0.01*float(t/30))
        ronald.up()
        ronald.goto(Pendulum1(0) + Pendulum2(0) + Pendulum3(0), Pendulum4(0) + Pendulum5(0) + Pendulum6(0))
        ronald.down()
        print("Pendulum 1 has a frequency " + str(f1) + ", a phase " + str(p1) + ", and an amplitude " + str(a1))
        print("Pendulum 2 has a frequency " + str(f2) + ", a phase " + str(p2) + ", and an amplitude " + str(a2))
        print("Pendulum 3 has a frequency " + str(f3) + ", a phase " + str(p3) + ", and an amplitude " + str(a3))
        print("Pendulum 4 has a frequency " + str(f4) + ", a phase " + str(p4) + ", and an amplitude " + str(a4))
        print("Pendulum 5 has a frequency " + str(f5) + ", a phase " + str(p5) + ", and an amplitude " + str(a5))
        print("Pendulum 6 has a frequency " + str(f6) + ", a phase " + str(p6) + ", and an amplitude " + str(a6))
        for t in range(10000): 
                targetX = Pendulum1(t) + Pendulum2(t) + Pendulum3(t)
                targetY = Pendulum4(t) + Pendulum5(t) + Pendulum6(t)
                ronald.goto(targetX,targetY)


harmonograph(f1, p1, a1, f2, p2, a2, f3, p3, a3, f4, p4, a4, f5, p5, a5, f6, p6, a6)
#GUIMain()
