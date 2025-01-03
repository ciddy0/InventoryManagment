from tkinter import *

window = Tk()

# gui settings
window.title('Dashboard')
window.geometry('1270x668+0+0')
window.resizable(0,0)
window.config(bg='white')

# inventory image and resizing
bg_image = PhotoImage(file='icons/inventory.png')
bg_image = bg_image.zoom(5)
bg_image = bg_image.subsample(32)

# Inventory Title
titleLabel = Label(window,image=bg_image,compound=LEFT, text='  Inventory Management System', font=('times new roman', 40, 'bold'), bg='#010c48', fg='white', anchor='w', padx=20)
titleLabel.place(x=0,y=0, relwidth=1)

# Logout button
logoutButton = Button(window, text="Logout", font=('times new roman', 20, 'bold'), fg='#010c48')
logoutButton.place(x=1110, y=10)

# system details
subtitleLabel = Label(window, text='Welcome Admin\t\t Date: 01-02-2025\t\t Time: 12:21:00 am', font=('times new roman', 15), bg='#4d636d', fg='white')
subtitleLabel.place(x=0, y=70, relwidth=1)

leftFrame = Frame(window)
leftFrame.place(x=0, y=102, width=200, height=555)
logoImage = PhotoImage(file='icons/checklist.png')
logoImage = logoImage.zoom(19).subsample(32)
imageLabel = Label(leftFrame, image=logoImage)
imageLabel.pack(fill=X)

menuLabel = Label(leftFrame, text='Menu', font=('times new roman', 20), bg='#009688')
menuLabel.pack(fill=X)

employee_icon = PhotoImage(file='icons/employee.png')
employee_icon = employee_icon.zoom(4).subsample(32)
employee_button = Button(leftFrame, image=employee_icon, compound=LEFT, text="Employee", font=('times new roman', 20, 'bold'), padx=20)
employee_button.pack(fill=X)

supplier_icon = PhotoImage(file='icons/supplier.png')
supplier_icon = supplier_icon.zoom(5).subsample(32)
supplier_button = Button(leftFrame, image=supplier_icon, compound=LEFT, text="Supplier", font=('times new roman', 20, 'bold'), padx=20)
supplier_button.pack(fill=X)

category_icon = PhotoImage(file='icons/category.png')
category_icon = category_icon.zoom(5).subsample(32)
category_button = Button(leftFrame, image=category_icon, compound=LEFT, text="Category", font=('times new roman', 20, 'bold'), padx=20)
category_button.pack(fill=X)

product_icon = PhotoImage(file='icons/product.png')
product_icon = product_icon.zoom(3).subsample(32)
product_button = Button(leftFrame, image=product_icon, compound=LEFT, text="Product", font=('times new roman', 20, 'bold'), padx=20)
product_button.pack(fill=X)

sales_icon = PhotoImage(file='icons/sales.png')
sales_icon = sales_icon.zoom(3).subsample(32)
sales_button = Button(leftFrame, image=sales_icon, compound=LEFT, text="Sales", font=('times new roman', 20, 'bold'), padx=20)
sales_button.pack(fill=X)

exit_icon = PhotoImage(file='icons/exit.png')
exit_icon = exit_icon.zoom(1).subsample(25)
exit_button = Button(leftFrame, image=exit_icon, compound=LEFT, text="Exit", font=('times new roman', 20, 'bold'), padx=20)
exit_button.pack(fill=X)

window.mainloop()
