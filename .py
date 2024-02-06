from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1530x700+0+0")

        self.Roll_No_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()
        self.text_Address = StringVar()

        self.search_by = StringVar()
        self.search_text = StringVar()

        title = Label(self.root, text="Student Management System", bd=10, relief=GROOVE,
                      font=("times new roman", 40, "bold"), bg="yellow", fg="red")
        title.pack(side=TOP, fill=X)

        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        Manage_Frame.place(x=20, y=100, width=400, height=580)

        m_title = Label(Manage_Frame, text="Manage Students", bg="crimson", fg="white",
                        font=("times new roman", 30, "bold"))
        m_title.grid(row=0, columnspan=2, pady=10)

        # Rest of your code for labels, text entries, buttons, and tables remains the same.
        lbl_roll = Label(Manage_Frame, text="Roll No", bg="crimson", fg="white",
                         font=("times new roman", 20, "bold"))
        lbl_roll.grid(row=1, column=0, pady=5, padx=20, sticky=W)
        text_roll = Entry(Manage_Frame, textvariable=self.Roll_No_var, font=("times new roman", 15, "bold"), bd=5,
                          relief=GROOVE)
        text_roll.grid(row=1, column=1, pady=5, padx=20, sticky=W)

        lbl_name = Label(Manage_Frame, text="Name", bg="crimson", fg="white",
                         font=("times new roman", 20, "bold"))
        lbl_name.grid(row=2, column=0, pady=5, padx=20, sticky=W)
        text_name = Entry(Manage_Frame, textvariable=self.name_var, font=("times new roman", 15, "bold"), bd=5,
                          relief=GROOVE)
        text_name.grid(row=2, column=1, pady=5, padx=20, sticky=W)

        lbl_Email = Label(Manage_Frame, text="Email", bg="crimson", fg="white",
                          font=("times new roman", 20, "bold"))
        lbl_Email.grid(row=3, column=0, pady=5, padx=20, sticky=W)
        text_Email = Entry(Manage_Frame, textvariable=self.email_var, font=("times new roman", 15, "bold"), bd=5,
                           relief=GROOVE)
        text_Email.grid(row=3, column=1, pady=5, padx=20, sticky=W)

        lbl_Gender = Label(Manage_Frame, text="Gender", bg="crimson", fg="white",
                           font=("times new roman", 20, "bold"))
        lbl_Gender.grid(row=4, column=0, pady=5, padx=20, sticky=W)
        combo_Gender = ttk.Combobox(Manage_Frame, textvariable=self.gender_var, font=("times new roman", 13, "bold"),
                                    state="readonly")
        combo_Gender['value'] = ("male", "female", "other")
        combo_Gender.grid(row=4, column=1, padx=20, pady=5)

        lbl_contact = Label(Manage_Frame, text="Contact", bg="crimson", fg="white",
                            font=("times new roman", 20, "bold"))
        lbl_contact.grid(row=5, column=0, pady=5, padx=20, sticky=W)
        text_contact = Entry(Manage_Frame, textvariable=self.contact_var, font=("times new roman", 15, "bold"), bd=5,
                             relief=GROOVE)
        text_contact.grid(row=5, column=1, pady=5, padx=20, sticky=W)

        lbl_Dob = Label(Manage_Frame, text="D.0.B", bg="crimson", fg="white",
                        font=("times new roman", 20, "bold"))
        lbl_Dob.grid(row=6, column=0, pady=5, padx=20, sticky=W)
        text_Dob = Entry(Manage_Frame, textvariable=self.dob_var, font=("times new roman", 15, "bold"), bd=5,
                         relief=GROOVE)
        text_Dob.grid(row=6, column=1, pady=5, padx=20, sticky=W)

        lbl_address = Label(Manage_Frame, text="Address", bg="crimson", fg="white",
                            font=("times new roman", 20, "bold"))
        lbl_address.grid(row=7, column=0, pady=5, padx=20, sticky=W)
        self.text_Address = Text(Manage_Frame, width=30, height=4, font=("", 10))
        self.text_Address.grid(row=7, column=1, pady=5, padx=20, sticky=W)

        # =========================button frame=======================
        btn_Frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg="crimson")
        btn_Frame.place(x=5, y=450, width=420)

        Addbtn = Button(btn_Frame, text="Add", width=10, command=self.add_students)
        Addbtn.grid(row=0, column=0, padx=10, pady=10)
        updatebtn = Button(btn_Frame, text="Update", width=10, command=self.update_data)
        updatebtn.grid(row=0, column=1, padx=10, pady=10)

        deletebtn = Button(btn_Frame, text="Delete", width=10, command=self.delete_data)
        deletebtn.grid(row=0, column=2, padx=10, pady=10)
        clearbtn = Button(btn_Frame, text="Clear", width=9, command=self.clear)
        clearbtn.grid(row=0, column=3, padx=10, pady=10)

        # =================Detail frame===============================

        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        Detail_Frame.place(x=450, y=100, width=800, height=580)

        lbl_search = Label(Detail_Frame, text="Search By", bg="crimson", fg="white",
                           font=("times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky=W)

        combo_search = ttk.Combobox(Detail_Frame, textvariable=self.search_by, width=15, font=("times new roman", 13, "bold"),
                                    state="readonly")
        combo_search['value'] = ("roll", "name", "contact")
        combo_search.grid(row=0, column=1, padx=20,        pady=10)

        text_search = Entry(Detail_Frame, textvariable=self.search_text, width=20, font=("times new roman", 10, "bold"), bd=5,
                            relief=GROOVE)
        text_search.grid(row=0, column=2, pady=10, padx=20, sticky=W)

        searchbtn = Button(Detail_Frame, text="Search", command=self.search_data, width=10, pady=5)
        searchbtn.grid(row=0, column=3, padx=7, pady=10)
        showallbtn = Button(Detail_Frame, text="Show All", command=self.fetch_data, width=10, pady=5)
        showallbtn.grid(row=0, column=4, padx=7, pady=10)
        # ===========Table frame======================================
        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="crimson")
        Table_Frame.place(x=10, y=70, width=760, height=450)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(Table_Frame,
                                          columns=("roll", "name", "email", "gender", "contact", "dob", "address"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("roll", text="Roll No.")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("gender", text="Gender.")
        self.student_table.heading("contact", text="Contact")
        self.student_table.heading("dob", text="D.O.B")
        self.student_table.heading("address", text="Address")

        self.student_table['show'] = 'headings'
        self.student_table.column("roll", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("contact", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("address", width=150)
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_students(self):
        if self.Roll_No_var.get() == "" or self.name_var.get() == "":
            messagebox.showerror("Error", "All fields are required!!")
        else:
            con = mysql.connector.connect(
                host="localhost",
                user="root",
                password="safiya@786",
                database="stm"
            )
            cur = con.cursor()
            cur.execute("INSERT INTO students (roll_no, name, email, gender, contact, dob, address) VALUES (%s, %s, %s, %s, %s, %s, %s)", (
                self.Roll_No_var.get(),
                self.name_var.get(),
                self.email_var.get(),
                self.gender_var.get(),
                self.contact_var.get(),
                self.dob_var.get(),
                self.text_Address.get("1.0", END)
            ))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success", "Record has been inserted")

    def fetch_data(self):
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="safiya@786",
            database="stm"
        )
        cur = con.cursor()
        cur.execute("SELECT * FROM students")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('', END, values=row)
        con.close()

    def clear(self):
        self.Roll_No_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.text_Address.delete("1.0", END)

    def get_cursor(self, ev):
        cursor_row = self.student_table.focus()
        contents = self.student_table.item(cursor_row)
        row = contents['values']
        self.Roll_No_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.text_Address.delete("1.0", END)
        self.text_Address.insert(END, row[6])

    def update_data(self):
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="safiya@786",
            database="stm"
        )
        cur = con.cursor()
        cur.execute("UPDATE students SET name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s WHERE roll_no=%s", (
            self.name_var.get(),
            self.email_var.get(),
            self.gender_var.get(),
            self.contact_var.get(),
            self.dob_var.get(),
            self.text_Address.get("1.0", END),
            self.Roll_No_var.get()
        ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def delete_data(self):
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="safiya@786",
            database="stm"
        )
        cur = con.cursor()
        cur.execute("DELETE FROM students WHERE roll_no=%s", (self.Roll_No_var.get(),))
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    def search_data(self):
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="safiya@786",
            database="stm"
        )
        cur = con.cursor()
        search = self.search_text.get()
        if self.search_by.get() == "roll":
            cur.execute("SELECT * FROM students WHERE roll_no LIKE %s", ('%' + search + '%',))
        elif self.search_by.get() == "name":
            cur.execute("SELECT * FROM students WHERE name LIKE %s", ('%' + search + '%',))
        elif self.search_by.get() == "contact":
            cur.execute("SELECT * FROM students WHERE contact LIKE %s", ('%' + search + '%',))

        rows = cur.fetchall()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('', END, values=row)
        con.close()

# The rest of your code should remain the same.

root = Tk()
ob = Student(root)
root.mainloop()