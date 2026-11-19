# Importer os 
import os
# Importer MongoClient 
from pymongo import MongoClient
# Importer random 
import random
# Importer time 
import time

# Créer NOM_BASE = "jeu_vagues"
NOM_BASE = "jeu_vagues"
# Créer NB_EQUIPE = 3
NB_EQUIPE = 3



# Ouvrir la base
def ouvrir_base():
    global client, base
    # Se connecter au serveur MongoDB local
    client = MongoClient("mongodb://localhost:27017/")
    # Ouvrir la base JEU_VAGUES
    base = client[NOM_BASE]


# Fermer la base
def fermer_base():
    # Fermer la connexion au serveur
    client.close()


# Lire les personnages
def lire_personnages():
    # Récupérer tous les documents de la collection "personnages" et les transformer en liste
    return list(base["personnages"].find({}, {"_id": 0}))


# Lire les scores
def lire_scores():
    # Récupérer tous les documents de la collection "scores" et les transformer en liste
    return list(base["scores"].find({}, {"_id": 0}))


# Enregistrer la vague max 
def enregistrer_vague_max(vague):
    # Prendre la date et l'heure du moment (exemple 2026-11-18 14:30)
    maintenant = time.strftime("%Y-%m-%d %H:%M")
    # Ajouter un document {vague, date} dans la collection "scores"
    base["scores"].insert_one({"vague": vague, "date": maintenant})


# Effacer l'écran
def effacer_ecran():
    # Si le système est Windows : exécuter cls, sinon exécuter clear
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


# Afficher titre (texte)
def afficher_titre(texte):
    # Calculer la longueur du texte + 4
    longueur = len(texte) + 4
    # Afficher une ligne de "=" 
    print("=" * longueur)
    # Afficher "| jeu des vagues |"
    print("| " + texte + " |")
    # Afficher une ligne de "=" 
    print("=" * longueur)


# Choix est valide (choix, minimum, maximum)
def choix_est_valide(choix, minimum, maximum):
    # Si le choix n'est pas isdigit() : retourner False
    if not choix.isdigit():
        return False
    # Convertir le choix en entier
    nombre = int(choix)
    # Si le choix est inférieur au minimum ou supérieur au maximum : retourner False
    if nombre < minimum or nombre > maximum:
        return False
    # Retourner True
    return True


# Afficher Menu 
def afficher_menu(options, minimum):
    # Pour chaque option dans enumerate: afficher (i). (option)
    for i, option in enumerate(options, start=1):
        print(str(i) + ". " + option)
    # Si le minimum est 0 : afficher "0. annuler"
    if minimum == 0:
        print("0. annuler")


# Récupérer un choix valide parmi les options
def recuperer_choix(options, minimum=1):
    # Tant que infini
    while True:
        # Afficher les options numérotées
        afficher_menu(options, minimum)
        # Demander un choix à l'utilisateur
        saisie = input("Ton choix : ")
        # Si le choix est valide : retourner le choix valide 
        if choix_est_valide(saisie, minimum, len(options)):
            return int(saisie)


# Menu Principal
def menu_principal():
    # Effacer l'écran
    effacer_ecran()
    # Afficher titre "JEU DES VAGUES"
    afficher_titre("JEU DES VAGUES")
    # Récupérer un choix valide parmi ["jouer", "score", "quitter"]
    return recuperer_choix(["jouer", "score", "quitter"])


# Sélectionner l'équipe
def selectionner_equipe(personnages):
    # Copier la liste des personnages dans "disponibles"
    # (la copie sert à retirer des personnages de l'affichage sans toucher à la base)
    disponibles = [dict(p) for p in personnages]
    # Créer une équipe vide
    equipe = []
    # Tant que l'équipe a moins de 3 personnages
    while len(equipe) < NB_EQUIPE:
        # Effacer l'écran
        effacer_ecran()
        # Afficher "Choisis tes personnages (n sur 3)"
        print("Choisis tes personnages (" + str(len(equipe)) + " sur " + str(NB_EQUIPE) + ")")
        # Récupérer un choix valide parmi 0 et le nombre de disponibles
        choix = recuperer_choix([p["nom"] + "  PV " + str(p["pv"]) + "  ATT " + str(p["attaque"]) for p in disponibles], 0)
        # Si le choix est 0 : retourner rien (annulation)
        if choix == 0:
            return None
        # Afficher l'équipe actuelle
        print("Équipe actuelle : " + ", ".join(p["nom"] for p in equipe))
        # Retirer le personnage choisi de "disponibles"
        choisi = disponibles.pop(choix - 1)
        # Ajouter ce personnage à l'équipe
        equipe.append(choisi)
        # Attendre une seconde
        time.sleep(1)
    # Retourner l'équipe
    return equipe


# Sous-menu Jouer
def sous_menu_jouer():
    # Effacer l'écran
    effacer_ecran()
    # Afficher titre "JOUER"
    afficher_titre("JOUER")
    # Charger la liste des personnages depuis la base
    personnages = lire_personnages()
    # Sélectionner l'équipe
    equipe = selectionner_equipe(personnages)
    # Si l'équipe est annulée : retourner au menu
    if equipe is None:
        return
    # Lancer la partie avec l'équipe
    lancer_partie(equipe)


# Sous-menu Score
def sous_menu_score():
    # Effacer l'écran
    effacer_ecran()
    # Afficher titre "SCORES"
    afficher_titre("SCORES")
    # Charger tous les scores depuis la base
    scores = lire_scores()
    # Si la liste est vide : afficher "aucun score pour l'instant"
    if scores == []:
        print("aucun score pour l'instant")
    # Sinon : trier du plus grand au plus petit et afficher chaque vague et date
    else:
        for score in sorted(scores, key=lambda s: s["vague"], reverse=True):
            print("Vague " + str(score["vague"]) + "  -  " + score["date"])
    # Récupérer un choix valide parmi ["retour au menu"]
    recuperer_choix(["retour au menu"])


