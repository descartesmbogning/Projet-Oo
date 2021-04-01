from Animal import Animal
    

class Oiseau(Animal):  # classe Oiseau qui hérite de la classe animal
    # mot-clé super pour redéfinir la fonction __init__ chez l’oiseau sans avoir à tout réécrire.
    def __init__(self, poids, taille, altitude_max):
        super().__init__(poids, taille)
        self.set_altitude_max(altitude_max)
    #redefinir la méthode se_deplacer( ) pour Oiseau.     
    def se_deplacer(self):    
        return 'Je vole'

    def set_altitude_max(self, altitude_max): #Encapsulation
        self.__altitude_max = altitude_max
    
    def get_altitute_max(self):
        return self.__altitude_max


#Instanciez maintenant ces deux objets dans le
#programme principal et appelez la méthode se_deplacer( ) pour chacun de ces
#objets.
rosignol = Oiseau(2, 1, 100)
print(f"Je suis madame la rosignol, l'{type(rosignol)}, {rosignol.se_deplacer()}")






