# Afficher Menu
# Récupérer un choix valide parmi les options
# tant que infini
#     afficher les options numérotées
#         pour chaque option dans enumerate(options, start=1)
#             afficher (i). (option)
#     demander un choix à l'utilisateur
#     si le choix est valide
#         retourner le choix valide
#     afficher un message d'erreur

# choix est valide
#     si le choix n'est pas isdigit()
#         retourner False
#     convertir le choix en entier
#     si le choix est inférieur au minimum ou supérieur au maximum
#         retourner False
#     retourner True

# Effacer l'écran
#     si le système est Windows
#         exécuter cls
#     sinon
#         exécuter clear


# Menu Principal
# Effacer l'écran
# Récupérer un choix valide parmi ["jouer", "score", "quitter"]
# retourner le choix

# Sous-menu Jouer
# Effacer l'écran
# Afficher Titre "JOUER"
# Charger la liste des personnages depuis la base
# si la base est inaccessible
#     afficher un message d'erreur
#     attendre Entrée
#     retourner au menu principal
# Sélectionner l'équipe
# si l'équipe est annulée
#     retourner au menu principal
# Lancer la partie avec l'équipe

# Sélectionner l'équipe
# Copier la liste des personnages dans "disponibles"
# Créer une équipe vide
# tant que l'équipe a moins de 3 personnages
#     Effacer l'écran
#     afficher "Choisis tes personnages (n sur 3)"
#     pour chaque personnage dans disponibles avec enumerate(start=1)
#         afficher (i). nom, PV, attaque
#     récupérer un choix valide parmi 0 et le nombre de disponibles
#     si le choix est 0
#         retourner rien (annulation)
#     retirer le personnage choisi de "disponibles" (il disparaît de l'affichage)
#     ajouter ce personnage à l'équipe
#     afficher "nom ajouté à ton équipe"
#     attendre une seconde
# retourner l'équipe

# Sous-menu Score
# Effacer l'écran
# Afficher Titre "SCORES"
# Charger tous les scores depuis la base
# si la base est inaccessible
#     afficher un message d'erreur
# si la liste est vide
#     afficher "aucun score pour l'instant"
# sinon
#     trier la liste du plus grand au plus petit
#     pour chaque score dans la liste
#         afficher la vague et la date
# afficher "1. retour au menu"
# récupérer un choix valide parmi [1]
# retourner au menu principal


#lancer la partie
#   