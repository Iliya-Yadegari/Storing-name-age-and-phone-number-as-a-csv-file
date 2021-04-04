import csv
from tkinter import *

def res_fun():
    
    fields = ['name','age','phone number']
    rows = [name_ent.get(),age_ent.get(),phone_ent.get()]
    
    with open('test.csv','w') as csvfile:
        csvwriter = csv.writer(csvfile)
        
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)

window = Tk()

window.title('Storage')


name_label = Label(window,text = 'Enter your name ===>').grid(row = 0, column = 0, padx = 10, pady = 10)
name_ent = Entry(window)
age_label = Label(window,text = 'Enter your age ===>').grid(row = 1, column = 0, padx = 10, pady = 10)
age_ent = Entry(window)
phone_label = Label(window,text = 'Enter your phone number ===>').grid(row = 2, column = 0, padx = 10, pady = 10)
phone_ent = Entry(window)
submit_btn = Button(window,text = 'Submit',width = 20,height = 3,command = res_fun).grid(row = 3, column = 0, padx = 10, pady = 10)

name_ent.grid(row = 0, column = 1, padx = 10, pady = 10)
age_ent.grid(row = 1, column = 1, padx = 10, pady = 10)
phone_ent.grid(row = 2, column = 1, padx = 10, pady = 10)


window.mainloop()