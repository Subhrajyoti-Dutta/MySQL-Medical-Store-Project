import psycopg2 as sql
import tkinter as tk
import tkinter.messagebox as tm
from tkinter import *
import datetime as dt
passwod=None

def search():
    def searching():
        liss3=[]                                #this will contain all the data
        liss4=[]                                #this will contain only the searched data
        mydb=sql.connect(user="root",host="localhost",passwd=passwod,database="medishop")
        mycursor=mydb.cursor()
        mycursor.execute("select * from  inventory")
        liss=[100,160,300,360]
        liss2=["SLNO","NAME_OF_MEDICINE","PRICE"," QUANTITY"]                                #it will show the heading
        for k in range(0,4):
            namelabel=tk.Label(window4,text=liss2[k]).place(relx = 0,rely=0, x =liss[k], y = 140, anchor = NW)
        for i in mycursor:
            liss3.append(list(i))                                #appending the datas
        NAME=str(name.get()).upper()
        for j in liss3:
            if j[1]==NAME:                                #appending the searched data 
                liss4.append(j)
        j=0
        for i in liss4:
            for k in range(0,4):
                namelabel=tk.Label(window4,text=i[k]).place(relx = 0,rely=0, x =liss[k], y = 170+j*30, anchor = NW)                                #this part is displaying the data
            j+=1
    window4=tk.Tk()
    window4.title("SEARCH")
    window4.geometry("600x300")
    label=tk.Label(window4,text="SEARCH FOR MEDICINE").place(relx = 0.5,rely=0, x =0, y = 20, anchor = N)
    name=tk.Entry(window4,width="40")
    namelabel=tk.Label(window4,text="ENTER THE NAME OF THE MEDICINE : ")
    namelabel.place(relx = 0,rely=0, x =20, y = 50, anchor = NW)
    name.place(relx = 0.5,rely=0, x =0, y = 50, anchor = NW)
    enter=tk.Button(window4,text="ENTER",command=searching,width="10")
    enter.place(relx = 0.5,rely=0, x =0, y = 120, anchor = S)

def insertion():                                #this will insert a record
    def insert():
        SLNO=str(slno.get()).upper()
        NAME=str(name.get()).upper()
        PRICE=str(price.get()).upper()
        QUA=str(qua.get()).upper()
        rock="insert into inventory values ("+SLNO+",'"+NAME+"',"+PRICE+","+QUA+")"
        mydb=sql.connect(user="root",host="localhost",passwd=passwod,database="medishop")
        mycursor=mydb.cursor()
        mycursor.execute(str(rock))
        mydb.commit()
        mydb.close()
        tm.showinfo("Alert Message","record successfully uploaded")
    window1=tk.Tk()
    window1.title("INSERT DATA")
    window1.geometry("600x300")
    label=tk.Label(window1,text="INSERT NEW DATA").place(relx = 0.5,rely=0, x =0, y = 20, anchor = N)
    slno=tk.Entry(window1,width="40")
    slnolabel=tk.Label(window1,text="ENTER THE SLNO OF THE MEDICINE : ")
    slnolabel.place(relx = 0,rely=0, x =20, y = 50, anchor = NW)
    slno.place(relx = 0.5,rely=0, x =0, y = 50, anchor = NW)
    name=tk.Entry(window1,width="40")
    namelabel=tk.Label(window1,text="ENTER THE NAME OF THE MEDICINE : ")
    namelabel.place(relx = 0,rely=0, x =20, y = 80, anchor = NW)
    name.place(relx = 0.5,rely=0, x =0, y = 80, anchor = NW)
    price=tk.Entry(window1,width="40")
    pricelabel=tk.Label(window1,text="ENTER THE PRICE OF THE MEDICINE : ")
    pricelabel.place(relx = 0,rely=0, x =20, y = 110, anchor = NW)
    price.place(relx = 0.5,rely=0, x =0, y = 110, anchor = NW)
    qua=tk.Entry(window1,width="40")
    qualabel=tk.Label(window1,text="ENTER THE QUANTITY OF THE MEDICINE : ")
    qualabel.place(relx = 0,rely=0, x =20, y = 140, anchor = NW)
    qua.place(relx = 0.5,rely=0, x =0, y = 140, anchor = NW)
    enter=tk.Button(window1,text="ENTER",command=insert,width="10")
    enter.place(relx = 0.5,rely=0, x =0, y = 200, anchor = S)

