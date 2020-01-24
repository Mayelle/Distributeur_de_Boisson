class Boisson:
	"""docstring for Boisson"""

	#Constructeur paramétré	
	def __init__(self, nom="Coca", typeB="Soda", prix=2, quantite=0):
		self.nom = nom
		self.typeB = typeB
		self.prix = prix
		self.quantite = quantite

	def __str__(self):
		return "Nom : {} \nType : {} \nPrix : {} \nQuantité restante : {}".format(self.nom, self.typeB, self.prix, self.quantite) 

	#Méthode pour remettre des boissons en stock
	def remettreEnStock(nbBoissonAjoute):
		self.quantite+=nbBoissonAjoute

	
class Distributeur:

	"""docstring for Distributeur"""
	
	#Constructeur paramétré
	def __init__(self, *boissons):
		self.boissons = boissons

	#def proposerBoissons():
		
		
	

