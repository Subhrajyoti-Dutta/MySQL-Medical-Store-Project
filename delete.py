import tkinter as tk
import tkinter.messagebox as tm
from properties import Properties

class Delete(Properties):
	def __init__(self):
		Properties.__init__(self)
		self.createDeleteWindow()

	def createDeleteWindow(self):
		self.window = tk.Tk()
		self.window.title("DELETE DATA")
		self.window.geometry(f"{self.winWidth}x{self.winHeight}")
		tk.Label(self.window,text="SEARCH FOR MEDICINE").place(relx = 0.5, rely = 0, x = 0, y = self.titleY, anchor = self.titleAnchor)

		self.slnolabel = tk.Label(self.window,text="ENTER THE SLNO OF THE MEDICINE : ")
		self.slnolabel.place(relx = 0.5, rely=0, x = self.LabelStartX, y = self.startY, anchor = self.LabelAnchor)
		self.slno=tk.Entry(self.window,width=self.EntryLength)
		self.slno.place(relx = 0.5, rely=0, x = self.EntryStartX, y = self.startY, anchor = self.EntryAnchor)

		self.namelabel = tk.Label(self.window,text="ENTER THE NAME OF THE MEDICINE : ")
		self.namelabel.place(relx = 0.5,rely=0, x = self.LabelStartX, y = self.startY + self.gap, anchor = self.LabelAnchor)
		self.name=tk.Entry(self.window,width=self.EntryLength)
		self.name.place(relx = 0.5, rely=0, x = self.EntryStartX, y = self.startY + self.gap, anchor = self.EntryAnchor)

		tk.Button(self.window,text="ENTER",command=self.deleteItem,width="10").place(relx = 0.5,rely=0, x =0, y = self.startY + 2 * self.gap, anchor = self.enterButtonAnchor)

	def deleteItem(self):
		SLNO=self.slno.get()
		NAME=self.name.get()
		self.mycursor.execute(f"delete from inventory where SLNO = {SLNO} and NAME_OF_MEDICINE = '{NAME}'")
		self.mydb.commit()
		tm.showinfo("Alert Message","Record Successfully Deleted")