_PLAYERS_ = [('Adams, Dave', 'dadams', 'david.adams@viasat.com', 'user'),
             ('Audi, Rob', 'raudi', 'Robert.Audi@fmr.com', 'user'),
             ('Carle, Andy', 'acarle', 'andyc66@gmail.com', 'user'),
             ('Champagne, Tim', 'tchampagne', 'tchampagne@bluecedar.com', 'user'),
             ('Denlinger, Dave', 'ddenlinger', 'd.denlinger@verizon.net', 'user'),
             ('DeOliveira, Fernando', 'fdeoliveira', 'Fernando.DeOliveira@viasat.com', 'user'),
             ('Ettenhofer, Todd', 'tettenhofer', 'Todd.Ettenhofer@viasat.com', 'user'),
             ('Ferreira, Tom', 'tferreira', 'tom.ferreira@commscope.com', 'user'),
             ('Flanagan, Dave', 'dflanagan', 'davidrflan@gmail.com', 'user'),
             ('Hurley, Jim', 'jhurley', 'jhurley@bluecedar.com', 'user'),
             ('Kelley, Connor', 'ckelley', 'ckelley@bluecedar.com', 'user'),
             ('McLaughin, Ivonne', 'imclaughin', 'ivonne.mclaughlin@gmail.com', 'user'),
             ('McLaughin, Mark-David', 'mmclaughin', 'mdjmcl@gmail.com', 'user'),
             ('Merritt, Chad', 'cmerritt', 'cmerritt@monogramfoods.com', 'user'),
             ('Mueller, Kyle', 'kmueller', 'kmueller@bluecedar.com', 'admin'),
             ('Tillotson, Paul', 'ptillotson', 'ptillotson@bluecedar.com', 'user'),
             ('Vincent, Shawn', 'svincent', 'svincent@bluecedar.com', 'user'),
             ('Wante, Ken', 'kwante', 'kjwante@gmail.com', 'user'),
             ('Wante, Nathan', 'nwante', 'npwante@gmail.com', 'user'),
             ('White, Justin', 'jwhite', 'justin@thewhitefoxes.com', 'user')
             ]

_TEAMS_ = {
    "Watch Out For I.T.": ("Ettenhofer, Todd", "McLaughin, Ivonne"),
    "Yin and Yang": ("Wante, Nathan", "Denlinger, Dave"),
    "2 Balls 1 Cup": ("Mueller, Kyle", "Tillotson, Paul"),
    "The Olson Twins": ("Hurley, Jim", "Adams, Dave"),
    "Sub Team 1": ("Vincent, Shawn", "Audi, Rob"),  # TODO subs
    "No beer cart no prob": ("White, Justin", "McLaughin, Mark-David"),
    "C & C Gang": ("Merritt, Chad", "Kelley, Connor"),
    "Gone Not Forgotten": ("Wante, Ken", "Flanagan, Dave"),
    "Portugues Rolls": ("Ferreira, Tom", "DeOliveira, Fernando"),
    "Positive Vibes": ("Champagne, Tim", "Carle, Andy")
}

# Handicap Index × (Slope Rating ÷ 113) + (Course Rating – Par)

_HANDICAP_INDICES_NINE_HOLES_ = {
    "Adams, Dave": 8.6,
    "Audi, Rob": 12.0,
    "Carle, Andy": 11.1,
    "Champagne, Tim": 10.3,
    "Denlinger, Dave": 15.7,
    "DeOliveira, Fernando": 12.3,
    "Ettenhofer, Todd": 6.0,
    "Ferreira, Tom": 6.5,
    "Flanagan, Dave": 13.1,
    "Hurley, Jim": 10.5,
    "Kelley, Connor": 19.4,
    "McLaughin, Ivonne": 12.2,
    "McLaughin, Mark-David": 15.2,
    "Merritt, Chad": 4.8,
    "Mueller, Kyle": 7.1,
    "Tillotson, Paul": 19.3,
    "Vincent, Shawn": 26.1,
    "Wante, Ken": 7.9,
    "Wante, Nathan": 10.6,
    "White, Justin": 9.0
}

# player name : (front handicap, back handicap)
_HANDICAPS_ = {
    "Adams, Dave": (10, 10),
    "Audi, Rob": (14, 14),
    "Carle, Andy": (13, 13),
    "Champagne, Tim": (12, 12),
    "Denlinger, Dave": (16, 17),
    "DeOliveira, Fernando": (14, 14),
    "Ettenhofer, Todd": (7, 7),
    "Ferreira, Tom": (8, 7),
    "Flanagan, Dave": (15, 15),
    "Hurley, Jim": (12, 12),
    "Kelley, Connor": (23, 23),
    "McLaughin, Ivonne": (12, 12),
    "McLaughin, Mark-David": (18, 18),
    "Merritt, Chad": (6, 5),
    "Mueller, Kyle": (8, 8),
    "Tillotson, Paul": (23, 23),
    "Vincent, Shawn": (31, 31),
    "Wante, Ken": (9, 9),
    "Wante, Nathan": (12, 12),
    "White, Justin": (11, 10)
}
