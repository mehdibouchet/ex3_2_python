from Tkinter import *
import Tkinter as tk

from threading import Thread, Condition, current_thread
import Game

class UI_Thread(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.game= Game.Game(master)
		self.game.setupGame()

fen= Tk()
fen.title("Ma fenetre")
fen.resizable(False, False)
fen.geometry("800x800+200+0")

ui= UI_Thread(fen)

#ui.animate()
fen.mainloop()
