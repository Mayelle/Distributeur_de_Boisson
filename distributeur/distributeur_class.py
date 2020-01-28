class Boisson:
	"""docstring for Boisson"""

	#Constructeur paramétré	
	def __init__(self, nom="Evian", typeB="Eau minérale", prix=2):
		self.nom = nom
		self.typeB = typeB
		self.prix = prix
		
	def __str__(self):
		return "Nom : {} \nType : {} \nPrix : {}€".format(self.nom, self.typeB, self.prix) 

		
	
class Distributeur:

	"""docstring for Distributeur"""
	
	REPONSES = {
	"mauvaise_entree":"Désolé, je n'ai pas compris votre réponse. Merci de réessayer.",
	"bienvenue":"Bonjour ! Bienvenue au Distri'Boisson !",
	"liste_boissons": "Voulez-vous voir la liste des boissons ? (oui/non)",
	"au_revoir": "Merci de votre visite, à bientôt !",
	"commande_boisson": "Pour commander une boisson, entrez son numéro dans la console : ",
	"non_existante": "Cette boisson n'existe pas. Veuillez entrer un autre numéro. ",
	"rupture_stock": "Cette boisson n'est malheureusement plus en stock ! Veuillez en choisir une autre.",
	"confirmation_choix": "Êtes-vous sûr de vouloir commander la boisson {} (oui/ non)? ",
	"degustation": "Voici votre boisson. Bonne dégustation !",
	"nouvelle_commande": "Voulez-vous commander une autre boisson ? (oui / non)",
	"demande_paiement": "Veuillez entrez le montant de la pièce que vous souhaitez insérer dans la machine : ",
	"montant_du": "Vous devez payer encore {} €",
	"montant_non_accepte" : "Ce montant n'est pas accepté par la machine. Merci de recommencer",
	"montant_rendu": "La machine vous rend la monnaie : vous avez récupéré "

	}

	PIECES_ACCEPTEES = [2.0,1.0,0.5,0.2,0.1,0.05,0.02,0.01]




	#Constructeur 
	def __init__(self, *args):
		self.boissons = []
		for arg in args:
			self.boissons.append(arg)
		self.quantite = {}
		for boisson in self.boissons:
			self.quantite[boisson.nom] = 5 
		

	def __str__(self):
		phrase = ""
		i = 1
		for boisson in self.boissons:
			phrase+="\nBoisson n°{} :\n{} \nQuantité restante: {}\n\n".format(i,boisson,self.quantite[boisson.nom])
			i = i+1
		return phrase

	def _accueilUtilisateur(self):
		print(self.REPONSES["bienvenue"])
		self.__demande_affichage_boissons()


	def __demande_affichage_boissons(self):
		"""
		Ask first question...
		"""
		new_reponse_utilisateur = input(self.REPONSES["liste_boissons"]).lower().replace(" ", "")
		self.__affichage_boissons(new_reponse_utilisateur)

	def __affichage_boissons(self, new_reponse_utilisateur):

		while new_reponse_utilisateur != "oui" and new_reponse_utilisateur != "non":
			print(self.REPONSES["mauvaise_entree"])
			return self.__demande_affichage_boissons()

		if new_reponse_utilisateur == "oui":
			print(self.__str__())
			return self.__verif_choix_utilisateur()

		else:
			print(self.REPONSES["au_revoir"])

			

	def __verif_choix_utilisateur(self):
		try:
			new_reponse_utilisateur = int(input(self.REPONSES["commande_boisson"]).replace(" ", ""))

			try:
				if new_reponse_utilisateur > 0:
					boisson_commandee = self.boissons[new_reponse_utilisateur - 1]
					self.__verif_quantite_boisson_restante(boisson_commandee)
				else:
					print(self.REPONSES["non_existante"])
					self.__verif_choix_utilisateur()

			except Exception as e:
				print(self.REPONSES["non_existante"])
				self.__verif_choix_utilisateur()	
		

		except Exception as e:
			print(self.REPONSES["mauvaise_entree"])
			self.__verif_choix_utilisateur()



	def __verif_quantite_boisson_restante(self, boisson_commandee):
		if self.quantite[boisson_commandee.nom] > 0:
			self.__confirmation_utilisateur(boisson_commandee)
		else:
			print(self.REPONSES["rupture_stock"])
			return self.__verif_choix_utilisateur()

	
	def __confirmation_utilisateur(self, boisson_commandee):
		reponse_utilisateur = input(self.REPONSES["confirmation_choix"].format(boisson_commandee.nom))
		while reponse_utilisateur != "oui" and reponse_utilisateur != "non":
			print(self.REPONSES["mauvaise_entree"])
			self.__confirmation_utilisateur(boisson_commandee)
		if reponse_utilisateur.lower().replace(" ", "") == "oui":
			return self.__demande_paiement(boisson_commandee)
		else:
			self.__verif_choix_utilisateur()



	def __demande_paiement(self, boisson_commandee, montant_paye = 0):
		montant_du = boisson_commandee.prix - montant_paye

		try:
			reponse_utilisateur = float(input(self.REPONSES["demande_paiement"]).replace(" ", ""))

			if self.__verif_piece_inseree(reponse_utilisateur) == True:
				

				montant_paye += reponse_utilisateur
				montant_du -= reponse_utilisateur
				
			
				while montant_du > 0:
					print(self.REPONSES["montant_du"].format(round(montant_du,2)))
					return self.__demande_paiement(boisson_commandee, montant_paye)

				return self.__rendu_monnaie(boisson_commandee, montant_du)

			else:
				print(self.REPONSES["montant_non_accepte"])
				return self.__demande_paiement(boisson_commandee, montant_paye)

		except:
			print(self.REPONSES["mauvaise_entree"])
			return self.__demande_paiement(boisson_commandee, montant_paye)


	def __verif_piece_inseree(self, piece):
		for i in range(0,len(self.PIECES_ACCEPTEES)):
			if piece == self.PIECES_ACCEPTEES[i]:
				return True
		
		return False

	def __rendu_monnaie(self, boisson_commandee, montant_du):
		if montant_du == 0:
			return self.__commande_boisson(boisson_commandee)
		else:
			monnaie_rendue = []
			montant_rendu = abs(montant_du)
			detail_monnaie_rendue = self.REPONSES["montant_rendu"]

			step = 0
			while round(montant_rendu,2) != 0.00:
				for i, x in enumerate(self.PIECES_ACCEPTEES[step:]):
					
					if round(montant_rendu,2) - x < 0:
						continue
						
					if round(montant_rendu,2) - x > 0:
						monnaie_rendue.append(x)
						montant_rendu = round(montant_rendu,2) - x
						step = i
						break

					if round(montant_rendu,2) - x == 0:
						monnaie_rendue.append(x)
						montant_rendu = round(montant_rendu,2) - x
						
						break


			for i in self.PIECES_ACCEPTEES:
				if monnaie_rendue.count(i) > 0:
					detail_monnaie_rendue+="{} pièce(s) de {} €, ".format(monnaie_rendue.count(i),i)
				
			print(detail_monnaie_rendue)
			return self.__commande_boisson(boisson_commandee)

								
	
	def __commande_boisson(self, boisson_commandee):
		print(self.REPONSES["degustation"])
		self.quantite[boisson_commandee.nom] -= 1
		recommencer = input(self.REPONSES["nouvelle_commande"]).lower().replace(" ", "")
		while recommencer != "oui" and recommencer != "non":
			recommencer = input(self.REPONSES["mauvaise_entree"])
		if recommencer == "oui":
			self.__affichage_boissons(recommencer)
		else:
			print(self.REPONSES["au_revoir"])

