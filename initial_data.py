# list format: name, username, email, tee name, 9-hold-handicap-index
_USERS_ = [
    ('Boice, Rob', 'rboice', 'boicer17@gmail.com', 'gold', 9.3),  # 1
    ('Carle, Andy', 'acarle', 'andyc66@gmail.com', 'gold', 8.7),  # 2
    ('Champagne, Tim', 'tchampagne', 'tchamp@champagnesoftware.com', 'gold', 10.3),  # 3
    ('Denlinger, Dave', 'ddenlinger', 'd.denlinger@verizon.net', 'white', 16.2),  # 4
    ('ForFred, Sub', 'sub', 'todo@todo.com', 'gold', 9.1),  # 5
    ('Ettenhofer, Todd', 'tettenhofer', 'Todd.Ettenhofer@viasat.com', 'gold', 5.9),  # 6
    ('Ferreira, Tom', 'tferreira', 'tom.ferreira@commscope.com', 'gold', 4.9),  # 7
    ('Flanagan, Dave', 'dflanagan', 'davidrflan@gmail.com', 'white', 13.6),  # 8
    ('Magley, Dale', 'dmagley', 'dmmagley@gmail.com', 'gold', 6.9),  # 9
    ('McLaughlin, Ivonne', 'imclaughlin', 'ivonne.mclaughlin@gmail.com', 'green', 11.2),  # 10
    ('McLaughlin, MD', 'mmclaughlin', 'mdjmcl@gmail.com', 'gold', 11.8),  # 11
    ('Merritt, Chad', 'cmerritt', 'cmerritt@monogramfoods.com', 'gold', 4.0),  # 12
    ('Mueller, Kyle', 'kmueller', 'k.mueller17@gmail.com', 'gold', 8.3),  # 13
    ('Olson, Mark', 'molson', 'mcolson513@gmail.com', 'gold', 9.8),  # 14
    ('Priest, John', 'jpriest', 'johnpriest@verizon.net', 'gold', 10.2),  # 15
    ('Tillotson, Paul', 'ptillotson', 'paul.tillotson@gmail.com', 'gold', 17.7),  # 16
    ('Wante, Ken', 'kwante', 'kjwante@gmail.com', 'gold', 8.4),  # 17
    ('Wante, Nathan', 'nwante', 'npwante@gmail.com', 'gold', 7.2),  # 18
    ('Wesley, Anne', 'awesley', 'awesley@protonmail.com', 'green', 20.2),  # 19
    ('White, Justin', 'jwhite', 'justin@thewhitefoxes.com', 'gold', 9.5),  # 20
    # ('Levi, Jonas', 'jlevi', 'jonaslevi05@gmail.com', 'gold'),
]

_TEAMS_ = {
    'Iron Faden': (2, 16, 1),
    'Liver Let Die': (20, 11, 1),
    'I\'d Tap That': (13, 14, 2),
    'Bogey Boys': (18, 3, 2),
    'Rise and Grind': (6, 1, 3),
    'Salt and Pepper': (9, 10, 3),  # 'Magley, Dale', 'McLaughlin, Ivonne'
    'Fairway to Heaven': (17, 8, 4),  # 'Wante, Ken', 'Flanagan, Dave'
    'The Olde RT Gang': (12, 5, 4),  # 'Merritt, Chad', 'ForFred, Sub'
    'Silver Foxes': (19, 4, 5),  # 'Wesley, Anne', 'Denlinger, Dave'
    'Team 1': (7, 15, 5)  # 'Ferreira, Tom', 'Priest, John'
}

# Course Handicap = Handicap Index × (Slope Rating ÷ 113) + (Course Rating – Par)

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
