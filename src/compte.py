class Compte:
    def __init__(self, client, solde_initial=0):
        self.client = client
        self.solde = solde_initial

    def deposer(self, montant):
        if montant > 0:
            self.solde += montant
            print(f"Dépôt de {montant} FCFA effectué.")
        else:
            print("Montant invalide.")

    def retirer(self, montant):
        if montant <= 0:
            print("Montant invalide.")
        elif montant > self.solde:
            print("Solde insuffisant.")
        else:
            self.solde -= montant
            print(f"Retrait de {montant} FCFA effectué.")

    def __str__(self):
        return (
            f"\n=== COMPTE BANCAIRE ===\n"
            f"Client : {self.client}\n"
            f"Solde : {self.solde} FCFA"
        )
