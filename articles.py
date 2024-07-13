import json
import re

# Fichiers de données
ARTICLES_FILE = 'articles.json'
VENTES_FILE = 'ventes.json'
CLIENTS_FILE = 'clients.json'

# Liste globale des articles, des ventes et des clients
articles = []
ventes = []
clients = []

def initialiser_donnees_vide():
    global articles, ventes, clients
    articles = []
    ventes = []
    clients = []

def ajoutArticle():
    while True:
        id_article = input("ID de l'article: ").strip()
        if not id_article:
            print("L'ID de l'article ne peut pas être vide.")
        elif not re.match(r'^[a-zA-Z0-9]', id_article):
            print("L'ID de l'article doit commencer par une lettre ou un chiffre.")
        elif any(article['id'] == id_article for article in articles):
            print("Un article avec cet ID existe déjà.")
        else:
            break

    while True:
        nom = input("Nom de l'article: ").strip()
        if not nom:
            print("Le nom de l'article ne peut pas être vide.")
        elif not re.match(r'^[a-zA-Z]', nom):
            print("Le nom de l'article doit commencer par une lettre.")
        else:
            break

    while True:
        try:
            prix = float(input("Prix de l'article: "))
            if prix > 0:
                break
            else:
                print("Le prix doit être un nombre positif.")
        except ValueError:
            print("Le prix doit être un nombre valide.")

    while True:
        try:
            quantite = int(input("Quantité de l'article: "))
            if quantite >= 0:
                break
            else:
                print("La quantité doit être un nombre positif ou zéro.")
        except ValueError:
            print("La quantité doit être un nombre valide.")

    article = {
        'id': id_article,
        'nom': nom,
        'prix': prix,
        'quantite': quantite
    }
    articles.append(article)
    print(f"Article {nom} ajouté avec succès!")

def afficherArticles():
    if not articles:
        print("Aucun article disponible.")
    else:
        for article in articles:
            print(f"ID: {article['id']}, Nom: {article['nom']}, Prix: {article['prix']}, Quantité: {article['quantite']}")

def sauvegarderArticlesEnJSON():
    with open(ARTICLES_FILE, 'w') as f:
        json.dump(articles, f)
    print(f"Articles sauvegardés dans {ARTICLES_FILE}")

def sauvegarderVentesEnJSON():
    with open(VENTES_FILE, 'w') as f:
        json.dump(ventes, f)
    print(f"Ventes sauvegardées dans {VENTES_FILE}")

def sauvegarderClientsEnJSON():
    with open(CLIENTS_FILE, 'w') as f:
        json.dump(clients, f)
    print(f"Clients sauvegardés dans {CLIENTS_FILE}")

def rechercher_produit_par_nom(nom_produit):
    for article in articles:
        if article['nom'].lower() == nom_produit.lower():
            return article
    return None

def rechercher_produit_par_id(id_produit):
    for article in articles:
        if article['id'] == id_produit:
            return article
    return None

def rechercher_client_par_nom(nom_client):
    for client in clients:
        if client['nom'].lower() == nom_client.lower():
            return client
    return None

def afficher_details_produit(produit):
    if produit:
        print(f"ID: {produit['id']}, Nom: {produit['nom']}, Prix: {produit['prix']}, Quantité: {produit['quantite']}")
    else:
        print("Produit non trouvé")

def enregistrer_vente():
    while True:
        nom_client = input("Nom du client: ").strip()
        if not nom_client:
            print("Le nom du client ne peut pas être vide.")
        elif not re.match(r'^[a-zA-Z]', nom_client):
            print("Le nom du client doit commencer par une lettre.")
        else:
            break

    client = rechercher_client_par_nom(nom_client)
    if not client:
        client = {'nom': nom_client, 'ventes': []}
        clients.append(client)

    while True:
        id_produit = input("ID du produit vendu: ").strip()
        if not id_produit:
            print("L'ID du produit ne peut pas être vide.")
        else:
            produit = rechercher_produit_par_id(id_produit)
            if produit:
                break
            else:
                print("Produit non trouvé. Vente non enregistrée.")

    while True:
        try:
            quantite = int(input("Quantité vendue: "))
            if quantite > 0:
                if quantite <= produit['quantite']:
                    produit['quantite'] -= quantite
                    break
                else:
                    print(f"La quantité en stock est insuffisante. Quantité disponible : {produit['quantite']}")
            else:
                print("La quantité doit être un nombre positif.")
        except ValueError:
            print("La quantité doit être un nombre valide.")

    vente = {
        'id': id_produit,
        'nom': produit['nom'],
        'quantite': quantite,
        'prix_total': produit['prix'] * quantite
    }
    client['ventes'].append(vente)
    ventes.append(vente)
    print(f"Vente de {quantite} {produit['nom']} enregistrée pour le client {nom_client}.")

def afficher_ventes():
    if not ventes:
        print("Aucune vente enregistrée.")
    else:
        for vente in ventes:
            print(f"ID: {vente['id']}, Produit: {vente['nom']}, Quantité: {vente['quantite']}, Prix total: {vente['prix_total']}")

def ventes_par_client():
    if not clients:
        print("Aucun client enregistré.")
    else:
        for client in clients:
            print(f"Client: {client['nom']}")
            if not client['ventes']:
                print("  Aucune vente enregistrée pour ce client.")
            else:
                for vente in client['ventes']:
                    print(f"  Produit: {vente['nom']}, Quantité: {vente['quantite']}, Prix total: {vente['prix_total']}")

def generer_rapport_de_ventes():
    total_ventes = 0
    for vente in ventes:
        total_ventes += vente['prix_total']
    print(f"Nombre total de ventes: {len(ventes)}")
    print(f"Montant total des ventes: {total_ventes}")

def charger_donnees():
    global articles, ventes, clients
    try:
        with open(ARTICLES_FILE, 'r') as f:
            articles = json.load(f)
        print(f"Articles chargés depuis {ARTICLES_FILE}")
    except FileNotFoundError:
        print(f"{ARTICLES_FILE} n'existe pas. Initialisation d'une liste vide.")
        initialiser_donnees_vide()
    
    try:
        with open(VENTES_FILE, 'r') as f:
            ventes = json.load(f)
        print(f"Ventes chargées depuis {VENTES_FILE}")
    except FileNotFoundError:
        print(f"{VENTES_FILE} n'existe pas. Initialisation d'une liste vide.")
        initialiser_donnees_vide()
    
    try:
        with open(CLIENTS_FILE, 'r') as f:
            clients = json.load(f)
        print(f"Clients chargés depuis {CLIENTS_FILE}")
    except FileNotFoundError:
        print(f"{CLIENTS_FILE} n'existe pas. Initialisation d'une liste vide.")
        initialiser_donnees_vide()

    sauvegarderArticlesEnJSON()
    sauvegarderVentesEnJSON()
    sauvegarderClientsEnJSON()
