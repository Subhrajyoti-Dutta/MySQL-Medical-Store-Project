import psycopg2 as sql
import tkinter as tk
import tkinter.messagebox as tm
# from tkinter import *
# import datetime as dt
import inventory
from properties import Properties

class Password(Properties):
	def __init__(self):
		Properties.__init__(self)
		self.winHeight = 120
		self.createPasswordWindow()

	def createPasswordWindow(self):

		self.windows = tk.Tk()
		self.windows.title("Password")
		self.windows.geometry(f"{self.winWidth}x{self.winHeight}")

		self.pwdLabel = tk.Label(self.windows, text="ENTER THE PASSWORD : ")
		self.pwdLabel.place(relx = 0.5, rely=0, x = self.LabelStartX, y = self.winHeight//3, anchor = self.LabelAnchor)

		self.pwdEntry = tk.Entry(self.windows, width=self.EntryLength)
		self.pwdEntry.place(relx = 0.5, rely=0, x = self.EntryStartX, y = self.winHeight//3, anchor = self.EntryAnchor)

		self.enter = tk.Button(self.windows, text="ENTER", command = self.postPassword, width="10")
		self.enter.place(   relx = 0.5, rely=0, x = 0,    y = 2 * self.winHeight//3, anchor = "center" )

		self.windows.mainloop()

	def checkPwd(self, pwd, userId = "postgres", hostId = "localhost"):
		try:
			Properties.mydb=sql.connect(user=userId, host=hostId, password = pwd)
			Properties.userId = userId
			Properties.hostId = hostId
			Properties.pwd = pwd
			self.windows.destroy()
			return True
		except:
			self.wrgPwd()
			return False

	def wrgPwd():
		tm.showinfo("Alert Message","Wrong Password")

	def postPassword(self):
		validPwd = self.checkPwd(self.pwdEntry.get())
		if validPwd:
			inventory.Inventory()

if __name__ == "__main__":
	Password()