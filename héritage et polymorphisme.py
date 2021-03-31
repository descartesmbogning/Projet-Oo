class Client(Utilisateur):          # par convention le nom d’une classe commence toujours par une majuscule.
    is_client = True
    
    def __init__(self, nom, age, mail):
        Utilisateur.__init__(self, name, age)
        self.user_mail = mail
        
    def getNom(self):
        print("Je suis ", self.user_name, ". Mon mail est : ", self.user_mail)
        
class Client(Utilisateur):  # sous classe de la classe de base "Utilisateur"
    is_client = True


pierre = Client("Pierre", 29, "pierre.giraud@edhec.com")
print(pierre.user_name)