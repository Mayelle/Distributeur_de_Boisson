from distributeur.distributeur_class import Distributeur, Boisson



superPorp = Boisson("Super Porp", "Soda")
durianJuice = Boisson("Durian Juice", "Juice")
duff = Boisson("Duff", "Bière")
slurm = Boisson("Slurm", "Soda")



distri = Distributeur(superPorp, durianJuice, duff, slurm)




print("Bonjour ! Bienvenue au Distri'Boisson !")
reponseUti = input(" Appuyez sur \'B\' pour voir la liste des boissons proposées. \n Appuyez sur \'X\' pour partir.")

#tant que l'utilisateur ne choisit pas l'une des options proposées ... 
while reponseUti.upper() != 'X' and reponseUti.upper() != 'B':
	reponseUti = input("Pardon, je n'ai pas compris ce que vous aviez écrit. Merci de recommencer.")

if reponseUti.upper() == 'X':
	print("Merci de votre visite, à bientôt !")

elif reponseUti.upper() == 'B':
	print(distri)
	reponseUti = input("Appuyez sur le numéro correspondant à votre boisson pour la commander. \nSinon, entrez \'Infos\' suivi du numéro de votre boisson pour avoir des informations.")
	if isinstance(reponseUti, str):
		if distri.infosBoissons(reponseUti) == False:
			print("Cette boisson n'existe pas, veuillez recommencer !")
		else:
			print(distri.infosBoissons(reponseUti))