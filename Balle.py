from Tkinter import *
import random

class Balle(object):
	def __init__(self, master):
		c_r= int(random.random()*256); c_g= int(random.random()*256); c_b= int(random.random()*256)
		c_r=("%02x"%random.randint(0,255))
		c_g=("%02x"%random.randint(0,255))
		c_b=("%02x"%random.randint(0,255))
		self.color= "#"+c_r+c_g+c_b
		r= 40
		self.rayon= r
		self.master= master
		

		self.speed= 1
		self.Ox= 0; self.Oy=0
		self.max_X= int( master.winfo_width()-r ); self.max_Y= int( master.winfo_height()-r )

		self.directionX= int(  (-1)**( int(random.random()*10) ) )
		self.directionY= int(  (-1)**( int(random.random()*10) ) )

		self.x= int(random.random()* self.max_X) + self.Ox; self.y= int(random.random()* self.max_Y) + self.Oy 
		bbox= (self.x, self.y, self.x+r, self.y+r)
		self.id= master.create_oval(*bbox, fill=self.color)

	def moveBalle(self):
		if self.directionX==1 and self.x >= self.max_X+self.Ox:
			self.directionX=-1
		if self.directionY==1 and self.y >= self.max_Y+self.Oy:
			self.directionY=-1
		if self.directionX==-1 and self.x <=self.Ox:
			self.directionX=1
		if self.directionY==-1 and self.y <= self.Oy:
			self.directionY=1

		dx= self.directionX*self.speed; dy= self.directionY*self.speed
		
		self.x+= dx; self.y+= dy
		self.master.move(self.id, dx, dy)

	def checkCollision(self, b):
		x1= self.x; y1= self.y
		x2= b.getPosX(); y2= b.getPosY();
		dx= abs( x1 - x2); dy= abs( y1-y2)
		dist= dx**2 + dy**2
		r= self.rayon/2 + b.getRayon()/2
		return dist <= r**2

	def setPosX(self, x):
		self.x= x
	def setPosY(self, y):
		self.y= y
	def getPosX(self):
		return self.x
	def getPosY(self):
		return self.y
	def getRayon(self):
		return self.rayon
	def getId(self):
		return self.id
	#def paintComponent(self):
		
# 		g.setColor(c);
