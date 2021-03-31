class Utilisateur:          # par convention le nom d’une classe commence toujours par une majuscule.
    statut = "Inscrit"      # Cette classe Utilisateur possède ici deux variables statut et age 
    age = 0                 # variable

    def setNom(self, n):    # et définit également une fonction setNom().
        self.nom = n

# Pour créer des objets à partir de cette classe, nous allons utiliser la syntaxe Utilisateur() comme ceci : 
pierre = Utilisateur()
mathilde = Utilisateur()

pierre.statut
'Inscrit'
pierre.age
0
mathilde.statut
'Inscrit'
mathilde.age
0
pierre.setNom("Pierre")
pierre.nom
'pierre'


