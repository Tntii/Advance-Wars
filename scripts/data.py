lang = "Francais"

trad = {"Francais": {"BACK": "RETOUR", "LANGUAGE": "LANGUE: francais", "QUIT": "QUITTER", "PLAY": "JOUER",
                     "SETTINGS": "PARAMETRE", "soldier": "soldat"},
        "English": {"LANGUAGE": "LANGUAGE: english"}}

main_volume = 100

troupe_stats = {
    "soldier": {
        "pv": 10, "attack": 5, "r_deplacement": 3, "r_attack": 1, "animation":
            {"idle": (((3, 104), (20, 104), (37, 104)),
                      ((392, 104), (409, 104), (426, 104)))
             }
    }
}

build_stats = {
    "HQ": {
        "nb_steps": 3,
        "animation":(
            ((3, 1034), (175, 1034)),
            ((3, 1067), (175, 1067)),
            ()
        )
    },
    "city": {
        "nb_steps": 2,
        "animation": (
            (),(),()
        ),
        }
    }

command = {"forward": (122, "z"),
           "backward": (115, "s"),
           "left": (113, "q"),
           "right": (100, "d")}
