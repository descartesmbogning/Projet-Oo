class Utilisateur:          # par convention le nom d’une classe commence toujours par une majuscule.
    anciennete = 0
    
    def __init__(self, nom, age):
        self.user_name=nom
        self.user_age = age
        
    def getNom(self):
        print("Salut, je suis ", self.user_name)
        

pierre = Utilisateur("Pierre", 29)
mathilde = Utilisateur("Mathilde", 27)

print(pierre.user_name)
print(mathilde.user_name)
p = pierre.getNom()
