import tkinter as tk
# import tkinter.messagebox as tm
import psycopg2 as sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import insertion, search, delete, showall
from properties import Properties

class Inventory(Properties):
	def __init__(self, dbName = 'medishop', inventoryName = 'inventory', salesName = 'sales'):
		Properties.__init__(self)
		Properties.dbName = dbName
		Properties.inventoryName = inventoryName
		Properties.salesName = salesName
		Properties.mydb.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
		
		self.winHeight = 120
		self.winWidth = 800

		self.createMedishop()
		self.createInventory()
		self.createSales()
		self.createInventoryWindow()

	def createMedishop(self):
		try:
			Properties.mydb=sql.connect(database = self.dbName, user = self.userId, host = self.hostId, password = self.pwd)
		except:
			self.mycursor.execute(f"create database {self.dbName}")
			Properties.mydb=sql.connect(database = self.dbName, user = self.userId, host = self.hostId, password = self.pwd)
		self.mydb.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
		Properties.mycursor = self.mydb.cursor()

	def createInventory(self):
		try:
			self.mycursor.execute(f"create table {self.inventoryName} (SLNO integer, NAME_OF_MEDICINE varchar(100), PRICE integer, QUANTITY integer)")
		except sql.errors.DuplicateTable:
			pass					#If inventory table already exist then pass
	
	def createSales(self):
		try:
			self.mycursor.execute(f"create table {self.salesName} (NAME_OF_CUSTOMER varchar(100), PHONE integer, SLNO integer, NAME_OF_MEDICINE varchar(100),  QUANTITY integer, TIME VARCHAR(100))")
		except sql.errors.DuplicateTable:		
			pass					#If inventory table already exist then pass

	def createInventoryWindow(self):
		self.window=tk.Tk()
		self.window.title("INVENTORY")
		self.window.geometry(f"{self.winWidth}x{self.winHeight}")
		self.label=tk.Label(self.window,text="MEDICAL SHOP APPLICATION")
		self.label.place(relx = 0.5,rely=0, x = 0, y = self.titleY, anchor = 'n')   

		self.buttons = {"SEARCH": self.searchItem, "INSERT": self.insertItem, "DELETE": self.deleteItem, "SHOW ALL": self.showAllItem, "SALE": self.saleItem, "SHOW SALE": self.showSaleOfItems}
		start = 60
		gap = start * 2
		j = -3
		for i in self.buttons:
			tk.Button(self.window, text = i, command = self.buttons[i], width="10").place(relx = 0.5, rely = 0, x = start + gap * j, y = 60, anchor = 'n')
			j += 1

	def searchItem(self):
		search.Search()
		
	def insertItem(self):
		insertion.Insertion()
		
	def deleteItem(self):
		delete.Delete()

	def showAllItem(self):
		showall.ShowAll()

	def saleItem(self):
		pass
		
	def showSaleOfItems(self):
		pass

if __name__ == "__main__":
	pass