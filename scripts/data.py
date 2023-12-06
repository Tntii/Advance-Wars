import pyxel

current_map = "The Bridge"

lang = "Francais"

trad = {"Francais": {"BACK": "RETOUR", "LANGUAGE": "LANGUE: francais", "QUIT": "QUITTER", "PLAY": "JOUER",
                     "SETTINGS": "PARAMETRE", "Key": "Controle", "infantry": "soldat", "heavy infantry": "soldat lourd", "mortar": "mortier",
                     "city": "ville", "hp": "pv", "col lvl": "niv col", "damage": "degats", "reach": "porte",
                     "0": "Les rouges ont gagnes !", "1": "Les bleus ont gagnes !", "HQ": "QG",
                     "up": "haut", "down": "bas", "right": "droite", "left": "gauche", "End": "Fin", "Give up": "Abandonne", "Continue": "Continuer", "Back to menue": "Retour au menu"},
        "English": {"LANGUAGE": "LANGUAGE: english", "0": "Red team won ! ", "1": "Blue team won!", "Key": "Control"},
        }

main_volume = "ON"

troupe_stats = {
    "infantry": {
        "pv": 10, "attack": 5, "r_deplacement": 3, "r_attack": 1, "r_cant_attack": 0, "collide lvl": 4,
        "animation": {
            "idle": (((3, 104), (20, 104), (37, 104)),
                     ((392, 104), (409, 104), (426, 104))),
            "have move": (((339, 104), (356, 104), (373, 104)),
                          ((728, 104), (745, 104), (762, 104)))
             }},
    "heavy infantry": {
        "pv": 12, "attack": 8, "r_deplacement": 2, "r_attack": 1, "r_cant_attack": 0, "collide lvl": 3,
        "animation": {
            "idle": (((3, 199), (20, 199), (37, 199)),
                    ((392, 199), (409, 199), (426, 199))),
            "have move": (((339, 199), (356, 199), (373, 199)),
                          ((728, 199), (745, 199), (762, 199)))
            }},
    "jeep": {
        "pv": 15, "attack": 9, "r_deplacement": 10, "r_attack": 1, "r_cant_attack": 0, "collide lvl": 2,
        "animation": {
            "idle": (((3, 294), (20, 294), (37, 294)),
                    ((392, 294), (409, 294), (426, 294))),
            "have move": (((339, 294), (356, 294), (373, 294)),
                          ((728, 294), (745, 294), (762, 294)))
            }
        },
    "tank": {
        "pv": 20, "attack": 11, "r_deplacement": 7, "r_attack": 1, "r_cant_attack": 0, "collide lvl": 1,
        "animation": {
            "idle": (((3, 313), (20, 313), (37, 313)),
                     ((392, 313), (409, 313), (426, 313))),
            "have move": (((339, 313), (356, 313), (373, 313)),
                          ((728, 313), (745, 313), (762, 313)))
        }
    },

    "mega tank": {
        "pv": 25, "attack": 15, "r_deplacement": 5, "r_attack": 1, "r_cant_attack": 0, "collide lvl": 0,
        "animation": {
            "idle": (((3, 332), (20, 332), (37, 332)),
                     ((392, 332), (409, 332), (426, 332))),
            "have move": (((339, 332), (356, 332), (373, 332)),
                          ((728, 332), (745, 332), (762, 332)))
        }},
    "mortar": {
        "pv": 6, "attack": 11, "r_deplacement": 3, "r_attack": 6, "r_cant_attack": 3, "collide lvl": 0,
        "animation": {
            "idle": (((3, 408), (20, 408), (37, 408)),
                    ((392, 408), (409, 408), (426, 408))),
            "have move": (((339, 408), (356, 408), (373, 408)),
                            ((728, 408), (745, 408), (762, 408)))}
    }
}

