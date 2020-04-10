
from random import sample, shuffle
from datetime import date



#dictionnaires a remplir: 
plats_winter={'viande':['Orgie de Foie Gras', 'Daube de boeuf', 'Tartiflette lardon', 'Goulash', 'Blanquette de vaeux', 'Chapon de noel', 'Cuisse de canard','stew', 'Pates-jambon-fromage', 'Boeuf bourgignon', 'Couscous de poulet'],
 'poisson': ['Pave de saumon-riz','Saumon de noel', 'Poisson noel', 'Pates au saumon', 'Soupe de poisson', 'Fish finger-riz'],
 'vegetarien':['gratin de coquuillete', 'Macaronis fromage','tartiflette sans lardon','pates coco piquantes', 'patate aux four', 'salade russe','pizza 3-fromages', 'Soufllé fromage'] }

plats_spring={'viande':['cordon bleu pates', 'Roti de veau', 'Burger!', 'Carpaccio provençal',  'viandespring5','viandespring6'],
 'poisson': ["poisson d'avril",'nouilles sautees aux fruits' 'fish finger-riz', 'poisson spring 4', 'poisson spring 5', 'poisson spring 6'],
 'vegetarien':['ratatouille','Tarte aux legumes printanier', 'Burger oeuf poché', 'Millefeuille de pomme de terre', 'Pizza au chevre', 'Lasagne vegetarienne'] }

plats_summer={'viande':[ "Canard a l'orange",'Steak frite','Oeuf a la basquaise', 'Spagetti bolo', 'Cuisse de canard','Salade de gesier', 'Cordon bleu pates', 'Pates-jambon-fromage'],
 'poisson': ['Tartare de Thon', 'Papillote de saumon', 'Salade de sardines, olives et tomates', 'Bar grillé aromatisé aux fines herbes', 'riz saute aux noix de cajou','nouilles sautees aux fruits de mer', 'pates au saumon', 'salade de thon', 'Carpaccio de saumon', 'Tilapia à la mangue'],
 'vegetarien':["Salade d’aubergines rôties au chèvre et menthe", "Melon", "Houmous a l'aubergine",'Aubergine farcie', 'sushis veggie','Taboulé ', 'Salade de penne à la feta', 'Salade de pomme de terre à la grecque'] }

plats_autumn={'viande':['Roti de porc aux pruneaux', 'Magret de canrds aux figues', 'steak frite', 'Pates poulet bechamel', 'Cordon bleu pates', 'Pates-jambon-fromage', 'Quiche poireaux jambon','viande autumn14', 'viande autumn5', 'viande autumn6'],
 'poisson': ['Fish finger-riz','Fish and chips', 'poisson panné', 'poisson autumn4', 'poisson autumn5'],
 'vegetarien':['ravioli ricotta-epinard', 'ratatouille', 'soupe au potiron',"citrouille d'haloween",'Lasagne aux champignons', 'Risotto aux champignons'] }



season=abs(int(input(print("Bonjour! pret pour des propositions de plats? Voulez-vous tenir compte des saisons ?\n Oui: 1, Non: 0 \n"))))

if season==1: 
  #If season taken in account, the we get the month of today and depending on the season we select the right dictionary of dishes
  today = date.today()
  #d1 = today.strftime("%d/%m/%Y")
  month = int(today.strftime("%m"))

  if (month>9 and month<12): 
    plats=plats_autumn
  elif(month>=3 and month<=6):
    plats=plats_spring
  elif(month>6 and month<=9):
    plats=plats_summer
  else:
    plats=plats_winter

#if we don't care of the season, we 'merge' the dictionaries: keys stay the sames but value are concatenation of lists from each season dictionary
else:

  plats= {'viande': plats_winter['viande']+plats_spring['viande']+plats_summer['viande']+ plats_autumn['viande'],
 'poisson': plats_winter['poisson']+plats_spring['poisson']+plats_summer['poisson']+ plats_autumn['poisson'],
  'vegetarien': plats_winter['vegetarien']+plats_spring['vegetarien']+plats_summer['vegetarien']+ plats_autumn['vegetarien']} 


try:
  nb_repas=int(input(print('Combien de repas dois-je vous sugerer pour cette semaine ? \n')))
except ValueError:
	print("donnez un chiffre")
	nb_repas=int(input(print('Combien de repas dois-je vous sugerer pour cette semaine ? \n')))


nb_veg=abs(int(input(print("Ok ça marche, je vais vous trouver %d bons petits plats repartis en 3 categories: vegetarien, poisson et viande ! \n Combien de plat vegetarien voulez-vous? \n" %nb_repas))))


nb_poisson=abs(int(input(print('Ok, et combien de plat avec du poisson cette semaine ? \n'))))

#I consider that the user is bad at maths
#If there are dishes left, 2 choices: either we put them as meat dishes or we redistribute them on the fish/veg dishes
if (nb_repas-nb_veg-nb_poisson)>0:
  viande=int(input(print('Ok, il nous reste %d plats... je vous les propose en plats de viande ? \nOui: 1, Non: 0' %(nb_repas-nb_veg-nb_poisson))))
else:
  viande=0

if viande == 1:
	nb_viande = nb_repas-nb_veg-nb_poisson
	print("Ok, on a donc " +str(nb_viande) + " plats de viande, "+str(nb_veg)+" plats vegetarien et " + str(nb_poisson)+" plats de poissons")
else:
  plats_restants = (nb_repas-nb_veg-nb_poisson)
  nb_poisson = nb_poisson + plats_restants//2  
  nb_veg = nb_veg + plats_restants//2 + (plats_restants%2)
  nb_viande=0
  print("Ok, je vous propose donc "+str(nb_veg)+" plats vegetarien et " + str(nb_poisson)+ " plats avec du poisson.")

selection =[str(i) for i in range(nb_repas)]
print('voici la liste des plats : \n')

#main job of the pgm lol. All the rest is like fiddling around...
selection = sample(plats['vegetarien'], nb_veg) +sample(plats['poisson'], nb_poisson) +sample(plats['viande'], nb_viande)  

shuffle(selection) #optional 

#nicer way to show the list than print(selection)
for i in range(len(selection)):
  print(selection[i])

