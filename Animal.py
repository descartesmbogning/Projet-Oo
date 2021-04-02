class Animal(): # créer une classe Animal
    """
    Création d'un zoo virtuel en python
    """
    poids = 0    
    taille = 0 
    
    def __init__(self, poids, taille):
        self.set_poids(poids)
        self.taille = taille
        
    def se_deplacer(self):    #Ajoutez une méthode se_deplacer( ) qui pour le moment ne fait rien.
        pass 

    def get_poids(self):   ## getter method to get the properties using an object
        return self.__poids

    def set_poids(self, poids): ## setter method to change the value 'poids' using an object
        if poids < 0:
            raise ValueError("value must be > 0")
        else:
            self.__poids = poids

    #Affectation des guetters et setters
    #Encapsule les attributs pour mieux les controler
    #Simplifie l'écriture dans le programme principal
    poids = property(get_poids, set_poids)

    def __str__(self):
        return f"L animal pèse {self.poids}kg et et à une taille de {self.__taille}"

#PROGRAMME PRINCIPAL

#instanciez cet objet. Faites un print de ses attributs.  
#chat = Animal(3, 2) 
# chat.poids(3)
#print(chat.set_poids)
#print(f"La taille de l'animal est de : {chat.get_poids()}")

ani = Animal(10, 3)

#print(str(ani))

#instanciez cet objet. Faites un print de ses attributs.  
python = Animal(80, 2) 
print(f"Le poids de l'animal est de : {python.poids}")
print(f"La taille de l'animal est de : {python.taille}")


#Instanciez maintenant ces deux objets dans le programme principal 
# et appelez la méthode se_deplacer( ) pour chacun de ces objets.
#python = Serpent(10, 5)
#rosignol = Oiseau(2, 1)
#print(f"Je suis monsieur python, {type(python)}, {python.se_deplacer()}")
#print(f"Je suis madame la rosignol, l'{type(rosignol)}, {rosignol.se_deplacer()}")


