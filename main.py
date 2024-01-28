"""Create safe passowrords for your accounts"""
import random
from tkinter import *


window = Tk()
window.geometry('400x200')
window.title('Password generator')
window.resizable(False, False)
window.configure(bg='white')


#lists of letter, numbers and symbols that may be inlcuded in the passoword
Lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '1234567890'
special = '!?"=#)¤(%/&*-_.:,;@£{[]\`'

combined = Lowercase + uppercase + numbers + special + Lowercase + uppercase + numbers + special + Lowercase + uppercase + numbers + special + Lowercase + uppercase + numbers + special + Lowercase + uppercase + numbers + special + Lowercase + uppercase + numbers + special
max_Length = len(combined)  



label1 = Label(window, text = f'Enter desired password length, max = {max_Length}...')
label1.pack()

entry1 = Entry()
entry1.pack()

output_text = Text(window, height=5, width=40)

def makePassword():
    password_Length = entry1.get()
    try:
        password_Length = int(password_Length)
        if password_Length > max_Length:
            print(f'Your password cant be longer than {max_Length} characters')
        else:
            generated_Password = ''.join(random.sample(combined, password_Length))
            label2 = Label(window, text= 'This is your new password:')
            label2.pack()
            output_text.pack()
            output_text.delete(1.0, END)  # Clear previous content
            output_text.insert(END, f'{generated_Password}')
    except ValueError:
        print('Please enter a valid integer for password length.')



button1 = Button(window, text='Create passowrd', command = makePassword)
button1.pack()
window.mainloop()