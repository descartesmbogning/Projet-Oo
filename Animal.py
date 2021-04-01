class Animal(): # créer une classe Animal
    """
    Création d'un zoo virtuel en python
    """
    poids = 0    
    taille = 0 
    
    def __init__(self, poids, taille):
        self.__poids = poids
        self.__taille = taille
        
    def se_deplacer(self):    #Ajoutez une méthode se_deplacer( ) qui pour le moment ne fait rien.
        pass 

    def get_poids(self):   ## getter method to get the properties using an object
        return self.__poids

    def set_poids(self, poids): ## setter method to change the value 'poids' using an object
        if poids < 0:
            raise ValueError("value must be > 0")
        else:
            self.__poids = poids

    poids = property(get_poids, set_poids)




#instanciez cet objet. Faites un print de ses attributs.  
chat = Animal(-3, 2) 
chat.set_poids(3)
#print(chat.set_poids)
print(f"La taille de l'animal est de : {chat.set_poids}")





