class Utilisateur:          # par convention le nom dâ€™une classe commence toujours par une majuscule.
    anciennete = 0
    
    def __init__(self, name, age):
        self.user_name= name
        self.user_age = age
        
    def getNom(self):
        print("Salut, je suis ", self.user_name)


class Client(Utilisateur):          # par convention le nom d’une classe commence toujours par une majuscule.
    is_client = True
    
    def __init__(self, name, age, email):
        Utilisateur.__init__(self, name, age)
        self.user_email = email
        
    def getNom(self):
        print("Je suis ", self.user_name, ". Mon mail est : ", self.user_mail)
        
#class Client(Utilisateur):  # sous classe de la classe de base "Utilisateur"
    #is_client = True






pierre = Utilisateur("Pierre", 29)
mathilde = Utilisateur("Mathilde", 27)

pierre = Client("Pierre", 29,"pierre.giraud@edhec.com")
print(pierre.user_name)
print(pierre.user_email)

isinstance(pierre, Client)
issubclass(pierre, Utilisateur)