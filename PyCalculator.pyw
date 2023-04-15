from tkinter import *
from tkinter import messagebox

def Add():
    try:
        text = input1.get()
        textInt = int(text)
        text1 = input2.get()
        text1Int = int(text1)
    except:
        messagebox.showinfo("PyCalculator", "Your input is not a number!")
        return
    input1.delete(0, 'end')
    input2.delete(0, 'end')
    result.delete(0, 'end')
    result.insert(0, textInt+text1Int)
    return

def Multiply():
    try:
        text = input1.get()
        textInt = int(text)
        text1 = input2.get()
        text1Int = int(text1)
    except:
        messagebox.showinfo("PyCalculator", "Your input is not a number!")
        return
    input1.delete(0, 'end')
    input2.delete(0, 'end')
    result.delete(0, 'end')
    result.insert(0, textInt*text1Int)
    return

def Subtract():
    try:
        text = input1.get()
        textInt = int(text)
        text1 = input2.get()
        text1Int = int(text1)
    except:
        messagebox.showinfo("PyCalculator", "Your input is not a number!")
        return
    input1.delete(0, 'end')
    input2.delete(0, 'end')
    result.delete(0, 'end')
    result.insert(0, textInt-text1Int)
    return

def Divide():
    try:
        text = input1.get()
        textInt = int(text)
        text1 = input2.get()
        text1Int = int(text1)
    except:
        messagebox.showinfo("PyCalculator", "Your input is not a number!")
        return
    input1.delete(0, 'end')
    input2.delete(0, 'end')
    result.delete(0, 'end')
    result.insert(0, textInt/text1Int)
    return

window = Tk()
window.title("PyCalculator")
window.geometry("300x300")

def Close():
    window.destroy()
    return

def Clear():
    input1.delete(0, 'end')
    input2.delete(0, 'end')
    result.delete(0, 'end')
    return

frame = Frame(window, relief="ridge", borderwidth=5)
frame.pack(fill="both", expand = 1)
number1 = Label(frame, text="Number 1:")
number1.place(x = 20, y = 30)
number2 = Label(frame, text="Number 2:")
number2.place(x = 170, y = 30)
input1 = Entry(frame, bd = 2, width = 10)
input1.place(x = 20, y = 70)
input2 = Entry(frame, bd = 2, width = 10)
input2.place(x = 170, y = 70)
button1 = Button(frame, text="+", command=Add)
button1.place(x = 5, y = 120)
button2 = Button(frame, text="*", command=Multiply)
button2.place(x = 25, y = 120)
button3 = Button(frame, text="-", command=Subtract)
button3.place(x = 45, y = 120)
button4 = Button(frame, text=":", command=Divide)
button4.place(x = 65, y = 120)
result1 = Label(frame, text="Result:")
result1.place(x = 50, y = 180)
result = Entry(frame, bd = 2, width = 10)
result.place(x = 120, y = 180)
button5 = Button(frame, text="Close", command=Close)
button5.place(x = 220, y = 260)
button6 = Button(frame, text="Clear", command=Clear)
button6.place(x = 180, y = 260)

Clear()

window.mainloop()
