import articles

def menu_principal():
    print("1. Ajouter produit")
    print("2. Afficher produits")
    print("3. Rechercher produit")
    print("4. Enregistrer vente")
    print("5. Afficher ventes")
    print("6. Ventes par client")
    print("7. Générer rapport de ventes")
    print("8. Charger données")
    print("9. Quitter")
    return input("Choisissez une option: ")

def main():
    # Charger les données au démarrage
    articles.charger_donnees()
    
    while True:
        choix = menu_principal()
        if choix == '1':
            articles.ajoutArticle()
        elif choix == '2':
            articles.afficherArticles()
        elif choix == '3':
            nom_produit = input("Entrez le nom du produit à rechercher : ").strip()
            produit_trouve = articles.rechercher_produit_par_nom(nom_produit)
            articles.afficher_details_produit(produit_trouve)
        elif choix == '4':
            articles.enregistrer_vente()
        elif choix == '5':
            articles.afficher_ventes()
        elif choix == '6':
            articles.ventes_par_client()
        elif choix == '7':
            articles.generer_rapport_de_ventes()
        elif choix == '8':
            articles.charger_donnees()
        elif choix == '9':
            articles.sau