def deletion():                                #this will delete a record
    def delete():
        SLNO=str(slno.get())
        NAME=str(name.get())
        rock="delete from inventory where SLNO="+SLNO+" and NAME_OF_MEDICINE='"+NAME+"'"
        mydb=sql.connect(user="root",host="localhost",passwd=passwod,database="medishop")
        mycursor=mydb.cursor()
        mycursor.execute(str(rock))
        mydb.commit()
        mydb.close()
        tm.showinfo("Alert Message","Record Successfully Deleted")
    window2=tk.Tk()
    window2.title("DELETE DATA")
    window2.geometry("600x300")
    label=tk.Label(window2,text="SEARCH FOR MEDICINE").place(relx = 0.5,rely=0, x =0, y = 20, anchor = N)
    slno=tk.Entry(window2,width="40")
    slnolabel=tk.Label(window2,text="ENTER THE SLNO OF THE MEDICINE : ")
    slnolabel.place(relx = 0,rely=0, x =20, y = 50, anchor = NW)
    slno.place(relx = 0.5,rely=0, x =0, y = 50, anchor = NW)
    name=tk.Entry(window2,width="40")
    namelabel=tk.Label(window2,text="ENTER THE NAME OF THE MEDICINE : ")
    namelabel.place(relx = 0,rely=0, x =20, y = 80, anchor = NW)
    name.place(relx = 0.5,rely=0, x =0, y = 80, anchor = NW)
    enter=tk.Button(window2,text="ENTER",command=delete,width="10")
    enter.place(relx = 0.5,rely=0, x =0, y = 140, anchor = S)

def showall():
    def refresh():
        data()                                #the refresh function runs the function data
    def data():
        mydb=sql.connect(user="root",host="localhost",passwd=passwod,database="medishop")
        mycursor=mydb.cursor()
        mycursor.execute("select * from  inventory")
        j=0
        liss=[100,160,300,360]                                #contains the width of columns
        liss2=["                          ","     SLNO     ","     NAME_OF_MEDICINE     ","     PRICE     ","     QUANTITY     "]                                #contains the headings of columns
        for k in range(0,5):                                #print the heading
            namelabel=tk.Label(frame,text=liss2[k]).grid(row=1,column=k)
        for i in mycursor:
            for k in range(0,4):                                #print the data
                namelabel=tk.Label(frame,text=i[k]).grid(row=j+2,column=k+1)
            j+=1
        mydb.close()
        
    def myfunction(event):
        canvas.configure(scrollregion=canvas.bbox("all"),width=560,height=200)
    
    window2=tk.Tk()
    window2.title("ALL RECORD")
    window2.geometry("600x300")
    
    myframe=tk.Frame(window2,relief=GROOVE,width=100,height=100,bd=1)
    myframe.place(x=10,y=60)
    
    canvas=tk.Canvas(myframe)                                #following are the codes for the scrollbar which only work in canvas
    frame=tk.Frame(canvas)
    myscrollbar=tk.Scrollbar(myframe,orient="vertical",command=canvas.yview)
    canvas.configure(yscrollcommand=myscrollbar.set)
    
    myscrollbar.pack(side="right",fill="y")
    canvas.pack(side="left")
    canvas.create_window((0,0),window=frame,anchor='nw')
    label=tk.Label(window2,text="LIST OF ALL THE MEDICINE").place(relx = 0.5,rely=0, x =0, y = 20, anchor = N)
    frame.bind("<Configure>",myfunction)
    enter=tk.Button(window2,text="REFRESH",command=refresh,width="10")                                #this will refresh the window incase u update ur data live
    enter.place(relx = 1,rely=0, x =-10, y = 10, anchor = NE)
    data()
    window2.mainloop()

