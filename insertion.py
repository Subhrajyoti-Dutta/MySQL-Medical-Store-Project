import tkinter as tk
import tkinter.messagebox as tm
from properties import Properties

class Insertion(Properties):
	def __init__(self, winHeight = 300, winWidth = 600):
		Properties.__init__(self)
        # self.mydb = mydb
		# self.mycursor = mycursor
		self.winHeight = winHeight
		self.winWidth = winWidth
		self.createInsertWindow()

	def createInsertWindow(self):
		self.window=tk.Tk()
		self.window.title("INSERT DATA")
		self.window.geometry(f"{self.winWidth}x{self.winHeight}")
		tk.Label(self.window,text="INSERT NEW DATA").place(relx = 0.5, rely = 0, x = 0, y = self.titleY, anchor = self.titleAnchor)

		self.fields = {"SLNO": None, "NAME": None, "PRICE": None, "QUANTITY": None}

		self.gap = 40

		j = 0
		for i in self.fields:
			tk.Label(self.window, text = f"ENTER THE {i} OF THE MEDICINE : ").place(relx = 0.5, rely = 0, x = self.LabelStartX, y = self.startY + self.gap*j, anchor = self.LabelAnchor)
			self.fields[i] = tk.Entry(self.window, width = self.EntryLength)
			self.fields[i].place(relx = 0.5, rely = 0, x = self.EntryStartX, y = self.startY + self.gap*j, anchor = self.EntryAnchor)
			j += 1

		enter=tk.Button(self.window,text="ENTER",command=self.insertItem,width="10")
		enter.place(relx = 0.5,rely=0, x = 0, y = self.startY + self.gap*j, anchor = self.enterButtonAnchor)

	def insertItem(self):
		SLNO  = self.fields["SLNO"].get().upper()
		NAME  = self.fields["NAME"].get().upper()
		PRICE = self.fields["PRICE"].get().upper()
		QUA   = self.fields["QUANTITY"].get().upper()
		self.mycursor.execute("insert into inventory values ("+SLNO+",'"+NAME+"',"+PRICE+","+QUA+")")
		self.mydb.commit()
		tm.showinfo("Alert Message","Record Successfully Uploaded")
		pass


if __name__ == "__main__":
	help(tk.Entry)