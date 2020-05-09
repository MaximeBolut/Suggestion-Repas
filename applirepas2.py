from random import sample, shuffle
from datetime import date
import tkinter
from tkinter import *



#---------------Fonctions ----------------------------------------------------------------------------------------------------------------
def stringtolist(string): 
    if type(string)== str: 
      ingredient_list = string.split(", ")
      ingredient_list_lower = [i.lower() for i in ingredient_list]
    else:
    	ingredient_list_lower = ['NA']

    return ingredient_list_lower 


bigdico={'spagetti bolognaise': {'type': 'viande', 'saison': 'ete', 'ingredient': ['pate', 'bolognaise'], 'recette': 'Faire cuire les pates. Melanger avec la bolo! Ajouter du fromage, des tomates…  ', 'temps de preparation': 2.0, 'temps de cuisson': 8.0, 'temps total': 10},
 'cordon bleu': {'type': 'viande', 'saison': 'all', 'ingredient': ['cordon bleu', ''], 'recette': 'Faite cuire a la poele 6 minutes le cordon bleu.', 'temps de preparation': 0.0, 'temps de cuisson': 6.0, 'temps total': 6},
 'salade': {'type': 'veg', 'saison': 'ete', 'ingredient': ['salade', 'moutarde', 'tomate'], 'recette': 'adggvqv q qefasf', 'temps de preparation': 2.0, 'temps de cuisson': 0.0, 'temps total': 2}, 'saumon': {'type': 'poisson', 'saison': 'hiver', 'ingredient': ['saumon', 'huile'], 'recette': 'faire cuire saumon au four', 'temps de preparation': 2.0, 'temps de cuisson': 20.0, 'temps total': 22},
 'Carpaccio provençal': {'type': 'viande', 'saison': 'all', 'ingredient': ['carpacio', 'huile olive'], 'recette': 'rien a faire', 'temps de preparation': 5.0, 'temps de cuisson': 0.0, 'temps total': 5},
 'Magret de canrds aux figues': {'type': 'viande', 'saison': 'automne', 'ingredient': ['figues', 'magret de canard'], 'recette': 'nan', 'temps de preparation': 2.0, 'temps de cuisson': 20.0, 'temps total': 22},
 'Tartare de Thon': {'type': 'poisson', 'saison': 'ete', 'ingredient': ['thon'], 'recette': 'non', 'temps de preparation': 2.0, 'temps de cuisson': 0.0, 'temps total': 2}, 'Fish and chips': {'type': 'poisson', 'saison': 'all', 'ingredient': ['NA'], 'recette': 'ffeqwf ', 'temps de preparation': '?', 'temps de cuisson': '?', 'temps total': 0},
 'ravioli ricotta-epinard': {'type': 'veg', 'saison': 'automne', 'ingredient': ['ravioli'], 'recette': 'Juste a cuire 5min', 'temps de preparation': 0.0, 'temps de cuisson': 5.0, 'temps total': 5}, 'ratatouille': {'type': 'veg', 'saison': 'automne', 'ingredient': ['ratatouille en boite'], 'recette': 'Juste a rechauffer 5min a la poele ou casserole ', 'temps de preparation': 0.0, 'temps de cuisson': 5.0, 'temps total': 5},
 'Macaronis fromage': {'type': 'veg', 'saison': 'hiver', 'ingredient': ['NA'], 'recette': 'fqwefqw ', 'temps de preparation': 'nan', 'temps de cuisson': 'nan', 'temps total': 0}, 'Tartiflette lardon': {'type': 'viande', 'saison': 'hiver', 'ingredient': ['patate', 'lardon', 'ail', 'roblochon', 'vin blanc'], 'recette': "Eplucher les patates et les faire cuire 15 bonnes minutes dans de l'eau chaude. Saissir les lardon a la poele. Frotter l'ail dans le plat a tartifflete. Couper les patates en rondelles epaisse et les repartir dans le plat avec les lardons. Couper le roblochon dans en 2 dans le sens de sa hauteur (pas comme on coupe le camember! lol) et le repartir sur le dessus du plat. Ajouter un verre de vin blanc et mettre le tout 45min 1h au four a 210degree", 'temps de preparation': 25.0, 'temps de cuisson': 60.0, 'temps total': 85},
 'Goulash': {'type': 'viande', 'saison': 'hiver', 'ingredient': ['NA'], 'recette': 'efwf', 'temps de preparation': 'nan', 'temps de cuisson': 'nan', 'temps total': 0}, 'Tarte aux legumes printanier': {'type': 'veg', 'saison': 'printemps', 'ingredient': ['NA'], 'recette': 'egh', 'temps de preparation': "?", 'temps de cuisson': '?', 'temps total': 0}, 'Burger oeuf poché': {'type': 'veg', 'saison': 'printemps', 'ingredient': ['oeuf', 'pain burger'], 'recette': 'Un burger avec un oeuf a la place du steak!', 'temps de preparation': 5, 'temps de cuisson': 5.0, 'temps total': 5}}



