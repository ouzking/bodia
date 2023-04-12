import sqlite3

print("Application de Gestion de budget avec Python et Sqlite3")
with sqlite3.connect("budget.db") as connection:
    cursor = connection.cursor()
    
cursor.execute(
    "CREATE TABLE IF NOT EXISTS budget (id INTEGER PRIMARY KEY AUTOINCREMENT, loyer TEXT, manger TEXT, transport TEXT, loisir TEXT, tontine TEXT, factures_courant TEXT, salaire TEXT, business TEXT, tontinee TEXT)")

class GESTION_BUDGET:
    
    
    def __init__(self):
        print("l'application de gestion de budget")


    def depense_total(self):
        print("Remplissez la liste de vos dépense:")
        ma_depense = input("quel type de depense voulez-vous ajouter:(loyer, manger, transport, loisir, tontine, factures_courant):\n")
        print("vous voulez ajouter:\n"+str(ma_depense))  
        loyer = int(input("Donnez le montant du loyer:"))
        manger = int(input("Le bilan du mangé:"))
        transport = int(input("Donnez la somme des tarifs du transprt:"))
        loisir = int(input("Donnez la somme effectuée du loisir:"))
        tontine = int(input("La somme versée de la tontine:"))
        factures_courant = int(input("Donnez la somme des factures:"))
        requette = "CREATE TABLE depense_total (id INTEGER PRIMARY KEY AUTOINCREMENT, loyer TEXT, manger TEXT, transport TEXT, loisir TEXT, tontine TEXT, factures_courant TEXT)"
        requette = "INSERT INTO depense_total('loyer', 'manger', 'transport', 'loisir', 'tontine', 'factures_courant') VALUES (?,?,?,?,?,?)"
        cursor.execute(requette, (loyer, manger, transport, loisir, tontine, factures_courant))
        connection.commit()
        print("les dépenses sont ajoutées")
        depense_totale = loyer+manger+transport+loisir+tontine+factures_courant
        print("la somme dépensé" +str(depense_totale)+ "Franc(CFA)")
        if depense_totale > 1000000:
            print("Votre dépense est hyper élevé")
        else:
            print("vous avez bien géré vos dépense")
            
    def revenu_total(self):
        print("Remplissez la liste de vos dépense:")
        mon_revenu = input("quel type de revenu voulez-vous connaitre:(salaire, business, tontine):\n")
        print("vous voulez savoir:\n"+str(mon_revenu))
        salaire = int(input("La somme de votre salaire:"))
        business = int(input("la somme gagnée du business:"))
        tontinee = int(input("La somme gagnée à la tontine:"))
        requette1 = "CREATE TABLE revenu_total(id INTEGER PRIMARY KEY AUTOINCREMENT, salaire TEXT, business TEXT, tontinee TEXT)"
        requette1 = "INSERT INTO revenu_total('salaire', 'business', 'tontinee') VALUES(?,?,?)"
        cursor.execute(requette1,(salaire, business, tontinee))
        connection.commit()
        print("vos revenus ont été consulté")
        revenu_totale = salaire+business+tontinee
        print("La somme des revenus" +str(revenu_totale)+ "Franc(CFA)")
        if revenu_totale > 500000:
            print("Vous pouvez souffler")
        else:
            print("vous avez pratiquement rien gagner")
            
    def la_difference(self):
        depense_totale = ("loyer+Manger+Transport+Loisir+Tontine+Factures_courant")
        revenu_totale = ("Salaire+Business+tontine")
        la_difference = revenu_totale - depense_totale
        print("Donnez la difference effectuée:"+str(la_difference))
        if revenu_totale > depense_totale:
            print("Vous avez bien géré vos transactions")
        elif revenu_totale < depense_totale:
            print("vous n'avez pas bien géré vos transactions")
        else:
            print("On a un égalité de somme entre les deux")
            
    def le_tarif_des_budgets(self):
        choix =""
        print("       Bonjour comment vous allez ?      ")
        print("                                         ")
        print("   A) Remplissez vos dépenses")
        print("   B) Consultez vos revenus")
        print("   C) Vérifier la difference entre la dépense et le revenu")
        print("   0) quitter l'application")
        choix = input("quel est votre désire:\n")
        if choix == "A":
            self.depense_total()
            self.le_tarif_des_budgets()
        elif choix == "B":
            self.revenu_total()
            self.le_tarif_des_budgets()
        elif choix == "C":
            self.la_difference()
            self.le_tarif_des_budgets()
        elif choix == "0":
            print("Quitter")
            exit()
        else:
            print("votre choix n'est pas reconnu" )
            

gestion_budget = GESTION_BUDGET()
gestion_budget.le_tarif_des_budgets()