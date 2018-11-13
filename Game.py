#PanedWindow(master=None, **options)  orient=VERTICAL width height
import Chronometre
import Balle
from Tkinter import *
import Tkinter as tk
import random
from threading import Thread, Condition, current_thread

class Game(PanedWindow):
	def __init__(self, parentNode=None, **kwargs):
		PanedWindow.__init__(self, orient=VERTICAL, width= 800, height= 800, **kwargs)
		self.root= parentNode
		self.pack();	self.update()
		width= self.winfo_height()
		self.cond= Condition()
		self.timer= Chronometre.Chronometre(parentNode, self, 0, 0)
		self.score= 0
		self.b= []
		self.MAX_BALLE= 10
		self.timerContainer= Frame(self, relief=GROOVE, bg="gray");	self.timerContainer.pack()
		self.gameContainer= Canvas(self, relief=GROOVE, bg="white", height=700);self.gameContainer.pack()
		self.addBallFlag= False; self.delBallFlag= False
		self.div_btns= Frame(self, relief=GROOVE); self.div_btns.pack()
		btns= Frame(self.div_btns); btns.place(in_=self.div_btns, anchor="c", relx=.5, rely=.5)

		self.stop_b= Button(btns, text="START", command=self.changeState, width=5)				;self.stop_b.pack(side=LEFT, padx=10)
		self.plus_b= Button(btns, text="+", command=self.setAddBallFlag, state=DISABLED, width=5)		;self.plus_b.pack(side=LEFT, padx=10)
		self.moins_b=Button(btns, text="-", command=self.setRemoveBallFlag, state=DISABLED, width=5)	;self.moins_b.pack(side=LEFT, padx=10)
		
		self.add(self.timerContainer, height=50)
		self.add(self.gameContainer, height=700)
		self.add(self.div_btns, height=50)

		self.pack(fill="both")

	def setupGame(self):
		self.state= True
		self.gameContainer.update()
		self.gameWidth= self.gameContainer.winfo_width()
		self.gameHeight= self.gameContainer.winfo_height()

		#self.addBalle()
		self.timer.start()

		self.plus_b['state']= 'normal'
		self.moins_b['state']= 'disabled'
		self.stop_b['text']= 'STOP'

	def stop(self):
		with self.cond:
			while not self.state:
				self.cond.wait()
			self.state= False
			self.plus_b['state']= 'disabled'
			self.moins_b['state']= 'disabled'
			self.stop_b['text']= 'START'
			self.cond.notifyAll()

	def start(self):
		cond= Condition()
		with self.cond:
			while self.state:
				self.cond.wait()
			self.state= True
			self.plus_b['state']= 'active'
			self.moins_b['state']= 'active'
			self.stop_b['text']= 'STOP'
			self.cond.notifyAll()
	
	def addBall(self):
		b_size= len(self.b)
		if b_size < self.MAX_BALLE:
			balle= Balle.Balle(self.gameContainer)
			self.b.append(balle)
		if b_size == 1:
			self.moins_b['state']= 'active'
		if b_size == self.MAX_BALLE-1:
			self.plus_b['state']= 'disabled'

	def removeBalle(self, b1):
		self.b.remove(b1)
		self.gameContainer.delete(b1.getId())

		b_size= len(self.b)

		if b_size == 0:
			self.moins_b['state']= 'disabled'
		if b_size < self.MAX_BALLE-1:
			self.plus_b['state']= 'active'	
	def removeBalleAlea(self):
		i= int( random.random()*len(self.b) )
		self.removeBalle(self.b[i])
	def moveBalles(self):
		for i in range(0, len(self.b)):
			self.b[i].moveBalle()
	def drawBalles(self):
		for i in range(0, len(self.b)):
			self.b[i].paintComponent()

	def checkCollision(self):
		b_size= len(self.b)
		colisions=[]
		for i in range(0, b_size):
			for j in range(i+1, b_size):
				b1= self.b[i]
				b2= self.b[j]
				if b1.checkCollision(b2):
					colisions+= list(set(colisions) | set([b1, b2]))
					self.score+= 1
	
		for b in colisions:
			self.removeBalle(b);
	def getState(self):
		return self.state
	def getScore(self):
		return self.score
	def getGameWidth(self):
		return self.gameWidth
	def getGameHeight(self):
		return self.gameHeight

	def paint(self):
		self.moveBalles()
		self.checkCollision()
		self.timer.paint()
		if( self.addBallFlag ):
			self.addBall(); 		self.addBallFlag= False
		if( self.delBallFlag ): 		
			self.removeBalleAlea();	self.delBallFlag= False

	def setAddBallFlag(self):
		self.addBallFlag= True
	def setRemoveBallFlag(self):
		self.delBallFlag= True
	def changeState(self):
		if not self.state:
			self.start()
		else:
			self.stop()