#--------------------------------------------------------------------------------------------------------------------------------------------

window=Tk()
window.title("L'appli Repas")
#window.iconbitmap('max_icon.ico')
window.config(background='#2E4053')
window.geometry("480x1080")


def inforecette(nomrecette):
  recette=Tk()
  recette.title('recette '+ nomrecette)
  #recette.iconbitmap('max_icon.ico')
  recette.config(background='#2E4053')
  recette.geometry("720x480")
  
  frame=Frame(recette,background='#2E4053', bd=2)  
  frame2=Frame(recette,background='#E74C3C', bd=2)

  label_title=Label(frame, text= bigdico[nomrecette]['recette'], font = ('Comic Sans MS',12), bg ='#2E4053', fg = '#E74C3C')
  label_title.pack()

  label_sub=Label(frame, text= 'Les ingredients:', font = ('Comic Sans MS',12), bg ='#2E4053', fg = '#E74C3C')
  label_sub.pack()

  for i in bigdico[nomrecette]['ingredient']:
   label_sub=Label(frame, text= i, font = ('Comic Sans MS',12), bg ='#2E4053', fg = '#E74C3C')
   label_sub.pack()

  label_info=Label(frame2, text= 'Temps de preparation '+ str(bigdico[nomrecette]['temps total'])+' min', font = ('Comic Sans MS',12), bg ='#E74C3C', fg = '#2E4053')
  label_info.pack()

  frame.pack(expand=YES)
  frame2.pack(expand=YES)