def sale():
    temp_record=[]
    liss3=[]
    liss4=[]
    def saling():                                #this function update the sale table and subtract the quantities from inventory
        for i in liss3:
            CUS=str(i[0]).upper()
            PH=str(i[1]).upper()
            SLNO=str(i[2]).upper()
            NAME=str(i[3]).upper()
            QUA=str(i[5]).upper()
            date=str(i[7]).upper()
            rock="insert into sale values ('"+CUS+"',"+PH+","+SLNO+",'"+NAME+"',"+QUA+",'"+date+"')"
            mydb=sql.connect(user="root",host="localhost",passwd=passwod,database="medishop")
            mycursor=mydb.cursor()
            mycursor.execute(str(rock))
            mydb.commit()
            rock2="update inventory set QUANTITY=QUANTITY-"+str(QUA)+" where SLNO="+SLNO+" and NAME_OF_MEDICINE='"+NAME+"'"
            mydb=sql.connect(user="root",host="localhost",passwd=passwod,database="medishop")
            mycursor=mydb.cursor()
            mycursor.execute(str(rock2))
            mydb.commit()
        tm.showinfo("Alert Message","Item(s) has been sold")
    def sale3():                                #this displays the medical slip
        window5=tk.Tk()
        window5.title("INVENTORY")
        window5.geometry("600x600")
        label=tk.Label(window5,text="""MEDICAL SHOP
        BILL SLIP""")
        label.place(relx = 0.5,rely=0, x =0, y = 0, anchor = N)
        label2=tk.Label(window5,text="NAME OF THE CUSTOMER : "+temp_record[0][0]).place(relx = 0,rely=0, x =100, y = 50, anchor = NW)                                #this two line will display the name and phno of the customer at the top
        label3=tk.Label(window5,text="PHNO OF THE CUSTOMER : "+temp_record[0][1]).place(relx = 0,rely=0, x =100, y = 80, anchor = NW)
        liss=[100,160,300,360,450]
        liss2=["SLNO","NAME_OF_MEDICINE","PRICE"," QUANTITY","TOTAL"]
        
        mydb=sql.connect(user="root",host="localhost",passwd=passwod,database="medishop")
        mycursor=mydb.cursor()
        mycursor.execute("select * from  inventory")
        for r in mycursor:
            liss4.append(list(r))
        for i in temp_record:
            lamp=i
            for p in liss4:
                if str(i[3])==str(p[1]) and str(i[2])==str(p[0]):                                #this line is searching for the data for the given input from saling from the inventory such as price
                    lamp.insert(-2,p[3])
                    lamp.insert(-1,(str(int(i[4])*int(i[5]))))
            liss3.append(lamp)                                #liss3 will be containing the contains to be displayed on the medical slip
        try:
            j=0
            for k in range(0,5):
                namelabel=tk.Label(window5,text=liss2[k]).place(relx = 0,rely=0, x =liss[k], y = 110, anchor = NW)
            for i in liss3:
                for k in range(2,7):
                    namelabel=tk.Label(window5,text=i[k]).place(relx = 0,rely=0, x =liss[k-2], y = 140+j*30, anchor = NW)
                j+=1
            namelabel=tk.Label(window5,text="AGGREGATE : ").place(relx = 0,rely=0, x =360, y = 140+j*30, anchor = NW)                                #this will contain the total price
            total=0
            for g in liss3:
                total+=int(g[6])
            namelabel=tk.Label(window5,text=total).place(relx = 0,rely=0, x =450, y = 140+j*30, anchor = NW)
            enter4=tk.Button(window5,text="ENTER",command=saling,width="10").place(relx = 0.5,rely=0, x =0, y = 200+j*30, anchor = N)
        except:                                #this for incase something went wrong
            window5.destroy()
            tm.showinfo("Alert Message","Something went wrong")
            
    def sale0():
        def sale5():                                #this will take u to the next window while appending the record to the temp_record
            sale2()
            sale3()
            window4.destroy()
        def sale2():                                #it serves the purpose of multiple medicine
            SLNO=str(slno.get()).upper()
            NAME=str(name.get()).upper()
            CUS=str(cus.get()).upper()
            QUA=str(qua.get())
            PH=str(ph.get())
            date=str(dt.datetime.now())
            temp_record2=[CUS,PH,SLNO,NAME,QUA,date]
            temp_record.append(temp_record2)                                #this will be containing the record of the sold item temporarily
            sale0()
        label=tk.Label(window4,text="DETAILS").place(relx = 0.5,rely=0, x =0, y = 20, anchor = N)
        slno=tk.Entry(window4,width="40")
        slnolabel=tk.Label(window4,text="ENTER THE SLNO OF THE MEDICINE : ")                                #contain the slno of the medicine
        slnolabel.place(relx = 0,rely=0, x =20, y = 110, anchor = NW)
        slno.place(relx = 0.5,rely=0, x =0, y = 110, anchor = NW)
        name=tk.Entry(window4,width="40")
        namelabel=tk.Label(window4,text="ENTER THE NAME OF THE MEDICINE : ")                                #contain the name of the medicine
        namelabel.place(relx = 0,rely=0, x =20, y = 140, anchor = NW)
        name.place(relx = 0.5,rely=0, x =0, y = 140, anchor = NW)
        qua=tk.Entry(window4,width="40")
        qualabel=tk.Label(window4,text="ENTER THE QUANTITY OF THE MEDICINE : ")                                #contain the number of the medicine
        qualabel.place(relx = 0,rely=0, x =20, y = 170, anchor = NW)
        qua.place(relx = 0.5,rely=0, x =0, y = 170, anchor = NW)
        enter=tk.Button(window4,text="ENTER",command=sale5,width="10")
        enter.place(relx = 0.5,rely=0, x =50, y = 230, anchor = S)
        next1=tk.Button(window4,text="NEXT",command=sale2,width="10")
        next1.place(relx = 0.5,rely=0, x =-50, y = 230, anchor = S)
    window4=tk.Tk()
    window4.title("SALE")
    window4.geometry("600x300")
    cus=tk.Entry(window4,width="40")
    cuslabel=tk.Label(window4,text="ENTER THE NAME OF THE CUSTOMER : ")                                #contains the name of customer
    cuslabel.place(relx = 0,rely=0, x =20, y = 50, anchor = NW)
    cus.place(relx = 0.5,rely=0, x =0, y = 50, anchor = NW)
    ph=tk.Entry(window4,width="40")
    phlabel=tk.Label(window4,text="ENTER THE PHONE NO. OF THE CUSTOMER : ")                                #contains the ph no of the customer
    phlabel.place(relx = 0,rely=0, x =20, y = 80, anchor = NW)
    ph.place(relx = 0.5,rely=0, x =0, y = 80, anchor = NW)
    sale0()

