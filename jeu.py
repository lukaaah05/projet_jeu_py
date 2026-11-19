# Imports et constantes
# Importer os 
# Importer MongoClient 
# Importer random 
# Importer time 
# Créer NOM_BASE = "jeu_vagues"
# Créer NB_EQUIPE = 3



# Ouvrir la base
# Se connecter au serveur MongoDB local
# Ouvrir la base JEU_VAGUES


# Fermer la base
# Fermer la connexion au serveur


# Lire les personnages
# Récupérer tous les documents de la collection "personnages" 
# Transformer le résultat en liste


# Lire les scores
# Récupérer tous les documents de la collection "scores" 
# Transformer le résultat en liste


# Enregistrer la vague max 
# Prendre la date et l'heure du moment (exemple 2026-11-18 14:30)
# Ajouter un document {vague, date} dans la collection "scores"


# Effacer l'écran


# Afficher titre 

# Afficher une ligne de "=" 
# Afficher "| jeu des vaues |"
# Afficher une ligne de "=" 


# Choix est valide (choix, minimum, maximum)
# Si le choix n'est pas isdigit() : retourner False
# Convertir le choix en entier
# Si le choix est inférieur au minimum ou supérieur au maximum : retourner False
# Retourner True


# Afficher Menu 
# Pour chaque option dans enumerate: afficher (i). (option)
# Si le minimum est 0 : afficher "0. annuler"


# Récupérer un choix valide parmi les options
# Tant que infini
#     Afficher les options numérotées
#     Demander un choix à l'utilisateur
#     Si le choix est valide : retourner le choix valide (en nombre entier)
#     Afficher un message d'erreur


# Menu Principal
# Effacer l'écran
# Afficher titre "JEU DES VAGUES"
# Récupérer un choix valide parmi ["jouer", "score", "quitter"]


# Sélectionner l'équipe
# Copier la liste des personnages dans "disponibles"
# (la copie sert à retirer des personnages de l'affichage sans toucher à la base)
# Créer une équipe vide
# Tant que l'équipe a moins de 3 personnages
#     Effacer l'écran
#     Afficher "Choisis tes personnages (n sur 3)"
#     Récupérer un choix valide parmi 0 et le nombre de disponibles
#     Si le choix est 0 : retourner rien (annulation)
#     Retirer le personnage choisi de "disponibles"
#     Ajouter ce personnage à l'équipe
#     Attendre une seconde
# Retourner l'équipe


# Sous-menu Jouer
# Effacer l'écran
# Afficher titre "JOUER"
# Charger la liste des personnages depuis la base
# Si la base est inaccessible : afficher un message d'erreur, attendre Entrée, retourner au menu
# Sélectionner l'équipe
# Si l'équipe est annulée : retourner au menu
# Lancer la partie avec l'équipe


# Sous-menu Score
# Effacer l'écran
# Afficher titre "SCORES"
# Charger tous les scores depuis la base
# Si la liste est vide : afficher "aucun score pour l'instant"
# Sinon : trier du plus grand au plus petit et afficher chaque vague et date
# Récupérer un choix valide parmi ["retour au menu"]


# Sous-menu Quitter
# Effacer l'écran
# Afficher "Veux-tu vraiment quitter ?"
# Récupérer un choix valide parmi ["oui", "non"]
# Si oui : retourner True (on quitte)
# Sinon : retourner False (on reste dans le menu)


# Lister les vivants 
# Créer une liste vide "liste_vivants"
# Pour chaque personnage du groupe
#     Si ses PV sont plus grands que 0 : l'ajouter à "liste_vivants"
# Retourner "liste_vivants"


# Attaquer 
# Choisir une cible au hasard dans la liste des cibles vivantes
# Dégâts = attaque de l'attaquant
# Retirer les dégâts aux PV de la cible
# Afficher "attaquant attaque cible : dégâts, il reste PV" (les PV ne descendent jamais sous 0)
# Si les PV de la cible sont 0 ou moins : afficher "cible est morte"

# Combat tour par tour (équipe du joueur, ennemi)
# Tant que le joueur a au moins un vivant et l'ennemi a encore des PV
#     Pour chaque personnage vivant du joueur
#         Si l'ennemi n'a plus de PV : sortir de la boucle
#         Le personnage attaque l'ennemi
#     Si l'ennemi a encore des PV et qu'il reste un personnage vivant
#         L'ennemi attaque un personnage vivant du joueur
# Retourner True si le joueur a encore un vivant, sinon False


# Générer l'ennemi d'une vague (numéro de vague)
# Nom = "Ennemi" + vague
# PV = 20 + vague * 5
# Attaque = 5 + vague
# Retourner l'ennemi (nom, pv, attaque)


# Lancer la partie (équipe)
# Vague = 1
# Tant que le joueur n'a pas perdu
#     Effacer l'écran
#     Afficher "VAGUE" + vague
#     Générer l'ennemi de la vague
#     Lancer le combat tour par tour (équipe, ennemi)
#     Si le joueur a gagné
#         Afficher "Vague gagnée"
#         Vague = vague + 1
#         Attendre deux secondes
#     Sinon : sortir de la boucle
# Afficher "Défaite à la vague" + vague
# Meilleure = la meilleure vague dans les scores (ou 0 si vide)
# Si vague > meilleure
#     Enregistrer la vague
#     Afficher "Nouveau record !"
# Sinon
#     Afficher "Pas de nouveau record, record actuel : meilleure"
# Attendre Entrée pour revenir au menu


# Boucle principale
# Ouvrir la base au démarrage
# Tant que le programme tourne
#     Afficher le menu principal et récupérer le choix
#     Si 1 : aller au sous-menu Jouer
#     Si 2 : aller au sous-menu Score
#     Si 3 : aller au sous-menu Quitter, et sortir de la boucle si l'utilisateur confirme
# Fermer la base (à la fin du programme, avant "À bientôt !")
# Afficher "À bientôt !"