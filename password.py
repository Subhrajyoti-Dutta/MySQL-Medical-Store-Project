class Password(SuperWindow):
	def __init__(self, winHeight = 120, winWidth = 600):
		SuperWindow.__init__(self)
		self.winWidth = winWidth
		self.winHeight = winHeight
		self.createPasswordWindow()

	def createPasswordWindow(self):
		print(self.LabelStartX, self.EntryStartX)
		self.windows = tk.Tk()
		self.windows.title("Password")
		self.windows.geometry(f"{self.winWidth}x{self.winHeight}")

		self.pwdLabel = tk.Label(self.windows, text="ENTER THE PASSWORD : ")
		self.pwdLabel.place(relx = 0.5, rely=0, x = self.LabelStartX, y = self.winHeight//3,     anchor = "center")

		self.pwdEntry = tk.Entry(self.windows, width="35")
		self.pwdEntry.place(relx = 0.5, rely=0, x = 80,  y = self.winHeight//3,     anchor = "center")

		self.enter =    tk.Button(self.windows, text="ENTER", command = self.postPassword, width="10")
		self.enter.place(   relx = 0.5, rely=0, x = 0,    y = 2 * self.winHeight//3, anchor = "center" )

		self.windows.mainloop()

	def checkPwd(self, pwd, userId = "postgres", hostId = "localhost"):
		try:
			self.mydb=sql.connect(user=userId, host=hostId, password = pwd)
			self.userId = userId
			self.hostId = hostId
			self.pwd = pwd
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
			inventory.Inventory(self.pwd, self.userId, self.hostId, self.mydb)