def showsale():                                #this show all the record of sale done
    def refresh():                                #refresh the window incase the data is changed live
        data()
    def data():
        mydb=sql.connect(user="root",host="localhost",passwd=passwod,database="medishop")
        mycursor=mydb.cursor()
        mycursor.execute("select * from  sale")
        j=0
        liss=[100,160,300,360]                                #width of column
        liss2=["NAME_OF_CUSTOMER","PHONE_NO.","SLNO","NAME_OF_MEDICINE","QUANTITY","TIME"]
        for k in range(0,6):
            namelabel=tk.Label(frame,text=liss2[k]).grid(row=1,column=k)
        for i in mycursor:
            for k in range(0,6):
                namelabel=tk.Label(frame,text=i[k]).grid(row=j+2,column=k)
            j+=1
        mydb.close()
        
    def myfunction(event):
        canvas.configure(scrollregion=canvas.bbox("all"),width=560,height=200)
    
    window2=tk.Tk()
    window2.geometry("600x300")
    
    myframe=tk.Frame(window2,relief=GROOVE,width=100,height=100,bd=1)
    myframe.place(x=10,y=60)
    
    canvas=tk.Canvas(myframe)                                #following are the codes for scrollbar and it only works in canvas
    frame=tk.Frame(canvas)
    myscrollbar=tk.Scrollbar(myframe,orient="vertical",command=canvas.yview)
    canvas.configure(yscrollcommand=myscrollbar.set)
    
    myscrollbar.pack(side="right",fill="y")
    canvas.pack(side="left")
    canvas.create_window((0,0),window=frame,anchor='nw')
    label=tk.Label(window2,text="LIST OF ALL THE SALES").place(relx = 0.5,rely=0, x =0, y = 20, anchor = N)
    frame.bind("<Configure>",myfunction)
    enter=tk.Button(window2,text="REFRESH",command=refresh,width="10")
    enter.place(relx = 1,rely=0, x =-10, y = 10, anchor = NE)
    data()
    window2.mainloop()

