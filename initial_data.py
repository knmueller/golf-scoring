_PLAYERS_ = [('Adams, Dave', 'dadams', 'david.adams@viasat.com', 'gold'),
             ('Audi, Rob', 'raudi', 'Robert.Audi@fmr.com', 'gold'),
             ('Carle, Andy', 'acarle', 'andyc66@gmail.com', 'gold'),
             ('Champagne, Tim', 'tchampagne', 'tchampagne@bluecedar.com', 'gold'),
             ('Denlinger, Dave', 'ddenlinger', 'd.denlinger@verizon.net', 'white'),
             ('DeOliveira, Fernando', 'fdeoliveira', 'Fernando.DeOliveira@viasat.com', 'gold'),
             ('Ettenhofer, Todd', 'tettenhofer', 'Todd.Ettenhofer@viasat.com', 'gold'),
             ('Ferreira, Tom', 'tferreira', 'tom.ferreira@commscope.com', 'gold'),
             ('Flanagan, Dave', 'dflanagan', 'davidrflan@gmail.com', 'gold'),
             ('Hurley, Jim', 'jhurley', 'jhurley@bluecedar.com', 'gold'),
             ('Kelley, Connor', 'ckelley', 'ckelley@bluecedar.com', 'gold'),
             ('McLaughin, Ivonne', 'imclaughin', 'ivonne.mclaughlin@gmail.com', 'red'),
             ('McLaughin, Mark-David', 'mmclaughin', 'mdjmcl@gmail.com', 'gold'),
             ('Merritt, Chad', 'cmerritt', 'cmerritt@monogramfoods.com', 'gold'),
             ('Mueller, Kyle', 'kmueller', 'kmueller@bluecedar.com', 'gold'),
             ('Tillotson, Paul', 'ptillotson', 'ptillotson@bluecedar.com', 'gold'),
             ('Vincent, Shawn', 'svincent', 'svincent@bluecedar.com', 'gold'),
             ('Wante, Ken', 'kwante', 'kjwante@gmail.com', 'gold'),
             ('Wante, Nathan', 'nwante', 'npwante@gmail.com', 'gold'),
             ('White, Justin', 'jwhite', 'justin@thewhitefoxes.com', 'gold')
             ]

_TEAMS_ = {
    "Yin and Yang": ("Wante, Nathan", "Denlinger, Dave", 1),
    "Gone Not Forgotten": ("Wante, Ken", "Flanagan, Dave", 1),
    "Portuguese Rolls": ("Ferreira, Tom", "DeOliveira, Fernando", 2),
    "Positive Vibes": ("Champagne, Tim", "Carle, Andy", 2),
    "The Olson Twins": ("Hurley, Jim", "Adams, Dave", 3),
    "No beer cart no prob": ("White, Justin", "McLaughin, Mark-David", 3),
    "Sub Team 1": ("Vincent, Shawn", "Audi, Rob", 4),
    "C & C Gang": ("Merritt, Chad", "Kelley, Connor", 4),
    "2 Balls 1 Cup": ("Mueller, Kyle", "Tillotson, Paul", 5),
    "Watch Out For I.T.": ("Ettenhofer, Todd", "McLaughin, Ivonne", 5)
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
    "Vincent, Shawn": (25, 25),
    "Wante, Ken": (9, 9),
    "Wante, Nathan": (12, 12),
    "White, Justin": (11, 10)
}

_MEN_COURSE_HDCP_ = [
    9, 17, 1, 11, 15, 7, 5, 13, 3, 6, 14, 10, 8, 12, 2, 4, 18, 16
]

_WOMEN_COURSE_HDCP_ = [
    11, 17, 7, 5, 13, 9, 3, 15, 1, 8, 18, 16, 10, 2, 4, 12, 14, 6
]
