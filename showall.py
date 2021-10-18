import tkinter as tk
import tkinter.messagebox as tm
from properties import Properties

class ShowAll(Properties):
	def __init__(self):
		Properties.__init__(self)
		self.createShowAllWindow()

	def createShowAllWindow(self):
		self.window = tk.Tk()
		self.window.title("ALL RECORD")
		self.window.geometry(f"{self.winWidth}x{self.winHeight}")

		self.title = tk.Label(self.window, text = "LIST OF ALL THE MEDICINE").place(relx = 0.5,rely=0, x = 0, y = self.titleY, anchor = self.titleAnchor)

		self.myframe=tk.Frame(self.window, relief = "groove", width=100, height=100)
		self.myframe.place(relx = 0.5, rely = 0, x=0, y=self.startY, anchor = 'n')

		self.canvas=tk.Canvas(self.myframe)#.window, relief = "groove", width=100, height=100)								#following are the codes for the scrollbar which only work in canvas
		self.frame=tk.Frame(self.canvas)
		self.myscrollbar=tk.Scrollbar(self.myframe,orient="vertical",command=self.canvas.yview)
		self.canvas.configure(yscrollcommand=self.myscrollbar.set)
		self.myscrollbar.pack(side="right",fill="y")

		self.canvas.pack(side="left")
		self.canvas.create_window((0,0),window=self.frame,anchor='nw')
		self.frame.bind("<Configure>", self.myfunction)
		# refresh=tk.Button(self.window,text="REFRESH",command=self.refresh,width="10")								#this will refresh the window incase u update ur data live
		# refresh.place(relx = 1,rely=0, x =-10, y = 10, anchor = 'ne')
		self.data()
		# self.window.mainloop()

	def myfunction(self,event):
		self.canvas.configure(scrollregion=self.canvas.bbox("all"),width=560,height=200)

	def refresh(self):
		self.data()

	def data(self):
		self.mycursor.execute("select * from  inventory")
		j=0
		liss=[100,160,300,360]								#contains the width of columns
		liss2=["						  ","	 SLNO	 ","	 NAME_OF_MEDICINE	 ","	 PRICE	 ","	 QUANTITY	 "]								#contains the headings of columns
		for k in range(0,5):								#print the heading
			namelabel=tk.Label(self.frame,text=liss2[k]).grid(row=1,column=k)
		for i in self.mycursor:
			for k in range(0,4):								#print the data
				namelabel=tk.Label(self.frame,text=i[k]).grid(row=j+2,column=k+1)
			j+=1

if __name__ == "__main__":
	help(tk.Frame().place)