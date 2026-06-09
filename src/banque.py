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
        pwd
    ):

        client = Client(
            nom,
            prenom,
            age,
            localisation,
            pwd
        )

        compte = Compte(client)

        self.comptes.append(compte)

        print("Compte cree avec succes.")
        print(f"Bienvenue {client.prenom} {client.nom}")
        print(f"ID client : {client.num_clt}")
        print(f"ID compte : {compte.num_compte}")

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

    def afficher_tous_les_comptes(self):

        if len(self.comptes) == 0:
            print("Aucun compte enregistre.")
            return

        print("\n===== LISTE DES COMPTES =====")
        for compte in self.comptes:
            print(compte)