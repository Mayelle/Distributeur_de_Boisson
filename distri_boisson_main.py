from distributeur.distributeur_class import Distributeur, Boisson


liste_boissons = [
	Boisson("Super Porp", "Soda"), 
	Boisson("Durian Juice", "Jus de fruit"),
	Boisson("Duff", "Bière"), Boisson("Slurm", "Soda")
	]


#Dictionnaire d'objets qui ont comme "attribut" une quantité
distri = Distributeur(*liste_boissons)

distri._accueilUtilisateur()