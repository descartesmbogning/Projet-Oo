from Animal import Animal

class Serpent(Animal):  # classe serpent qui hérite de la classe animal
    def se_deplacer(self):    #redefinir la méthode se_deplacer( ) pour serpent.
       return 'Je rampe'

    


#Instanciez maintenant ces deux objets dans le
#programme principal et appelez la méthode se_deplacer( ) pour chacun de ces
#objets.
python= Serpent(10, 5)

print(f"Je suis monsieur python, {type(python)}, {python.se_deplacer()}")




