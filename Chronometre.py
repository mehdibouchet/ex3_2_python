import tkFont
from Tkinter import *
import Tkinter as tk
from threading import Thread, current_thread
import time

class Chronometre(Thread):
	def __init__(self, node, g, t, score):
		Thread.__init__(self)
		self.node= node
		self.t= 0
		self.state= False
		self.g= g
		self.daemon= True
		self.f1= tkFont.Font(family="Helvetica Neue",size=30,weight="normal")
		self.f2= tkFont.Font(family="Helvetica Neue",size=15,weight="normal")
		self.scoreText= Label(self.node,text="cc")
		self.timeText= Label(self.node, text="zef")
		
		self.scoreText.place(x=275, y=20)
		self.timeText.place(x=600, y=20)

	def paint(self):
		self.scoreText.configure(text="Score: "+str(self.g.getScore()))
		self.timeText.configure(text="Temps: "+str(self.t)+"s")

		self.scoreText.place(x=275, y=20)
		self.timeText.place(x=600, y=20)
	def run(self):
		i= 1
		while True:
			if self.g.getState():
				if(i == 0):
					self.t+= 1
				time.sleep(.01)
				i= (i+1)%99
				self.g.paint()
