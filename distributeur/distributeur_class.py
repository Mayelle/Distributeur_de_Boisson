class Boisson:
	"""docstring for Boisson"""

	#Constructeur paramétré	
	def __init__(self, nom="Coca", typeB="Soda", prix=2, quantite=0):
		self.nom = nom
		self.typeB = typeB
		self.prix = prix
		self.quantite = quantite

	def __str__(self):
		return "Nom : {} \nType : {} \nPrix : {}€ \nQuantité restante : {}".format(self.nom, self.typeB, self.prix, self.quantite) 

	#Méthode pour remettre des boissons en stock
	def remettreEnStock(nbBoissonAjoute):
		self.quantite+=nbBoissonAjoute

	
class Distributeur:

	"""docstring for Distributeur"""
	
	#Constructeur paramétré
	def __init__(self, *boissons):
		self.boissons = boissons

	def __str__(self):
		phrase = "Voici les boissons disponibles : \n\n"
		for i in range(0,len(self.boissons) - 1):
			phrase+="Boisson n°{} : {} \n".format(i+1,self.boissons[i].nom)
		return phrase

	#Lorsque l'utilisateur souhaite avoir des informations sur une boisson
	def infosBoissons(self, reponseUti):
		infos = "infos"

		#on transforme la réponse de l'utilisateur en enlevant les potentiels espaces et majuscules
		newReponseUti = reponseUti.lower().replace(" ", "")
		

		for i in range(0,len(self.boissons) - 1):
			infos+=str(i+1)
			#si le numéro choisi par l'utilisateur correspond bien à une boisson, on renvoie les informations demandées
			if infos == newReponseUti:
				return self.boissons[i]

			#on redonne à la variable infos sa valeur d'origine, afin de pouvoir continuer à la tester	
			infos = "infos"

		return False
	

