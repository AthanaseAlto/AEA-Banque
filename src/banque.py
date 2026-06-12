from client import Client
from compte import Compte


class Banque:

    def __init__(self):
        self.comptes = []

    def creer_compte(
        self,
        nom,
        prenom,
        age,
        localisation,
        email,
        pwd,
        solde_initial
    ):

        client = Client(
            nom,
            prenom,
            age,
            localisation,
            email,
            pwd
        )

        compte = Compte(client,solde_initial)

        self.comptes.append(compte)

        print("Compte cree avec succes.")
        print(f"Bienvenue {client.prenom} {client.nom}")
        print(f"ID client : {client.num_clt}")

    def trouver_compte(self, num_client):

        for compte in self.comptes:

            if compte.client.num_clt == num_client:
                return compte

        return None

    def transfert(
        self,
        num_source,
        num_destination,
        montant,
        pwd
    ):
        print("Source:", num_source)
        print("Destination:", num_destination)
        source = self.trouver_compte(num_source)
        destination = self.trouver_compte(num_destination)

        if source is None:
            print("Compte source introuvable.")
            return

        if destination is None:
            print("Compte destination introuvable.")
            return

        if not source.client.verifier_pwd(pwd):
            print("Mot de passe incorrect.")
            return

        if montant > source.solde:
            print("Solde insuffisant.")
            return

        source.solde -= montant
        destination.solde += montant

        print(f"Transfert de {montant} Fcfa effectue avec succes")

    def rechercher_email(self, email):

        for compte in self.comptes:

            if compte.client.email == email:
                return compte

        return None
    def afficher_tous_les_comptes(self):

        if len(self.comptes) == 0:
            print("Aucun compte enregistre.")
            return

        print("\n===== LISTE DES COMPTES =====")
        for compte in self.comptes:
            f"{compte.client.num_clt} - "
            f"{compte.client.nom} "
            f"{compte.client.prenom} - "
            f"{compte.solde} FCFA"