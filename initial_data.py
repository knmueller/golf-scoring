_PLAYERS_ = [('Olson, Mark', 'molson', 'mcolson513@gmail.com', 'gold'),
             ('Audi, Rob', 'raudi', 'Robert.Audi@fmr.com', 'gold'),
             ('Carle, Andy', 'acarle', 'andyc66@gmail.com', 'gold'),
             ('Champagne, Tim', 'tchampagne', 'tchampagne@bluecedar.com', 'gold'),
             ('Denlinger, Dave', 'ddenlinger', 'd.denlinger@verizon.net', 'white'),
             ('DeOliveira, Fernando', 'fdeoliveira', 'Fernando.DeOliveira@viasat.com', 'gold'),
             ('Ettenhofer, Todd', 'tettenhofer', 'Todd.Ettenhofer@viasat.com', 'gold'),
             ('Ferreira, Tom', 'tferreira', 'tom.ferreira@commscope.com', 'gold'),
             ('Flanagan, Dave', 'dflanagan', 'davidrflan@gmail.com', 'gold'),
             ('Hurley, Jim', 'jhurley', 'jhurley@bluecedar.com', 'gold'),
             ('Levi, Jonas', 'jlevi', 'jonaslevi05@gmail.com', 'gold'),
             ('McLaughin, Ivonne', 'imclaughin', 'ivonne.mclaughlin@gmail.com', 'red'),
             ('McLaughin, MarkDavid', 'mmclaughin', 'mdjmcl@gmail.com', 'gold'),
             ('Merritt, Chad', 'cmerritt', 'cmerritt@monogramfoods.com', 'gold'),
             ('Mueller, Kyle', 'kmueller', 'kmueller@bluecedar.com', 'gold'),
             ('Tillotson, Paul', 'ptillotson', 'ptillotson@bluecedar.com', 'gold'),
             ('Vincent, Shawn', 'svincent', 'svincent@bluecedar.com', 'gold'),
             ('Wante, Ken', 'kwante', 'kjwante@gmail.com', 'gold'),
             ('Wante, Nathan', 'nwante', 'npwante@gmail.com', 'gold'),
             ('White, Justin', 'jwhite', 'justin@thewhitefoxes.com', 'gold')
             ]

_TEAMS_ = {
    "The Dubliners": ("Hurley, Jim", "Flanagan, Dave", 1),
    "Wrecking Balls": ("Champagne, Tim", "Olson, Mark", 1),
    "Master and Apprentice": ("Wante, Nathan", "Wante, Ken", 2),
    "Box Of Chocolates": ("McLaughin, Ivonne", "Carle, Andy", 2),
    "All Over The Place": ("Levi, Jonas", "Audi, Rob", 3),
    "We Got No Honors": ("Vincent, Shawn", "White, Justin", 3),
    "The Olde RT Gang": ("Merritt, Chad", "DeOliveira, Fernando", 4),
    "Balls In Bushes": ("Mueller, Kyle", "McLaughin, MarkDavid", 4),
    "Did You See It": ("Ettenhofer, Todd", "Denlinger, Dave", 5),
    "Ass Wipes": ("Ferreira, Tom", "Tillotson, Paul", 5)
}

# Handicap Index × (Slope Rating ÷ 113) + (Course Rating – Par)

_HANDICAP_INDICES_NINE_HOLES_ = {
    "Audi, Rob": 11.8,
    "Carle, Andy": 10.7,
    "Champagne, Tim": 10.1,
    "Denlinger, Dave": 15.4,
    "DeOliveira, Fernando": 11.2,
    "Ettenhofer, Todd": 5.6,
    "Ferreira, Tom": 5.9,
    "Flanagan, Dave": 12.4,
    "Hurley, Jim": 10.8,
    "Levi, Jonas": 9.0,
    "McLaughin, Ivonne": 11.4,
    "McLaughin, MarkDavid": 16.3,
    "Merritt, Chad": 7.6,
    "Mueller, Kyle": 7.5,
    "Olson, Mark": 14.9,
    "Tillotson, Paul": 14.9,
    "Vincent, Shawn": 25.0,
    "Wante, Ken": 9.4,
    "Wante, Nathan": 9.7,
    "White, Justin": 10.2
}

# player name : (front handicap, back handicap)
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
    "McLaughin, Ivonne": (13, 12),
    "McLaughin, MarkDavid": (19, 19),
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
# _MEN_COURSE_HDCP_ = [
#     9, 17, 1, 11, 15, 7, 5, 13, 3, 6, 14, 10, 8, 12, 2, 4, 18, 16
# ]

_MEN_COURSE_HDCP_ = [
    9, 17, 3, 11, 13, 7, 5, 15, 1, 6, 10, 16, 8, 12, 4, 2, 18, 14
]

_WOMEN_COURSE_HDCP_ = [
    11, 17, 7, 5, 13, 9, 3, 15, 1, 8, 18, 16, 10, 2, 4, 12, 14, 6
]
