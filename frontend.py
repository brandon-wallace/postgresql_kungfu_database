#!/usr/bin/env python3
"""

Classic Kung-Fu film database application using Tkinter and Postgresql.


"""


from tkinter import *
import backend



def get_selected_row(event):
    '''Get the row selected in the listbox window.'''
    global selected_tuple
    index = listbox1.curselection()[0]
    selected_tuple = listbox1.get(index)
    selected_tuple = selected_tuple.split(',')
    e1.delete(0, END)
    e1.insert(END, selected_tuple[1])
    e2.delete(0, END)
    e2.insert(END, selected_tuple[2])
    e3.delete(0, END)
    e3.insert(END, selected_tuple[3])
    e4.delete(0, END)
    e4.insert(END, selected_tuple[4])


def view_command():
    '''View entire database.'''
    listbox1.delete(0, END)
    listbox1.insert(END, ("{}, {}, {}, {}, {}".format("ID", "Title", "Alternate Title", "Length", "Year")))
    for row in backend.view_all():
        listbox1.insert(END, "{}, {}, {}, {}, {}".format(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4])))


def search_command():
    '''Run queries on the database.'''
    listbox1.delete(0, END)
    for row in backend.search(title.get(), alt_title.get(), duration.get(), year.get()):
        listbox1.insert(END, row)


def add_command():
    '''Add entries to the database.'''
    backend.insert(title_text.get(), alt_title_text.get(), duration_text.get(), year_text.get())
    listbox1.delete(0, END)
    listbox1.insert(END, (str(title_text.get()), str(alt_title_text.get()), duration_text.get(), year_text.get()))


def delete_command():
    '''Remove entries from the database.'''
    backend.delete(selected_tuple[0])


def update_command():
    '''Update the database.'''
    backend.update(selected_tuple[0], title_text.get(), alt_title_text.get(), duration_text.get(), year_text.get())


window = Tk()
window.wm_title("Classic Kung-Fu Film Database")
window.resizable(width=False, height=False)


Grid.rowconfigure(window, 0, weight=1)
Grid.columnconfigure(window, 0, weight=1)


l1 = Label(window, text="Title:")
l1.grid(row=0, column=0, sticky=W)

l2 = Label(window, text="Alt Title:")
l2.grid(row=0, column=2, sticky=W)

l3 = Label(window, text="Length:")
l3.grid(row=1, column=0, sticky=W)

l4 = Label(window, text="Year:")
l4.grid(row=1, column=2, sticky=W)

title_text = StringVar()
e1 = Entry(window, textvariable=title_text, width=20)
e1.grid(row=0, column=1, sticky=N+S+E+W)

alt_title_text = StringVar()
e2 = Entry(window, textvariable=alt_title_text, width=20)
e2.grid(row=0, column=3, sticky=N+S+E+W)

duration_text = StringVar()
e3 = Entry(window, textvariable=duration_text, width=20)
e3.grid(row=1, column=1, sticky=N+S+E+W)

year_text = StringVar()
e4 = Entry(window, textvariable=year_text, width=20)
e4.grid(row=1, column=3, sticky=N+S+E+W)

listbox1 = Listbox(window, height=20, width=50)
listbox1.grid(row=2, column=0, rowspan=9, columnspan=4, sticky=N+S+E+W)

scrollbar1 = Scrollbar(window)
scrollbar1.grid(row=2, rowspan=9, column=4, stick=N+S+E+W)

listbox1.configure(yscrollcommand=scrollbar1.set)
scrollbar1.configure(command=listbox1.yview)

listbox1.bind('<<ListboxSelect>>', get_selected_row)

b1 = Button(window, text="Search", width=15, command=search_command)
b1.grid(row=2, column=5)

b2 = Button(window, text="View All", width=15, command=view_command)
b2.grid(row=3, column=5)

b3 = Button(window, text="Add", width=15, command=add_command)
b3.grid(row=4, column=5)

b3 = Button(window, text="Update", width=15, command=update_command)
b3.grid(row=5, column=5)

b4 = Button(window, text="Delete", width=15, command=delete_command)
b4.grid(row=6, column=5)

b5 = Button(window, text="Close", width=15, command=window.destroy)
b5.grid(row=10, column=5)

window.mainloop()


