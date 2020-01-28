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
	"nouvelle_commande": "Voulez-vous commander une autre boisson ? (oui / non)"

	}




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
		reponse_utilisateur = input(self.REPONSES["commande_boisson"])
		try:
			new_reponse_utilisateur = int(reponse_utilisateur.replace(" ", ""))

			try:
				if new_reponse_utilisateur > 0:
					nom_boisson_commandee = self.boissons[new_reponse_utilisateur - 1].nom
					self.__verif_quantite_boisson_restante(nom_boisson_commandee)
				else:
					print(self.REPONSES["non_existante"])
					self.__verif_choix_utilisateur()

			except Exception as e:
				print(self.REPONSES["non_existante"])
				self.__verif_choix_utilisateur()	
		

		except Exception as e:
			print(self.REPONSES["mauvaise_entree"])
			self.__verif_choix_utilisateur()



	def __verif_quantite_boisson_restante(self, nom_boisson_commandee):
		if self.quantite[nom_boisson_commandee] > 0:
			self.__confirmation_utilisateur(nom_boisson_commandee)
		else:
			print(self.REPONSES["rupture_stock"])
			return self.__verif_choix_utilisateur()

	
	def __confirmation_utilisateur(self, nom_boisson_commandee):
		reponse_utilisateur = input(self.REPONSES["confirmation_choix"].format(nom_boisson_commandee))
		while reponse_utilisateur != "oui" and reponse_utilisateur != "non":
			print(self.REPONSES["mauvaise_entree"])
			self.__confirmation_utilisateur(nom_boisson_commandee)
		if reponse_utilisateur.lower().replace(" ", "") == "oui":
			self.__commande_boisson(nom_boisson_commandee)
		else:
			self.__verif_choix_utilisateur()

		
	
	def __commande_boisson(self, nom_boisson_commandee):
		print(self.REPONSES["degustation"])
		self.quantite[nom_boisson_commandee] -= 1
		recommencer = input(self.REPONSES["nouvelle_commande"]).lower().replace(" ", "")
		while recommencer != "oui" and recommencer != "non":
			recommencer = input(self.REPONSES["mauvaise_entree"])
		if recommencer == "oui":
			self.__affichage_boissons(recommencer)
		else:
			print(self.REPONSES["au_revoir"])








		# phrase = "Voici les boissons disponibles : \n\n"
		# for i in range(0,len(self.boissons) - 1):
		# 	phrase+="Boisson n°{} : {} \n".format(i+1,self.boissons[i].nom)
		# return phrase

	# #Lorsque l'utilisateur souhaite avoir des informations sur une boisson
	# def infosBoissons(self, reponse_utilisateur):
	# 	infos = "infos"

	# 	#on transforme la réponse de l'utilisateur en enlevant les potentiels espaces et majuscules
	# 	new_reponse_utilisateur = reponse_utilisateur.lower().replace(" ", "")
		

	# 	for i in range(0,len(self.boissons) - 1):
	# 		infos+=str(i+1)
	# 		#si le numéro choisi par l'utilisateur correspond bien à une boisson, on renvoie les informations demandées
	# 		if infos == new_reponse_utilisateur:
	# 			return self.boissons[i]

	# 		#on redonne à la variable infos sa valeur d'origine, afin de pouvoir continuer à la tester	
	# 		infos = "infos"

	# 	return False
	
	# def verifCommande(self, reponse_utilisateur):

	# 	for i in range(0,len(self.boissons) - 1):
	# 		#je vérifie si la boisson commandée se trouve dans mon tableau
	# 		if reponse_utilisateur == i + 1:
	# 			#je vérifie si la boisson est toujours en stock
	# 			if self.boissons[i].quantite > 0:
	# 			return True
	# 			else:
	# 			return "Cette boisson n'est plus en stock."	
		
	# 	return False


