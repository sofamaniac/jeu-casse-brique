"""Copyright (c) 2014 Grimod Antoine
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
* Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
* Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

import pygame

pygame.init()#initialisation de tous les modules pygame



def load_image(path):
	"""Fonction permettant de charger une image.
	
	Parametres nommes :
		-path : chemin absolu ou relatif de l'image a charger
	
	"""
	try:
		image = pygame.image.load(path).convert_alpha()
		
	except NameError as erreur_ouverture:
		print("Impossible de charger l'image : ", erreur_ouverture)
		
	return image

	


def load_sound(path):
	"""Fonction chargeant un son.
	
	Parametres nommes :
		-path : chemin absolu ou relatif du son a charger
	
	"""
	
	try:
		son = pygame.mixer.Sound(path)
		
	except NameError as erreur_ouverture:
		print("Impossible de charger le son : ", erreur_ouverture)
		
	return son

	
	
	
def load_music(path):
	"""Fonction chargant un son.
	
	Paramètre :
		-path : chemin d'accés à la music à charger
		
	"""
	
	try:
		music = pygame.mixer.music.load(path)
		
	except NameError as erreur_ouverture:
		print("Impossible de charger l'image : ", erreur_ouverture)
		
	
	

def afficher_text(fenetre, text, coordonnees, police="Arial", taille=40):
	"""Fonction permettant d'afficher du texte.
	
	Parametres nommes :
		-fentre : objet pygame.Surface ou sera afficher le texte
		-text : le texte a afficher
		-coordonnees : tuple contenant les coordonnees du texte a afficher
		-police : nom de la police a utiliser par defaut : Ariane
		-taille : taille du texte en pixel(px) par defaut : 40px
	
	"""

	font = pygame.font.SysFont(police, taille)

	rendu = font.render(text, True, (255, 255, 255))
	
	fenetre.blit(rendu, coordonnees)
	

	
def fenetre(taille_l, taille_h, titre, logo):
	"""Fonciton initialisant la fenetre.
	
	Parametres nommes :
			-taille_l : longueur en pixels de la fenetre
			-taille_h : hauteur en pixels de la fenetre
			-titre : nom de la fenetre
			-logo : chemin absolu ou relatif de l'image qui sert de logo
			
	"""
	fenetre = pygame.display.set_mode((taille_l, taille_h))
	
	pygame.display.set_caption(titre)
	pygame.display.set_icon(load_image(logo))
	
	pygame.display.flip()

	return fenetre
	
	
		
def fenetre_update(fenetre, balle, posistion_balle, raquette, position_raquette, niveau, taille_brique, score, vies):

	fenetre.blit(balle, position_balle)
	fenetre.blit(raquette, position_raquette)
	
	taille_l = fenetre.get_width()
	taille_h = fenetre.get_height()
	
	afficher_text(fenetre, "score " + str(score), taille_l - 19 * len(str(score))/2, 40)
	afficher_text(fenetre, "vies" + str(vies), 0, 40)#a remplacer par l'affichage de coeurs
	
	
	y = 0
	for lignes in niveau:
		x = 0
		for brique in lignes:
		
			if brique != 'v':
			
				position_brique = [x*taille_brique[0], y*taille_brique[1]]
				
				nom_brique = "img/brique" + brique + ".png"
				
				image_brique = load_image(nom_brique)
				
				fenetre.blit(image_brique, position_brique)
				
			x += 1	
		y += 1
		
	pygame.display.flip()	