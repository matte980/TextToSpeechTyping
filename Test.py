import pyttsx3
engine = pyttsx3.init() # object creation

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 150)     # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

with open('TextToSay.txt', 'r', encoding='utf-8') as f:
    text = f.read()

print(text)

engine.say(text)
engine.runAndWait()
engine.stop()

"""Saving Voice to a file"""
# On linux make sure that 'espeak' and 'ffmpeg' are installed
# engine.save_to_file('Hello World', 'test.mp3')
# engine.runAndWait()


def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

# ----------------------------------------------------------------------------
# MAIN
root = tk.Tk()
root.geometry('700x300+300+200')
root.wm_attributes('-topmost', 1)

root.columnconfigure((0,1,2,3,4), weight= 1)
root.rowconfigure((1), weight= 1)

#   TEXTVARIABLES IN TEXT
sv = tk.StringVar()
sv.trace('w', lambda name, index, mode, sv=sv: callback(sv))

#   WIDGETS
restartB = tk.Button(root, text='Restart', font=("Helvetica", 11), command= lambda: restart_program(), state = 'disabled')
restartB.grid(row = 0, column = 0, sticky = 'nw')

timeLabel = tk.Label(root, font=('Helvetica', 11), bd = 0, text = '1:00')
timeLabel.grid(row = 0, column = 4, sticky = 'ne')

T = tk.Text(root, font=('Helvetica', 50), bd = 0, bg = '#f5f5f5', wrap = 'word')
T.grid(row = 1, column = 0, columnspan = 5, sticky = 'ew')

fillText()

# changeWord()

# scrollWords()
# scrollWords()
# scrollWords()
# actIndex=0

tEntry = tk.Entry(root, text='', justify = 'center', font=('Helvetica', 32), textvariable=sv)
tEntry.grid(row = 2, column = 0, columnspan = 5, sticky = 'ew')

root.mainloop()