# Sous-menu Quitter
def sous_menu_quitter():
    # Effacer l'écran
    effacer_ecran()
    # Afficher "Veux-tu vraiment quitter ?"
    print("Veux-tu vraiment quitter ?")
    # Récupérer un choix valide parmi ["oui", "non"]
    # Si oui : retourner True (on quitte)
    if recuperer_choix(["oui", "non"]) == 1:
        return True
    # Sinon : retourner False (on reste dans le menu)
    return False


# Lister les vivants 
def vivants(groupe):
    # Créer une liste vide "liste_vivants"
    liste_vivants = []
    # Pour chaque personnage du groupe
    for personnage in groupe:
        # Si ses PV sont plus grands que 0 : l'ajouter à "liste_vivants"
        if personnage["pv"] > 0:
            liste_vivants.append(personnage)
    # Retourner "liste_vivants"
    return liste_vivants


# Attaquer (attaquant, liste des cibles)
def attaquer(attaquant, cibles):
    # Choisir une cible au hasard dans la liste des cibles vivantes
    cible = random.choice(cibles)
    # Dégâts = attaque de l'attaquant
    degats = attaquant["attaque"]
    # Retirer les dégâts aux PV de la cible
    cible["pv"] = cible["pv"] - degats
    # Afficher "attaquant attaque cible : dégâts, il reste PV" (les PV ne descendent jamais sous 0)
    print(attaquant["nom"] + " attaque " + cible["nom"] + " : " + str(degats) + " dégâts, il reste " + str(max(0, cible["pv"])) + " PV")
    # Si les PV de la cible sont 0 ou moins : afficher "cible est morte"
    if cible["pv"] <= 0:
        print(cible["nom"] + " est mort.")
    # Attendre une seconde
    time.sleep(1)


# Combat tour par tour (équipe du joueur, ennemi)
def combat(equipe, ennemi):
    # Tant que l'équipe est en vie et l'ennemi est en vie
    while vivants(equipe) != [] and ennemi["pv"] > 0:
        # Pour chaque personnage vivant du joueur
        for personnage in vivants(equipe):
            # Si l'ennemi n'a plus de PV : sortir de la boucle
            if ennemi["pv"] <= 0:
                break
            # Le personnage attaque l'ennemi
            attaquer(personnage, [ennemi])
        # Si l'ennemi a encore des PV
        if ennemi["pv"] > 0:
            # L'ennemi attaque un personnage vivant du joueur
            attaquer(ennemi, vivants(equipe))
    # Retourner True si le joueur a encore un vivant, sinon False
    return len(vivants(equipe)) > 0


# Générer l'ennemi d'une vague (numéro de vague)
def generer_ennemi(vague):
    # Nom = "Ennemi" + vague
    nom = "Ennemi " + str(vague)
    # PV = 20 + vague * 5
    pv = 20 + vague * 5
    # Attaque = 5 + vague
    attaque = 5 + vague
    # Retourner l'ennemi (nom, pv, attaque)
    return {"nom": nom, "pv": pv, "attaque": attaque}


# Lancer la partie (équipe)
def lancer_partie(equipe):
    # Vague = 1
    vague = 1
    # Tant que le joueur n'a pas perdu
    while True:
        # Effacer l'écran
        effacer_ecran()
        # Afficher "VAGUE" + vague
        print("VAGUE " + str(vague))
        # Générer l'ennemi de la vague
        ennemi = generer_ennemi(vague)
        # Lancer le combat tour par tour (équipe, ennemi)
        # Si le joueur a gagné
        if combat(equipe, ennemi):
            # Afficher "Vague gagnée"
            print("Vague " + str(vague) + " gagnée !")
            # Vague = vague + 1
            vague = vague + 1
            time.sleep(2)
        # Sinon : sortir de la boucle
        else:
            break
    # Afficher "Défaite à la vague" + vague
    print("Défaite à la vague " + str(vague))
    # Meilleure = la meilleure vague dans les scores (ou 0 si vide)
    meilleure = max([s["vague"] for s in lire_scores()], default=0)
    # Si vague > meilleure : enregistrer la vague et afficher "Nouveau record !"
    if vague > meilleure:
        enregistrer_vague_max(vague)
        print("Nouveau record !")
    # Sinon : afficher "Pas de nouveau record, record actuel : meilleure"
    else:
        print("Pas de nouveau record, record actuel : " + str(meilleure))
    # Attendre Entrée pour revenir au menu
    input("Entrée pour revenir au menu...")


# Boucle principale
def main():
    # Ouvrir la base au démarrage
    ouvrir_base()
    # Tant que le programme tourne
    while True:
        # Afficher le menu principal et récupérer le choix
        choix = menu_principal()
        # Si 1 : aller au sous-menu Jouer
        if choix == 1:
            sous_menu_jouer()
        # Si 2 : aller au sous-menu Score
        elif choix == 2:
            sous_menu_score()
        # Si 3 : aller au sous-menu Quitter, et sortir de la boucle si l'utilisateur confirme
        elif choix == 3:
            if sous_menu_quitter():
                break
    # Fermer la base (à la fin du programme, avant "À bientôt !")
    fermer_base()
    # Afficher "À bientôt !" 
    print("À bientôt !")


if __name__ == "__main__":
    main()