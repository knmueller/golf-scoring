_PLAYERS_ = [('Audi, Rob', 'raudi', 'Robert.Audi@fmr.com', 'gold'),
             ('Carle, Andy', 'acarle', 'andyc66@gmail.com', 'gold'),
             ('Champagne, Tim', 'tchampagne', 'tchampagne@bluecedar.com', 'gold'),
             ('Denlinger, Dave', 'ddenlinger', 'd.denlinger@verizon.net', 'white'),
             ('DeOliveira, Fernando', 'fdeoliveira', 'Fernando.DeOliveira@viasat.com', 'gold'),
             ('Ettenhofer, Todd', 'tettenhofer', 'Todd.Ettenhofer@viasat.com', 'gold'),
             ('Ferreira, Tom', 'tferreira', 'tom.ferreira@commscope.com', 'gold'),
             ('Flanagan, Dave', 'dflanagan', 'davidrflan@gmail.com', 'white'),
             ('Hurley, Jim', 'jhurley', 'jhurley@bluecedar.com', 'gold'),
             ('Levi, Jonas', 'jlevi', 'jonaslevi05@gmail.com', 'gold'),
             ('Magley, Dale', 'dmagley', 'dmmagley@gmail.com', 'gold'),
             ('McLaughlin, Ivonne', 'imclaughlin', 'ivonne.mclaughlin@gmail.com', 'green'),
             ('McLaughlin, MarkDavid', 'mmclaughlin', 'mdjmcl@gmail.com', 'gold'),
             ('Merritt, Chad', 'cmerritt', 'cmerritt@monogramfoods.com', 'gold'),
             ('Mueller, Kyle', 'kmueller', 'kmueller@bluecedar.com', 'gold'),
             ('ODea, Mike', 'modea', 'mikeodea19@gmail.com', 'gold'),
             ('Tillotson, Paul', 'ptillotson', 'ptillotson@bluecedar.com', 'gold'),
             ('Wante, Ken', 'kwante', 'kjwante@gmail.com', 'gold'),
             ('Wante, Nathan', 'nwante', 'npwante@gmail.com', 'gold'),
             ('White, Justin', 'jwhite', 'justin@thewhitefoxes.com', 'gold')
             ]

_TEAMS_ = {
    "Bald Eagles": ("Audi, Rob", "Ettenhofer, Todd", 1),
    "X-Out": ("Wante, Ken", "Carle, Andy", 1),
    "Beauty & Beast Mode": ("Merritt, Chad", "Tillotson, Paul", 2),
    "MF": ("Mueller, Kyle", "Flanagan, Dave", 2),
    "Pound & Pound": ("Levi, Jonas", "White, Justin", 3),
    "Salt n Pepa": ("McLaughlin, Ivonne", "Hurley, Jim", 3),
    "Deez Nuts": ("Wante, Nathan", "ODea, Mike", 4),
    "Guiness Guys": ("Magley, Dale", "DeOliveira, Fernando", 4),
    "Couple of Putts": ("Ferreira, Tom", "McLaughlin, MarkDavid", 5),
    "Thunder Buddies": ("Champagne, Tim", "Denlinger, Dave", 5)
}

# Handicap Index × (Slope Rating ÷ 113) + (Course Rating – Par)

_HANDICAP_INDICES_NINE_HOLES_ = {
    "Audi, Rob": 12.8,
    "Carle, Andy": 9.0,
    "Champagne, Tim": 10.3,
    "Denlinger, Dave": 15.1,
    "DeOliveira, Fernando": 11.3,
    "Ettenhofer, Todd": 5.2,
    "Ferreira, Tom": 5.7,
    "Flanagan, Dave": 13.1,
    "Hurley, Jim": 10.8,
    "Levi, Jonas": 9.1,
    "Magley, Dale": 7.0,
    "McLaughlin, Ivonne": 10.6,
    "McLaughlin, MarkDavid": 15.2,
    "Merritt, Chad": 5.6,
    "Mueller, Kyle": 7.7,
    "ODea, Mike": 4.0,
    "Tillotson, Paul": 14.5,
    "Wante, Ken": 9.0,
    "Wante, Nathan": 9.9,
    "White, Justin": 10.1
}

# player name : (front handicap, back handicap)
# TODO dont think i need this anymore. Now calculating the handicaps
_HANDICAPS_ = {
    "Audi, Rob": (14, 14),
    "Carle, Andy": (13, 12),
    "Champagne, Tim": (12, 12),
    "Denlinger, Dave": (16, 16),
    "DeOliveira, Fernando": (13, 13),
    "Ettenhofer, Todd": (7, 6),
    "Ferreira, Tom": (7, 7),
    "Flanagan, Dave": (15, 14),
    "Hurley, Jim": (13, 12),
    "Levi, Jonas": (11, 10),
    "McLaughlin, Ivonne": (13, 12),
    "McLaughlin, MarkDavid": (19, 19),
    "Merritt, Chad": (9, 9),
    "Mueller, Kyle": (9, 8),
    "Olson, Mark": (18, 17),
    "Tillotson, Paul": (18, 17),
    "Vincent, Shawn": (25, 25),
    "Wante, Ken": (11, 11),
    "Wante, Nathan": (12, 11),
    "White, Justin": (12, 12)
}

# 2021 hole handicaps
_MEN_COURSE_HDCP_ = [
    9, 17, 1, 11, 15, 7, 5, 13, 3, 6, 14, 10, 8, 12, 2, 4, 18, 16
]

# From card on website -- wrong
# _MEN_COURSE_HDCP_ = [
#     9, 17, 3, 11, 13, 7, 5, 15, 1, 6, 10, 16, 8, 12, 4, 2, 18, 14
# ]

_WOMEN_COURSE_HDCP_ = [
    11, 17, 7, 5, 13, 9, 3, 15, 1, 8, 18, 16, 10, 2, 4, 12, 14, 6
]

# (Rating, Slope)
HIGHFIELDS_FRONT_PAR = 36
HIGHFIELDS_BACK_PAR = 36
HIGHFIELDS_GOLD_RATING = (71.4, 130)
HIGHFIELDS_GOLD_FRONT_RATING = (35.6, 131)  # 35.6 / 131
HIGHFIELDS_GOLD_BACK_RATING = (35.8, 129)  # 35.8 / 129
HIGHFIELDS_WHITE_RATING = (69.2, 126)
HIGHFIELDS_WHITE_FRONT_RATING = (34.3, 130)  # 34.3 / 130
HIGHFIELDS_WHITE_BACK_RATING = (34.9, 121)  # 34.9 / 121
HIGHFIELDS_GREEN_RATING = (70.4, 126)  # Women's rating
HIGHFIELDS_GREEN_FRONT_RATING = (35.3, 127)  # Women's rating 35.3 / 127
HIGHFIELDS_GREEN_BACK_RATING = (35.1, 124)  # Women's rating 35.1 / 124
