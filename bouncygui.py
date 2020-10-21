'''
program: bouncygui.py
author: ry 10/20/2020

GUI-based version of the bouncy.py app from ch3 
NOTES FROM OG PROGRAM:
program will calculate the total distance traveled by a bouning ball.
user will input:
	the starting height of the ball
	how bouncy the ball is
the output should be the total distance that the ball travels
'''

from breezypythongui import EasyFrame
from tkinter.font import Font

class Bouncy(EasyFrame):

	def __init__(self):
		#sets up the window and the widgets
		EasyFrame.__init__(self, title = 'Bouncy App', background = 'green')
		#create a var to store a Font obj
		myFont = Font(family = 'Courier New', size = 16, )

		#add label widgets
		self.addLabel(text = 'bouncy experiment', row = 0, column = 0, columnspan = 2, background = 'green', font = myFont)

		self.addLabel(text = 'Initial Height:', row = 1, column = 0, background = 'green')
		self.addLabel(text = 'Bounciness Index:', row = 2, column = 0, background = 'green')
		self.addLabel(text = 'No. of Bounces', row = 3, column = 0, background = 'green')
		self.addLabel(text = 'Total Distance', row = 5, column = 0, background = 'green')

		#add the entry fields
		self.height = self.addFloatField(value = 0.0, row = 1, column = 1)
		self.index = self.addFloatField(value = 0.0, row = 2, column = 1)
		self.bounces = self.addIntegerField(value = 0, row = 3, column = 1)
		self.distance = self.addFloatField(value = 0.0, row = 5, column = 1, precision = 2, state = 'readonly')
		
		#add command btn
		self.addButton(text = 'compute', row = 4, column = 0, columnspan = 2, command = self.bounce)
	
	#event handling method
	def bounce(self):
		#calculates total distance traveled given the inputs

		#input phase 
		ht = self.height.getNumber()
		ind = self.index.getNumber()
		bnce = self.bounces.getNumber()

		#accumulator var for the total distance traveled
		totalDistance = 0.0

		# for loop to determine the total distance traveled 
		for count in range(bnce):
			totalDistance += ht
			ht *= ind
			totalDistance += ht

		#output of the total distance 
		self.distance.setNumber(totalDistance)


#def of main() funct
def main():
	Bouncy().mainloop()

#global call to main()
main()