def passwod():
    global passwod
    passwod=passwd.get()                          #passwod contains the password for mysql
    try:                          #"try" because the next line shows error incase the password is wrong
        mydb=sql.connect(user="root",host="localhost",passwd=passwod)
        mycursor=mydb.cursor()
        window=tk.Tk()
        window.title("INVENTORY")
        window.geometry("600x120")
        label=tk.Label(window,text="MEDICAL SHOP APPLICATION").place(relx = 0.5,rely=0, x =0, y = 20, anchor = N)                          #relx and rely is the position for origin and x & y are the coordinate. anchor is the direction for direction of +ve axis   
        enter0=tk.Button(window,text="SEARCH",command=search,width="10").place(relx = 0.5,rely=0, x =-185, y = 60, anchor = NE)
        enter1=tk.Button(window,text="INSERT",command=insertion,width="10").place(relx = 0.5,rely=0, x =-95, y = 60, anchor = NE)
        enter3=tk.Button(window,text="DELETE",command=deletion,width="10").place(relx = 0.5,rely=0, x =-5, y = 60, anchor = NE)
        enter2=tk.Button(window,text="SHOW ALL",command=showall,width="10").place(relx = 0.5,rely=0, x =5, y = 60, anchor = NW)
        enter4=tk.Button(window,text="SALE",command=sale,width="10").place(relx = 0.5,rely=0, x =95, y = 60, anchor = NW)
        enter5=tk.Button(window,text="SHOW SALE",command=showsale,width="10").place(relx = 0.5,rely=0, x =185, y = 60, anchor = NW)
        windows.destroy()
        mydb=sql.connect(user="root",host="localhost",passwd=passwod)
        mycursor=mydb.cursor()
        mycursor.execute("show databases")
        t=0
        for i in mycursor:
            if i==('medishop',):                          #this is checking if the database named medishop exist or not
                t=1
        if t==0:                          # this line of codes are creating the database
            mydb=sql.connect(user="root",host="localhost",passwd=passwod)
            mycursor=mydb.cursor()
            mycursor.execute("create database medishop")
        
        rt=0
        mydb=sql.connect(user="root",host="localhost",passwd=passwod,database="medishop")
        mycursor=mydb.cursor()
        mycursor.execute("show tables")
        for i in mycursor:                                #this is checking if the table named inventory exist or not
            if i==('inventory',):
                rt=1
        if rt==0:                          # this line of codes are creating the table
            mydb=sql.connect(user="root",host="localhost",passwd=passwod,database="medishop")
            mycursor=mydb.cursor()
            mycursor.execute("create table inventory (SLNO int(10), NAME_OF_MEDICINE varchar(100), PRICE int(10), QUANTITY int(10))")
        
        mydb=sql.connect(user="root",host="localhost",passwd=passwod,database="medishop")
        mycursor=mydb.cursor()
        mycursor.execute("show tables")
        rtr=0
        for i in mycursor:                                #this is checking if the table named sale exist or not
            if i==('sale',):
                rtr=1
        if rtr==0:                           # this line of codes are creating the table
            mydb=sql.connect(user="root",host="localhost",passwd=passwod,database="medishop")
            mycursor=mydb.cursor()
            mycursor.execute("create table sale (NAME_OF_CUSTOMER varchar(100), PHONE int(10), SLNO int(10), NAME_OF_MEDICINE varchar(100),  QUANTITY int(10), TIME VARCHAR(100))")
    
    except:                                #this will show the message box of error incase the password is wrong
        tm.showinfo("Alert Message","Wrong Password")

windows=tk.Tk()
windows.title(" ")
windows.geometry("475x130")
passwd=tk.Entry(windows,width="40")
passwdlabel=tk.Label(windows,text="ENTER THE PASSWORD : ")
passwdlabel.place(relx = 0,rely=0, x =20, y = 30, anchor = NW)
passwd.place(relx = 0,rely=0, x =200, y = 30, anchor = NW)
enter=tk.Button(windows,text="ENTER",command=passwod,width="10")
enter.place(relx = 0.5,rely=0, x =0, y = 100, anchor = S)
windows.mainloop()

