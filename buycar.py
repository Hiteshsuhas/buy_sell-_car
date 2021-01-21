from tkinter import *
import sqlite3
import tkinter.messagebox
from typing import List

conn = sqlite3.connect('sellcar.db')
c = conn.cursor()
ids = []


# tkinter windows6

class Application:
    new: List[int]

    def __init__(self, master):
        self.master = master

        # creating the frames in the master
        self.left = Frame(master, width=800, height=720, bg='white')
        self.left.pack(side=LEFT)

        self.right = Frame(master, width=600, height=720, bg='gold2')
        self.right.pack(side=RIGHT)
        # labels for the window
        self.heading2 = Label(self.left, text=".....................,______,", font=('arial 10 bold'), bg='white',
                              fg='steelblue')
        self.heading2.place(x=100, y=15)
        self.heading3 = Label(self.left, text="..........______/ _|__|__ _____", font=('arial 10 bold'), bg='white',
                              fg='steelblue')
        self.heading3.place(x=100, y=35)
        self.heading4 = Label(self.left, text="........|_________|__|________|", font=('arial 10 bold'), bg='white',
                              fg='steelblue')
        self.heading4.place(x=100, y=55)
        # self.heading6 = Label(self.left, text="..................o..........o", font=('arial 10 bold'), bg='white', fg='steelblue')
        # self.heading6.place(x=100, y=18)
        self.heading5 = Label(self.left,
                              text="-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------",
                              font=('arial 10 bold'), bg='white', fg='steelblue')
        self.heading5.place(x=0, y=0)
        self.heading = Label(self.left, text="Buy", font=('arial 40 bold'), bg='white', fg='steelblue')
        self.heading.place(x=400, y=15)
        self.heading = Label(self.left, text="car", font=('arial 40 italic'), bg='white', fg='gold2')
        self.heading.place(x=502, y=15)
        self.heading5 = Label(self.left,
                              text="-----------------------------------------o.............o---------------------------------------------------------------------------------------------------------------------------------------------------------",
                              font=('arial 10 bold'), bg='white', fg='steelblue')
        self.heading5.place(x=0, y=77)
        # button to perform a command
        self.submit = Button(self.left, text="1.Filter By Budget", width=20, height=5, fg='white', bg='steelblue',
                             command=self.see_car1)
        self.submit.place(x=400, y=180)
        self.submit = Button(self.left, text="2.Filter By Brand", width=20, height=5, fg='white', bg='steelblue',
                             command=self.see_car2)
        self.submit.place(x=400, y=260)
        self.submit = Button(self.left, text="3.Auto Search", width=20, height=5, fg='white', bg='steelblue',
                             command=self.see_car3)
        self.submit.place(x=400, y=340)
        self.submit = Button(self.left, text="4.Quit", width=20, height=5, fg='white', bg='steelblue',
                             command=self.see_car4)
        self.submit.place(x=400, y=420)
        self.heading5 = Label(self.left, text="Enter The ID", font=('arial 18 bold'), bg='white', fg='gold2')
        self.heading5.place(x=250, y=550)
        self.namenet = Entry(self.left, width=25, fg='steelblue', bg='white')
        self.namenet.place(x=450, y=550)
        self.submit = Button(self.left, text="Proceed", width=10, height=2, bg='white', fg='black',
                             command=self.see_car5)
        self.submit.place(x=420, y=600)
        # getting the number of car to view in the log
        sql2 = "SELECT ID FROM sellcar "
        self.result = c.execute(sql2)
        for self.row in self.result:
            self.id = self.row[0]
            ids.append(self.id)

        # ordering the ids
        self.new = sorted(ids)
        self.final_id = self.new[len(ids)-1]
        # displaying the logs in our right frame
        self.logs = Label(self.right, text="Cars Lists", font=('arial 28 italic'), fg='white', bg='steelblue')
        self.logs.place(x=0, y=0)

        self.box = Text(self.right, width=50, height=40)
        self.box.place(x=20, y=60)
        self.box.insert(END, "Total no of car in sell till now :  " + str(self.final_id))

    def see_car1(self):
        self.box1 = Text(self.right, width=50, height=40)
        self.box1.place(x=20, y=60)
        # getting the number of car to view in the log
        sql2 = "SELECT * FROM sellcar ORDER BY budget"
        self.result = c.execute(sql2)
        self.box1.insert(END, "Id : Owner_Name : Car_Company : Price(in rupee) : ")
        for self.row in self.result:
            self.id = self.row[0]
            self.own_nam = self.row[1]
            self.contact_no = self.row[2]
            self.brand = self.row[4]
            self.milage = self.row[5]
            self.budget = self.row[7]
            self.serviceno = self.row[8]
            self.carmodel = self.row[11]
            self.modelyear = self.row[10]
            self.box1.insert(END, str(self.id) + "       " + str(self.own_nam) + "         " + str(
                self.brand) + "            " + str(self.budget) + "       ")

        #    self.box1.insert(END, " Owner_Name : " + str(self.own_nam )+ " Phone_Number : " +str(self.contact_no)+" Car_Company : " +str(self.brand)+" Mileage : " +str(self.milage)+"Price(in rupee) : " +str(self.budget)+" No_Service : " +str(self.serviceno)+"Car_Type : " +str(self.carmodel)+"Year_Model : " +str(self.modelyear))

    def see_car2(self):
        self.box1 = Text(self.right, width=50, height=40)
        self.box1.place(x=20, y=60)
        # getting the number of car to view in the log
        sql2 = "SELECT * FROM sellcar ORDER BY brandid DESC"
        self.result = c.execute(sql2)
        self.box1.insert(END, "Id : Owner_Name : Car_Company : Price(in rupee) : ")
        for self.row in self.result:
            self.id = self.row[0]
            self.own_nam = self.row[1]
            self.contact_no = self.row[2]
            self.brand = self.row[4]
            self.milage = self.row[5]
            self.budget = self.row[7]
            self.serviceno = self.row[8]
            self.carmodel = self.row[3]
            self.modelyear = self.row[11]
            self.box1.insert(END, str(self.id) + "        " + str(self.own_nam) + "         " + str(
                self.brand) + "        " + str(self.budget) + "          ")

    def see_car3(self):
        # getting the user inputs
        self.box1 = Text(self.right, width=50, height=40)
        self.box1.place(x=20, y=60)
        # getting the number of car to view in the log
        sql2 = "SELECT * FROM sellcar ORDER BY brandid ,modelyear DESC, milage DESC,budget"
        self.result = c.execute(sql2)
        self.box1.insert(END, "Id : Owner_Name : Car_Company : Price(in rupee) : ")
        for self.row in self.result:
            self.id = self.row[0]
            self.own_nam = self.row[1]
            self.contact_no = self.row[2]
            self.brand = self.row[4]
            self.milage = self.row[5]
            self.budget = self.row[7]
            self.serviceno = self.row[8]
            self.carmodel = self.row[3]
            self.modelyear = self.row[11]
            self.box1.insert(END, str(self.id) + "       " + str(self.own_nam) + "           " + str(
                self.brand) + "          " + str(self.budget) + "       ")

    def see_car4(self):
        # getting the user inputs
        quit()

    def see_car5(self):
        self.input = self.namenet.get()
        sql = "SELECT * FROM sellcar WHERE id=?"
        self.res = c.execute(sql, (self.input,))
        for self.row in self.res:
            self.id = self.row[0]
            self.own_nam = self.row[1]
            self.contact_no = self.row[2]
            self.brand = self.row[4]
            self.milage = self.row[6]
            self.budget = self.row[7]
            self.serviceno = self.row[9]
            self.carmodel = self.row[3]
            self.modelyear = self.row[11]
            self.box1.insert(END, " Owner_Name : " + str(self.own_nam) + " Phone_Number : " + str(
                self.contact_no) + "Car_Company : " + str(self.brand) + " Mileage : " + str(
                self.milage) + "Price(in rupee) : " + str(self.budget) + " No_Service : " + str(
                self.serviceno) + "Car_Type : " + str(self.carmodel) + "Year_Model : " + str(self.modelyear))


# creating the object
root = Tk()
b = Application(root)
root.title("MY_DRIVE")
root.configure(bg="green")

# resolution of the window
root.geometry("1300x720+0+0")

# preventing the resize feature
root.resizable(True, True)

# end the loop
root.mainloop()


