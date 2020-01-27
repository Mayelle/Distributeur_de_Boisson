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
	
	#Constructeur paramétré
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
			phrase+="Boisson n°{} :\n{} \nQuantité restante: {}\n\n".format(i,boisson,self.quantite[boisson.nom])
			i = i+1
		return phrase



		# phrase = "Voici les boissons disponibles : \n\n"
		# for i in range(0,len(self.boissons) - 1):
		# 	phrase+="Boisson n°{} : {} \n".format(i+1,self.boissons[i].nom)
		# return phrase

	# #Lorsque l'utilisateur souhaite avoir des informations sur une boisson
	# def infosBoissons(self, reponseUti):
	# 	infos = "infos"

	# 	#on transforme la réponse de l'utilisateur en enlevant les potentiels espaces et majuscules
	# 	newReponseUti = reponseUti.lower().replace(" ", "")
		

	# 	for i in range(0,len(self.boissons) - 1):
	# 		infos+=str(i+1)
	# 		#si le numéro choisi par l'utilisateur correspond bien à une boisson, on renvoie les informations demandées
	# 		if infos == newReponseUti:
	# 			return self.boissons[i]

	# 		#on redonne à la variable infos sa valeur d'origine, afin de pouvoir continuer à la tester	
	# 		infos = "infos"

	# 	return False
	
	# def verifCommande(self, reponseUti):

	# 	for i in range(0,len(self.boissons) - 1):
	# 		#je vérifie si la boisson commandée se trouve dans mon tableau
	# 		if reponseUti == i + 1:
	# 			#je vérifie si la boisson est toujours en stock
	# 			if self.boissons[i].quantite > 0:
	# 			return True
	# 			else:
	# 			return "Cette boisson n'est plus en stock."	
		
	# 	return False


