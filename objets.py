"""Copyright (c) 2014 Grimod Antoine
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
* Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
* Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

from fenetre import *

from pygame.locals import *

class Raquette:

	def __init__(self, image,coordonnees, deplacement=8):
	
		self.image = image
		self.position = coordonnees
		self.deplacement = deplacement
	
	
	def deplacer(self, taille_l, event):

		if event.key == K_LEFT:
		
			if self.position[0] - deplacement <= 0:
			
				self.position[0] = self.position[0] - deplacement
				
				
		if event.key == K_RIGHT:

			if self.position[0] + deplacement <= taille_l:
			
				self.position[0] = self.position[0] + deplacement
				

class Balle:

		def __init__(self, image, coordonnees, deplacement=[8,8]):
		
			self.image = image
			self.position = coordonnees
			self.deplacement = deplacement
			
		def deplacer(self, taille_l, taill_h)

			if self.position[0] + self.deplacement[0] <= 0 or self.position[0] + self.deplacement[0] >= taille_l:
				deplacement[0] = -deplacement[0]
				
			if self.positon[1] + self.deplacement[1] <= 0:
				self.deplacement[1] = -self.deplacement[1]
				

class Brique:
	
	def __init__(self, image, coordonnees):
	
		self.image = image
		self.position = coordonnees
		self.power_up = Power_up()

				
def charger_niveau(path):
	
	niveau = [[]]
	
	with open(path, 'r') as fichier:
	
		for lignes in fihcier:
			
			for briques in lignes: