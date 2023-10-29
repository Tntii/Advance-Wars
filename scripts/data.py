lang = "Francais"

trad = {"Francais": {"BACK": "RETOUR", "LANGUAGE": "LANGUE: francais", "QUIT": "QUITTER", "PLAY": "JOUER", "SETTINGS": "PARAMETRE", "soldier": "soldat"},
        "English": {"LANGUAGE": "LANGUAGE: english"}}

main_volume = 100

'''nom de la troupe: (0:PV, 1:degat, 2:rayon de déplacement, 3:rayon ou il ne peut pas attaquer, rayon d'attaque'''
troupe_stats = {"soldier": (10, 5, 3, 0, 1, "terrestre", ("terrestre"),
                            {"0":((3, 104), (20, 104), (37, 104)),
                             "1": ((392, 104), (409, 104), (426, 104))})}

command = {"forward": (122, "z"),
           "backward": (115, "s"),
           "left": (113, "q"),
           "right": (100, "d")}