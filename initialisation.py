"""Copyright (c) 2014 Grimod Antoine
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
* Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
* Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

import pickle


def charger_niveau(path):
	
	niveau = []
	
	with open(path, 'rb') as fichier:
		
		y = 0
		niveau.append([])
		
		for lignes in fichier:
			
			x = 0
			
			for briques in lignes:
			
				niveau[y][x].append(Brique(image_brique, (x * taille_brique, y * taille_brique)))
				x += 1
				
			y += 1	
			
		fichier.close()
		
		
		
def save(fichier, dico):

	with open(fichier,"wb") as fichier:
	
		enregistrer = pickle.Pickler(fichier)
		
		enregistrer.dump(dico)
		
		fichier.close()
		
		
		
		
def read_save(fichier):

	with open(fichier,"rb") as fichier:
	
		reader = pickle.Unpickler(fichier)
		
		save = reader.load()
		
		fichier.close()
		
	return save