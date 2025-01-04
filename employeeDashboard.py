from tkinter import *
from tkinter import ttk

def employee_form(window):
    global back_image
    employee_frame = Frame(window, width=1070, height=570, bg='#BFD7ED')
    employee_frame.place(x=200, y=93)
    heading_label = Label(employee_frame, text='Manage Employee Details', font=('times new roman', 16, 'bold'), bg='#0074B7', fg='white')
    heading_label.place(x=0, y=0, relwidth=1)

    back_image = PhotoImage(file='icons/back.png')
    back_image = back_image.zoom(1).subsample(60)
    back_button = ttk.Button(employee_frame, image=back_image, style="TButton",
                         command=lambda: employee_frame.place_forget())
    back_button.place(x=10, y=30)

    top_frame = Frame(employee_frame, bg='#BFD7ED')
    top_frame.place(x=0, y=60, relwidth=1, height=235)

    search_frame = Frame(top_frame, bg='#BFD7ED')
    search_frame.pack()
    search_combobox= ttk.Combobox(search_frame, values=('Id', 'Name', 'Email'), font=('times new roman', 12), state='readonly')
    search_combobox.set('Search By')
    search_combobox.grid(column=0, row=0, padx=20)

    search_entry = Entry(search_frame, font=('times new roman', 12), bg='white', fg='black')
    search_entry.grid(column=1, row=0, padx=20)

    search_button = ttk.Button(search_frame, text='SEARCH', style='TButton')
    search_button.grid(column=2, row=0, padx=20)

    show_button = ttk.Button(search_frame, text='SHOW ALL', style='TButton')
    show_button.grid(column=3, row=0, padx=20)

    employee_treeview = ttk.Treeview(top_frame, columns=('empid', 'name', 'email'), show='headings')
    employee_treeview.pack(pady=10)

    employee_treeview.heading('empid', text='EmpId')
    employee_treeview.heading('name', text='Name')
    employee_treeview.heading('email', text='Email' )




