import tkinter as tk
from properties import Properties

class Search(Properties):
	def __init__(self, winHeight = 300, winWidth = 600):
		Properties.__init__(self)
		self.winHeight = winHeight
		self.winWidth = winWidth
		self.createSearchWindow()

	def createSearchWindow(self):
		self.window = tk.Tk()
		self.window.title("SEARCH")
		self.window.geometry(f"{self.winWidth}x{self.winHeight}")
		self.title = tk.Label(self.window, text="SEARCH FOR MEDICINE").place(relx = 0.5, rely = 0, x = 0, y = self.titleY, anchor = self.titleAnchor)
		self.label = tk.Label(self.window, text="ENTER THE NAME OF THE MEDICINE : ")
		self.label.place(relx = 0.5, rely=0, x = self.LabelStartX, y = self.startY, anchor = self.LabelAnchor)
		self.item = tk.Entry(self.window, width = self.EntryLength)
		self.item.place(relx = 0.5, rely=0, x = self.EntryStartX, y = self.startY, anchor = self.EntryAnchor)
		enter=tk.Button(self.window,text="ENTER",command=self.searchItem,width="10")
		enter.place(relx = 0.5,rely=0, x =0, y = self.startY + self.gap, anchor = self.enterButtonAnchor)

	def searchItem(self):
		self.nameOfMedicine = self.item.get()
		self.mycursor.execute(f"select * from {self.inventoryName} where NAME_OF_MEDICINE like '%{self.nameOfMedicine}%' limit 4")
		self.listOfMedicine = [i for i in self.mycursor]
		self.display()
		# print(self.listOfMedicine)

	def display(self):
		self.indentation = [-200, -140, 0, 60]
		self.heading = ["SLNO", "NAME_OF_MEDICINE", "PRICE", "QUANTITY"]
		for i, med in enumerate([self.heading] + self.listOfMedicine):
			for col in range(0,4):
				tk.Label(self.window, text=med[col]).place(relx = 0.5, rely=0, x = self.indentation[col], y = self.startY + (i+2)*self.gap, anchor = 'nw')

if __name__ == "__main__":
	help(tk.Label().place)