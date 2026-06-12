class Client:
    compteur_clt = 1
    def __init__(self,nom, prenom, age, localisation,email, pwd):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.localisation = localisation
        self.email= email
        self.pwd = pwd
        self.num_clt = f"CLT{Client.compteur_clt}"
        Client.compteur_clt += 1

    def verifier_pwd(self, pwd):
        return self.pwd == pwd

    def update_pwd (self, old_pwd,new_pwd):
        if self.verifier_pwd(old_pwd):
            self.pwd = new_pwd
            print("Mot de passe modifié avec succès")
        else:
            print("Mot de passe incorrect")

    def __str__(self):
        return f"{self.num_clt} - {self.nom} {self.prenom} - {self.age} - {self.localisation}"

