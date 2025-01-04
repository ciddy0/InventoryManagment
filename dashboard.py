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

# left menu
leftFrame = Frame(window, bg='#D3D3D3')
leftFrame.place(x=0, y=102, width=200, height=555)
logoImage = PhotoImage(file='icons/checklist.png')
logoImage = logoImage.zoom(19).subsample(32)
imageLabel = Label(leftFrame, image=logoImage, bg= '#D3D3D3')
imageLabel.pack(fill=X)

menuLabel = Label(leftFrame, text='Menu', font=('times new roman', 20), bg='#009688')
menuLabel.pack(fill=X)

# employee button
employee_icon = PhotoImage(file='icons/employee.png')
employee_icon = employee_icon.zoom(5).subsample(32)
employee_button = Button(leftFrame, image=employee_icon, compound=LEFT, text="Employee", font=('times new roman', 20, 'bold'), padx=20)
employee_button.pack(fill=X)

# supplier button
supplier_icon = PhotoImage(file='icons/supplier.png')
supplier_icon = supplier_icon.zoom(6).subsample(32)
supplier_button = Button(leftFrame, image=supplier_icon, compound=LEFT, text="Supplier", font=('times new roman', 20, 'bold'), padx=20)
supplier_button.pack(fill=X)

# category button
category_icon = PhotoImage(file='icons/category.png')
category_icon = category_icon.zoom(6).subsample(32)
category_button = Button(leftFrame, image=category_icon, compound=LEFT, text="Category", font=('times new roman', 20, 'bold'), padx=20)
category_button.pack(fill=X)

# product button
product_icon = PhotoImage(file='icons/product.png')
product_icon = product_icon.zoom(4).subsample(32)
product_button = Button(leftFrame, image=product_icon, compound=LEFT, text="Product", font=('times new roman', 20, 'bold'), padx=20)
product_button.pack(fill=X)

# sales button
sales_icon = PhotoImage(file='icons/sales.png')
sales_icon = sales_icon.zoom(4).subsample(32)
sales_button = Button(leftFrame, image=sales_icon, compound=LEFT, text="Sales", font=('times new roman', 20, 'bold'), padx=20)
sales_button.pack(fill=X)

# exit button
exit_icon = PhotoImage(file='icons/exit.png')
exit_icon = exit_icon.zoom(2).subsample(25)
exit_button = Button(leftFrame, image=exit_icon, compound=LEFT, text="Exit", font=('times new roman', 20, 'bold'), padx=20)
exit_button.pack(fill=X)

# total employees frame
emp_frame = Frame(window, bg='#4d636d', bd=3, relief=GROOVE)
emp_frame.place(x=400, y=125, height=170, width=280)
total_emp_icon = PhotoImage(file='icons/employee_count.png')
total_emp_icon = total_emp_icon.zoom(10).subsample(32)
total_emp_icon_label = Label(emp_frame, image=total_emp_icon, bg='#4d636d')
total_emp_icon_label.pack()
total_emp_label = Label(emp_frame, text='Total Employees', bg='#4d636d', fg='white', font=('times new romans', 15))
total_emp_label.pack()
total_emp_count_label = Label(emp_frame, text='0', bg='#4d636d', fg='white', font=('times new romans', 20))
total_emp_count_label.pack()

# total suppliers frame
supp_frame = Frame(window, bg='#4d636d', bd=3, relief=GROOVE)
supp_frame.place(x=800, y=125, height=170, width=280)
total_supp_icon = PhotoImage(file='icons/truck_count.png')
total_supp_icon = total_supp_icon.zoom(4).subsample(32)
total_supp_icon_label = Label(supp_frame, image=total_supp_icon, bg='#4d636d')
total_supp_icon_label.pack()
total_supp_label = Label(supp_frame, text='Total Suppliers', bg='#4d636d', fg='white', font=('times new romans', 15))
total_supp_label.pack()
total_supp_count_label = Label(supp_frame, text='0', bg='#4d636d', fg='white', font=('times new romans', 20))
total_supp_count_label.pack()

# total categories frame
cat_frame = Frame(window, bg='#4d636d', bd=3, relief=GROOVE)
cat_frame.place(x=400, y=310, height=170, width=280)
total_cat_icon = PhotoImage(file='icons/category_count.png')
total_cat_icon = total_cat_icon.zoom(4).subsample(32)
total_cat_icon_label = Label(cat_frame, image=total_cat_icon, bg='#4d636d')
total_cat_icon_label.pack()
total_cat_label = Label(cat_frame, text='Total Categories', bg='#4d636d', fg='white', font=('times new romans', 15))
total_cat_label.pack()
total_cat_count_label = Label(cat_frame, text='0', bg='#4d636d', fg='white', font=('times new romans', 20))
total_cat_count_label.pack()

# total products frame
prod_frame = Frame(window, bg='#4d636d', bd=3, relief=GROOVE)
prod_frame.place(x=800, y=310, height=170, width=280)
total_prod_icon = PhotoImage(file='icons/product_count.png')
total_prod_icon = total_prod_icon.zoom(4).subsample(32)
total_prod_icon_label = Label(prod_frame, image=total_prod_icon, bg='#4d636d')
total_prod_icon_label.pack()
total_prod_label = Label(prod_frame, text='Total Products', bg='#4d636d', fg='white', font=('times new romans', 15))
total_prod_label.pack()
total_prod_count_label = Label(prod_frame, text='0', bg='#4d636d', fg='white', font=('times new romans', 20))
total_prod_count_label.pack()

# total sales frame
sal_frame = Frame(window, bg='#4d636d', bd=3, relief=GROOVE)
sal_frame.place(x=600, y=495, height=170, width=280)
total_sal_icon = PhotoImage(file='icons/sales_count.png')
total_sal_icon = total_sal_icon.zoom(4).subsample(32)
total_sal_icon_label = Label(sal_frame, image=total_sal_icon, bg='#4d636d')
total_sal_icon_label.pack()
total_sal_label = Label(sal_frame, text='Total Sales', bg='#4d636d', fg='white', font=('times new romans', 15))
total_sal_label.pack()
total_sal_count_label = Label(sal_frame, text='0', bg='#4d636d', fg='white', font=('times new romans', 20))
total_sal_count_label.pack()

window.mainloop()