def selection_plats():
  masterframe=Frame(window,background='#2E4053', bd=2) 
  masterframe.pack()
 
  season=IntVar()

  season_check=Checkbutton(masterframe, text='Voulez-vous tenir compte des saisons?',font = ('Comic Sans MS',12), bg ='#2E4053', fg = '#E74C3C', variable=season)
  season_check.pack()
 
  def selection_fetch():
    
    seasonis=int(season.get())

    if seasonis==1: 
    #If season taken in account, the we get the month of today and depending on the season we select the right dictionary of dishes
      today = date.today()
      #d1 = today.strftime("%d/%m/%Y")
      month = int(today.strftime("%m"))
            
      if (month>9 and month<12):
        plats = {i:bigdico[i] for i in bigdico.keys() if (bigdico[i]['saison'] == 'automne' or bigdico[i]['saison'] == 'all')}

      elif(month>=3 and month<=6):
        plats = {i:bigdico[i] for i in bigdico.keys() if (bigdico[i]['saison'] == 'printemps' or bigdico[i]['saison'] == 'all')}

      elif(month>6 and month<=9):
        plats = {i:bigdico[i] for i in bigdico.keys() if (bigdico[i]['saison'] == 'ete' or bigdico[i]['saison'] == 'all')}

      else:
        plats = {i:bigdico[i] for i in bigdico.keys() if (bigdico[i]['saison'] == 'hiver' or bigdico[i]['saison'] == 'all')}

    else:
      plats = bigdico

    nb_viande= int(e3.get())
    nb_poisson=int(e2.get())
    nb_veg=int(e1.get())

    viandes= sample([i for i in plats.keys() if plats[i]['type'] == 'viande'], nb_viande)
    poisson= sample([i for i in plats.keys() if plats[i]['type'] == 'poisson'], nb_poisson)
    veg= sample([i for i in plats.keys() if plats[i]['type'] == 'veg'], nb_veg)

    platspropose=viandes+poisson+veg
    shuffle(platspropose)
    
    frame=Frame(masterframe,background='#2E4053', bd=2) 
    frame.pack()
    for item in platspropose:
      label_title=Button(frame,height=1, width=30, text=item, font = ('Comic Sans MS',12), bg ='#2E4053', fg = '#E74C3C', command= lambda x= item: inforecette(x))
      label_title.pack()


       
    def clear_frame():
      masterframe.destroy()

    clear=Button(frame, text= 'clear', font = ('Comic Sans MS',12), bg ='#2E4053', fg = '#E74C3C', width=20,  command= clear_frame)
    clear.pack()




  enterveg=Label(masterframe, text= "Entrez le nombre de plats vegetarien:", font = ('Comic Sans MS',12), bg ='#2E4053', fg = '#E74C3C')
  enterveg.pack()
  e1=Entry(masterframe,text= 'viande', width=15 )
  e1.pack()
  enterpoisson=Label(masterframe, text= "Entrez le nombre de plats de poisson:", font = ('Comic Sans MS',12), bg ='#2E4053', fg = '#E74C3C')
  enterpoisson.pack()
  e2=Entry(masterframe, text= 'veg', width=15 )
  e2.pack()
  enterviande=Label(masterframe, text= "Entrez le nombre de plats de viande:", font = ('Comic Sans MS',12), bg ='#2E4053', fg = '#E74C3C')
  enterviande.pack()
  e3=Entry(masterframe, width=15 )
  e3.pack()
  go=Button(masterframe, text= 'GO', font = ('Comic Sans MS',12), bg ='#2E4053', fg = '#E74C3C', width=20, command= selection_fetch)
  go.pack()



def reste():
  masterframe=Frame(window,background='#2E4053', bd=2) 
  masterframe.pack()

  def canbecooked():
    frame=Frame(masterframe,background='#2E4053', bd=2) 
    frame.pack()
    ingredientliste=ingredient_user.get()
    ingredient_restant=stringtolist(ingredientliste)

    can_be_cooked={}
    for i in bigdico.keys():
    #check if ingredient_restant contains all elements in ingredient
      result =  all(elem in ingredient_restant  for elem in bigdico[i]['ingredient'])
      if result:
        can_be_cooked[i]=bigdico[i]



    for i in can_be_cooked.keys():
      label_title=Button(frame, height=1, width=30, text= i, font = ('Comic Sans MS',12), bg ='#2E4053', fg = '#E74C3C', command= lambda x= i: inforecette(x))
      label_title.pack()
   


    def clear_frame():
      masterframe.destroy()

    clear = Button(frame, text= "clear", font = ('Comic Sans MS',12), bg ='#2E4053', fg = '#E74C3C', command= clear_frame)
    clear.pack()



 
  
  label_info=Label(masterframe, text= "Entrez les ingredients qu'il vous reste:", font = ('Comic Sans MS',12), bg ='#E74C3C', fg = '#2E4053')
  label_info.pack()
  ingredient_user=Entry(masterframe, width=50)
  ingredient_user.pack()
  go=Button(masterframe, text= 'GO', font = ('Comic Sans MS',12), bg ='#2E4053', fg = '#E74C3C', width=20, command= canbecooked)
  go.pack()










choix1 = Button(window, height=2, width=50, text="je veux une liste de plats!", font=("Courrier", 12), bg='#2E4053', fg='#E74C3C', command=selection_plats)
choix1.pack()

choix2 =Button(window, height=2, width=50, text="je veux savoir ce que je peux cuisiner avec ce que j'ai!", font=("Courrier", 12), bg='#2E4053', fg='#E74C3C', command=reste)
choix2.pack()

choix3 =Button(window, height=2, width=50, text="je veux un dessert!", font=("Courrier", 12), bg='#2E4053', fg='#E74C3C')
choix3.pack()



window.mainloop()