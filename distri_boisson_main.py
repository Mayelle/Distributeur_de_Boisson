from distributeur.distributeur_class import Distributeur, Boisson



superPorp = Boisson("Super Porp", "Soda")
durianJuice = Boisson("Durian Juice", "Jus de fruit")
duff = Boisson("Duff", "Bière")
slurm = Boisson("Slurm", "Soda")


#Dictionnaire d'objets qui ont comme "attribut" une quantité
distri = Distributeur(superPorp, durianJuice, duff, slurm)

print("Bonjour ! Bienvenue au Distri'Boisson !")
reponseUti = ""
while reponseUti != "non" and reponseUti != "oui":
	reponseUti = input("Voulez-vous voir la liste des boissons ? (oui/non) ").lower().replace(" ", "")
	print(distri.demandeAffichageBoissons(reponseUti))





# module = ""

# while module != "Exit":

# 	if reponseUti.upper() == 'B':
# 		module = "afficherBoissons"

# 	if module == "afficherBoissons":
# 		print(distri)

# 	if "infos" in reponseUti.lower():
# 		module = "afficherInformations"

# 	if module == "afficherInformations":
# 		if distri.infosBoissons(reponseUti) == False:
#  			print("Cette boisson n'existe pas!")
#  			module = "afficherBoissons"
#  		else:
#  			print(distri.infosBoissons(reponseUti))
#  			reponseUti = input("Appuyez sur \'B\' pour revenir au choix des boissons")

#  	if isinstance(reponseUti, int) and module != "paiement":
#  		module = "Commande"

#  	if module == "Commande":
#  		verif = distri.verifCommande(reponseUti)
#  		if verif == False:
#  			print("Cette boisson n'existe pas !")
#  		elif verif == True:
#  			module = "Paiement"
#  		else:
#  			print distri.verifCommande(reponseUti)


		

#tant que l'utilisateur ne choisit pas l'une des options proposées ... 
# while reponseUti.upper() != 'X' and reponseUti.upper() != 'B':
# 	reponseUti = input("Pardon, je n'ai pas compris ce que vous aviez écrit. Merci de recommencer.")

# if reponseUti.upper() == 'X':
# 	print("Merci de votre visite, à bientôt !")

# elif reponseUti.upper() == 'B':
# 	print(distri)
# 	reponseUti = input("Appuyez sur le numéro correspondant à votre boisson pour la commander. \nSinon, entrez \'Infos\' suivi du numéro de votre boisson pour avoir des informations.")
# 	if isinstance(reponseUti, str):
# 		if distri.infosBoissons(reponseUti) == False:
# 			print("Cette boisson n'existe pas, veuillez recommencer !")
# 		else:
# 			print(distri.infosBoissons(reponseUti))
# 			

