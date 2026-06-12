from banque import Banque

banque = Banque()

def view_menu_principal():

    print("""
                                                    ========================================
                                                       WELCOME TO AEA BANK SYSTEM
                                                    ========================================

1 - Créer un compte
2 - Se connecter
0 - Quitter
""")

def view_menu_client():

    print("""
                                                                        ====================
                                                                            MON COMPTE
                                                                        ====================

1 - Consulter solde
2 - Déposer
3 - Retirer
4- Transefet d'argent
5 - Mes informations
6 - Modifier mot de passe
0 - Déconnexion
""")

while True:

    view_menu_principal()
    choix = int(input("Choix : "))
    match choix:
        case 1:
            nom = input("Entrer votre nom")
            prenom = input("Entrer votre prenom")
            age = int(input("Entrez votre âge"))
            ville = input("Entrer votre localisation")
            email = input("Email : ")
            mot_de_passe = input("Saisir mot de passe")

            print("\n1 - Courant")
            print("2 - Epargne")
            type_choix = input("Type de compte : ")

            if type_choix == "1":
                type_compte = "Courant"
            else:
                type_compte = "Epargne"

            solde = int(input("Solde initial : "))
            compte = banque.creer_compte(nom,prenom,age,ville,email,pwd,type_compte,solde)
            print("\nCompte créé avec succès")


        case 2:
            email_clt = input("Entrer l'email")
            pwd = input("Entrer votre mot de passe")
            connecte_compte = (banque.rechercher_email(email_clt))

            if (connecte_compte is not None and connecte_compte.client.verifier_pwd(pwd)):
                while True:
                    view_menu_client()
                    choix_clt = int(input("Choix : "))
                    match choix_clt:
                        case 1:
                            print(connecte_compte.consulter_solde())
                        case 2:
                            montant = int(input("Montant : "))

                            print(connecte_compte.deposer(montant ))
                        case 3:
                            montant = int(input("Montant : "))
                            print(connecte_compte.retirer(montant))
                        case 4:
                            print("Fonction transfert .")
                        case 5:
                            print(connecte_compte.client)
                        case 6:
                            ancien = input("Ancien mot de passe : ")
                            nouveau = input("Nouveau mot de passe : ")
                            connecte_compte.client.update_pwd(ancien,nouveau)
                        case 0:
                            print( "Déconnexion...")
                            break
                        case _:
                            print(  "Choix invalide.")
            else:
                print("Email ou mot de passe incorrect.")
        case 0:
            print("Merci d'avoir utilisé AEA BANK.")
            break
        case _:
            print("Choix invalide.")

view_menu_principal()