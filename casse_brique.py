"""Copyright (c) 2014 Grimod Antoine
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
* Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
* Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Fichier principal du jeu du casse brique



"""
import sys

from objets import *
from fenetre import *
from initailisation import *



taille_l = 480

taille_h = 700

fenetre = fenetre(taille_l, taille_h, titre, logo)


def jeu(fenetre, save):

	jouer = True	
	
	taille_l = fenetre.get_width()
	taille_ h = fenetre.get_height()
	
	
	score = save["score"]
	niveau_actuel = save["niveau"]
	vies = save["vies"]

	jeu = False
	
	niveau = charger_niveau("niv/niveau" + str(niveau_actuel) + ".lvl")
	
	raquette = Raquette()
	balle = Balle(image, coordonnees, deplacement_balle)
	
	nb_frame = 0#permet de ne pas mettre l'affichage à jour à tous les tours de boucle
	
	power_up_en_chute = {}#contiendra les power_up en chute ainsi que leurs coordonnees NE GERE PAS LES DOUBLONS
	power_up_en_cours = {}#contiendra les power_up en cours de fonctionnement ainsi que leur temps restant
	
	while jouer:
	
		pygame.time.Clock.tick(60)#on limite la boucle à 60 tours par seconde
		
		for event in pygame.event.get():
		
			while not jeu and event.key != K_SPACE:
			
				if event.key == KSPACE:
				
					jeu = True				
					
			if event.type == QUIT:
				sys.exit(1)				
				
			if event.type == KEYDOWN:

				if event.key == K_LEFT:
					raquette.deplacer(-1)
					
				if event.key == K_RIGHT:
					raquette.deplacer(1)
					
				if event.key == K_ESCAPE:
					menu_options()
		
		
		niveau = is_collision(niveau, raquette, balle, power_up_en_cours)

		if nb_frame == 2:
			fenetre_update(fenetre, balle, raquette, niveau, scores, vies)
			nb_frame = 0