build_stats = {
    "HQ": {
        "nb_steps": 3,
        "animation":(
            ((3, 1034), (175, 1034)),
            ((3, 1067), (175, 1067)),
            ((3, 1212), (3, 1212))
        )
    },
    "city": {
        "nb_steps": 2,
        "animation": (
            ((88, 1034), (260, 1034)),
            ((88, 1067), (260, 1067)),
            ((88, 1212), (88, 1212))
        )
        }
    }

command = {"up": (122, "z"),
           "down": (115, "s"),
           "left": (113, "q"),
           "right": (100, "d"),
           "hide stats": (104, "h")}

texture = {}

music = [

]

map = {
        "Brace Range": {"collision": [
                                        [],
                                        [
                                            (0, 0),
                                            (1, 1),
                                            (7, 1),
                                            (8, 2),
                                            (14, 9),
                                            (13, 8),
                                            (6, 8),
                                            (7, 9),
                                        ],
                                        [
                                            (4, 3),
                                            (5, 3),
                                            (4, 6),
                                            (5, 6),
                                            (9, 6),
                                            (10, 6),
                                            (9, 0),
                                            (10, 0),
                                        ],
                                        [
                                            (0, 5),
                                            (2, 5),
                                            (3, 5),
                                            (4, 5),
                                            (5, 5),
                                            (6, 5),
                                            (8, 5),
                                            (9, 5),
                                            (10, 5),
                                            (11, 5),
                                            (12, 5),
                                            (13, 5),
                                            (14, 5),
                                        ],
                                        [
                                            (4, 7),
                                            (4, 8),
                                            (4, 9),
                                            (5, 7),
                                            (5, 8),
                                            (5, 9),
                                            (4, 4),
                                            (5, 4),
                                            (10, 1),
                                            (10, 2),
                                            (10, 3),
                                            (10, 4),
                                            (9, 1),
                                            (9, 2),
                                            (9, 3),
                                            (9, 4),
                                        ],
                                        []
                                    ],
                        "troupe": [
                                        [
                                            ["mortar", 0, 96, 10, True],
                                            ["tank", 16, 80, 10, True],
                                            ["infantry", 16, 96, 10, True],
                                            ["infantry", 32, 96, 10, True],
                                            ["heavy infantry", 48, 96, 10, True],
                                            ["heavy infantry", 16, 112, 10, True],
                                            ["jeep", 16, 128, 10, True]

                                        ],
                                        [
                                            ["mortar", 224, 32, 10, True],
                                            ["tank", 208, 48, 10, True],
                                            ["infantry", 192, 16, 10, True],
                                            ["infantry", 208, 32, 10, True],
                                            ["heavy infantry", 176, 16, 10, True],
                                            ["heavy infantry", 192, 32, 10, True],
                                            ["jeep", 208, 16, 10, True]
                                        ]
                        ],
                        "build": [
                                [
                                    [0, 128, 0, 0],
                                    [224, 16, 1, 0]
                                ],
                                [
                                    [48, 128, 2, 0],
                                    [64, 16, 2, 0],
                                    [80, 16, 2, 0],
                                    [176, 32, 2, 0],
                                    [144, 144, 2, 0],
                                    [160, 144, 2, 0]

                                ]
                            ],
                        "src": (240, 160, "../map/braceRange.png", "map")},

        "River Range": {"collision": [
                                        [],
                                        [
                                            (0, 0),
                                            (1, 0),
                                            (7, 0),
                                            (5, 8),
                                            (11, 8)
                                        ] + [(3 + i, 9) for i in range(9)],
                                        [
                                            (3, 2),
                                            (4, 2),
                                            (5, 2),
                                            (6, 2),
                                            (7, 2),
                                            (8, 2),
                                            (9, 2),
                                            (10, 2),
                                            (11, 2),
                                            (7, 4),
                                            (8, 4),
                                            (9, 4),
                                            (6, 8),
                                            (10, 8)
                                        ],
                                        [
                                            (i, 3) for i in range(15) if i not in (2, 12)],
                                        [
                                            (0, 2),
                                            (1, 2),
                                            (14, 2),
                                            (13, 2),
                                            (7, 7),
                                            (8, 7),
                                            (9, 7),
                                            (7, 8),
                                            (8, 8),
                                            (9, 8),
                                            (8, 6),
                                            (8, 5)
                                        ],
                                        []
                                    ],
                        "troupe": [
                                    [
                                        ["tank", 32, 64, 10, True],
                                        ["jeep", 16, 64, 10, True],
                                        ["mortar", 48, 64, 10, True],
                                        ["infantry", 32, 80, 10, True],
                                        ["infantry", 16, 80, 10, True],
                                        ["infantry", 48, 80, 10, True],
                                        ["heavy infantry", 32, 96, 10, True]
                                    ],

                                    [
                                        ["tank", 192, 64, 10, True],
                                        ["jeep", 208, 64, 10, True],
                                        ["mortar", 176, 64, 10, True],
                                        ["infantry", 176, 80, 10, True],
                                        ["infantry", 208, 80, 10, True],
                                        ["infantry", 192, 80, 10, True],
                                        ["heavy infantry", 192, 96, 10, True]
                                    ]
                                ],
                        "build": [
                                [
                                    [0, 80, 0, 0],
                                    [224, 80, 1, 0]
                                ],
                                [
                                    [16, 144, 0, 0],
                                    [32, 144, 0, 0],
                                    [80, 112, 0, 0],
                                    [96, 112, 0, 0],
                                    [208, 144, 1, 0],
                                    [192, 144, 1, 0],
                                    [160, 112, 1, 0],
                                    [176, 112, 1, 0],
                                ] + [[16*(6 + i), 16, 2, 0] for i in range(3)]
                            ],
                        "src": (240, 160, "../map/riverRange.png", "map")},

        "The Bridge": {
                        "collision": [
                                        [],
                                        [
                                            (1, 1),
                                            (0, 2),
                                            (1, 2),
                                            (2, 2),
                                            (0, 3),
                                            (1, 3),
                                            (2, 3),
                                            (1, 4),
                                            (2, 4),
                                            (1, 18),
                                            (2, 18),
                                            (3, 18),
                                            (0, 17),
                                            (1, 17),
                                            (2, 17),
                                            (3, 17),
                                            (1, 16),
                                            (2, 16),
                                            (1, 15),
                                            (12, 1),
                                            (12, 2),
                                            (13, 2),
                                            (14, 2),
                                            (15, 2),
                                            (13, 3),
                                            (14, 3),
                                            (14, 4),
                                            (15, 4),
                                            (14, 5),
                                            (15, 6),
                                            (19, 0),
                                            (19, 1),
                                            (20, 1),
                                            (18, 2),
                                            (19, 2),
                                            (19, 3),
                                            (20, 3),
                                            (18, 3),
                                            (12, 13),
                                            (13, 13),
                                            (12, 14),
                                            (11, 15),
                                            (10, 16),
                                            (11, 16),
                                            (11, 17),
                                            (12, 17),
                                            (10, 18),
                                            (11, 18),
                                            (15, 16),
                                            (16, 16),
                                            (14, 18),
                                            (16, 18),
                                            (15, 19),
                                            (16, 19),
                                            (17, 19),
                                            (15, 17)

                                        ],
                                        [
                                            (29, y) for y in range(1, 19) if y not in (9, 10)
                                        ] + [(28, 11), (27, 13), (26, 13)],
                                        [
                                        ],
                                        [
                                            (x, y) for y in range(1, 19) for x in range(26, 30) if (y not in range(7, 13) or x not in range(26, 28)) and (y != 10 or x not in range(28, 30)) and (x, y) not in [(29, y) for y in range(1, 19) if y not in (9, 10)] + [(28, 11), (27, 13), (26, 13)]
                                        ],
                                        [
                                            (x, y) for y in range(7, 13) for x in range(28) if x not in range(2, 5)
                                        ]
                                    ],
                        "troupe": [
                                        [
                                            ["tank", 320, 272, 10, True],
                                            ["tank", 320, 256, 10, True],
                                            ["tank", 320, 240, 10, True],
                                            ["mega tank", 304, 272, 10, True],
                                            ["mega tank", 304, 256, 10, True],
                                            ["mega tank", 304, 240, 10, True],
                                            ["jeep", 336, 272, 10, True],
                                            ["jeep", 336, 256, 10, True],
                                            ["heavy infantry", 336, 240, 10, True],
                                            ["heavy infantry", 352, 272, 10, True],
                                            ["heavy infantry", 352, 256, 10, True],
                                            ["heavy infantry", 352, 240, 10, True],
                                            ["infantry", 368, 272, 10, True],
                                            ["infantry", 368, 256, 10, True],
                                            ["infantry", 368, 240, 10, True]
                                        ],
                                        [
                                            ["tank", 320, 64, 10, True],
                                            ["tank", 320, 80, 10, True],
                                            ["tank", 320, 96, 10, True],
                                            ["mega tank", 304, 64, 10, True],
                                            ["mega tank", 304, 80, 10, True],
                                            ["mega tank", 304, 96, 10, True],
                                            ["jeep", 336, 64, 10, True],
                                            ["jeep", 336, 80, 10, True],
                                            ["heavy infantry", 336, 96, 10, True],
                                            ["heavy infantry", 352, 64, 10, True],
                                            ["heavy infantry", 352, 80, 10, True],
                                            ["heavy infantry", 352, 96, 10, True],
                                            ["infantry", 368, 64, 10, True],
                                            ["infantry", 368, 80, 10, True],
                                            ["infantry", 368, 96, 10, True]
                                        ]
                                    ],
                        "build": [
                                [
                                    [384, 304, 0, 0],
                                    [384, 16, 1, 0]
                                ],
                                [
                                    [16, 80, 2, 0],
                                    [16, 96, 2, 0],
                                    [32, 80, 2, 0],
                                    [64, 80, 2, 0],
                                    [80, 96, 2, 0],
                                    [80, 80, 2, 0],
                                    [48, 144, 2, 0],
                                    [48, 160, 2, 0],
                                    [16, 208, 2, 0],
                                    [16, 224, 2, 0],
                                    [32, 224, 2, 0],
                                    [80, 208, 2, 0],
                                    [80, 224, 2, 0],
                                    [64, 224, 2, 0],
                                    [80, 288, 0, 0],
                                    [96, 288, 0, 0],
                                    [320, 288, 0, 0],
                                    [352, 288, 0, 0],
                                    [336, 288, 0, 0],
                                    [64, 16, 1, 0],
                                    [80, 16, 1, 0],
                                    [368, 48, 1, 0],
                                    [368, 64, 1, 0],
                                    [352, 64, 1, 0],


                                ]
                            ],
                        "src": (480, 320, "../map/theBridge.png", "map")
    }
}


def load_texture(mapp):
    global texture
    src = ((781, 641, "../texture/spriteMap.png", "unite"),
           (781, 1790, "../texture/tile.png", "build"),
           (map[mapp]["src"]),
           (16, 16, "../texture/target.png", "target"),
           (16, 16, "../texture/case.png", "case"))

    for sr in src:
        img = pyxel.Image(sr[0], sr[1])
        img.load(0, 0, sr[2])
        texture[sr[3]] = img


current_music = 0


def next_music():
    global current_music

    if current_music == 1:
        current_music = 0
    else:
        current_music = 1
    pyxel.stop()
    pyxel.playm(current_music, loop=True)


def load_music():
    pyxel.load("../res_Bruno.pyxres", image=False, tilemap=False)


def traducteur(key):
    global lang, trad

    try:
        return trad[lang][key]
    except KeyError:
        return key
