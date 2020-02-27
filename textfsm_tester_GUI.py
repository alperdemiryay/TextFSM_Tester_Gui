import textfsm, io
from tkinter import *
from tkinter import scrolledtext

def clicked():
    parsingResultBox.delete('1.0', END)
    targetOutputText = targetOutputBox.get("1.0", "end-1c")
    textFsmTemplateText = textFsmTemplateBox.get("1.0","end-1c")
    textFsmTemplateFile = io.StringIO(textFsmTemplateText)
    try:
        textFsmTemplateObj = textfsm.TextFSM(textFsmTemplateFile)
        parsing_result = textFsmTemplateObj.ParseText(targetOutputText)
        for i in reversed(parsing_result):
            parsingResultBox.insert(0.0, str(parsing_result.index(i) + 1) + ' ' + str(i) + '\n')
        parsinResultCountLabel.configure(text="Parcing Count is: {}".format(len(parsing_result)))
    except:
        parsingResultBox.delete('1.0', END)
        parsinResultCountLabel.configure(text="TextFSM Syntax Error!")

def onselect(evt):
    w = evt.widget
    try:
        selectedCountLabel.configure(text="Selected char count is: {}".format(str(len(w.get('sel.first', 'sel.last')))))
    except:
        selectedCountLabel.configure(text="Selected char count is: 0")

root=Tk()
root.title('TextFSM Tester')
root.geometry('1100x700')

targetOutputBox = scrolledtext.ScrolledText(root,width=134,height=19,undo=True)
targetOutputBox.grid(column=0, columnspan=2, row=0,sticky=W+E)
targetOutputBox.bind('<<Selection>>', onselect)

textFsmTemplateBox = scrolledtext.ScrolledText(root,width=66,height=19,undo=True)
textFsmTemplateBox.grid(column=0, row=3, sticky=W+E)
textFsmTemplateBox.bind('<<Selection>>', onselect)

parsingResultBox = scrolledtext.ScrolledText(root,width=66,height=19)
parsingResultBox.grid(column=1, row=3, sticky=W+E)
parsingResultBox.bind('<<Selection>>', onselect)

parsinResultCountLabel = Label(root, text="Parcing Count is: ")
parsinResultCountLabel.grid(column=1, row=1, sticky=W, padx=100)

selectedCountLabel = Label(root,text="Selected char count is: 0")
selectedCountLabel.grid(column=0, row=1)

buttonCommit=Button(root, height=1, width=10, text="Parse Output", command=clicked)
buttonCommit.grid(column=1, row=1, sticky=W)

mainloop()