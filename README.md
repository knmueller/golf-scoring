# Golf Scoring

A simple flask webapp to calculate the following scores:

1. Net player score for front 9
2. Net player score for back 9
3. Net player total score
4. Team net total score

### Running The App
To get the app up and running, go to the terminal and do the following:
```
$ cd <golf-scoring-dir>
$ export FLASK_APP=scoringapp.py
$ flask run
```

The default port the app runs on is http://localhost:5000

### Debugging the DB
To debug the database, insert entries, query data, etc., set the `FLASK_APP` env variable and run the `flask shell` 
command. This will drop you into an interactive shell to communicate with the db with python syntax. Here is an example:

```
[~/project/golf-scoring] $ flask shell                                                                                                                                     21:58:16
Python 3.9.6 (default, Jun 29 2021, 05:25:02)
[Clang 12.0.5 (clang-1205.0.22.9)] on darwin
App: app [production]
Instance: /Users/kyle/project/golf-scoring/instance
>>> players = Player.query.all()
>>> teams = Team.query.all()
>>> print(teams)
[<1 Team Watch Out For I.T.>, <2 Team Yin and Yang>, <3 Team 2 Balls 1 Cup>, <4 Team The Olson Twins>, <5 Team One A-Holer>, <6 Team No beer cart no prob>, <7 Team C & C Gang>, <8 Team Gone Not Forgotten>, <9 Team Portuguese Rolls>, <10 Team Positive Vibes>]
>>> print(players)
[<1 Player Adams, Dave>, <2 Player Audi, Rob>, <3 Player Carle, Andy>, <4 Player Champagne, Tim>, <5 Player Denlinger, Dave>, <6 Player DeOliveira, Fernando>, <7 Player Ettenhofer, Todd>, <8 Player Ferreira, Tom>, <9 Player Flanagan, Dave>, <10 Player Hurley, Jim>, <11 Player Kelley, Connor>, <12 Player McLaughlin, Ivonne>, <13 Player McLaughlin, Mark-David>, <14 Player Merritt, Chad>, <15 Player Mueller, Kyle>, <16 Player Tillotson, Paul>, <17 Player Vincent, Shawn>, <18 Player Wante, Ken>, <19 Player Wante, Nathan>, <20 Player White, Justin>]
>>> print(teams[0])
<1 Team Watch Out For I.T.>
>>> print(teams[0].player_one)
7
>>> print(players[6])
<7 Player Ettenhofer, Todd>
```

### Entering Scores
The home page of the app is used to enter scores for every player. Here is an example screenshot:

![Entering Score](screenshots/entering-scores-screenshot.jpg?raw=true "Entering Scores")

### Viewing Results
Once the scores are entered, the user clicks the Submit button. All of the scoring will be calculated and displayed in 
tables. There is also a "Results" link in the top bar to go directly to the Results tables. Here is an example of that page:

![Viewing Results](screenshots/viewing-results-screenshot.jpg?raw=true "Viewing Results")


#### TODO
X - authentication / signup page <br>
X - editing player scores allowed only for the player who is logged in <br>
X - help page <br>
X - reset password via admin page <br>
X - Fix submission bug <br>
X - Add admin user outside of kmueller <br>
X - Best Gross table -- no zeros <br>
X - Add table for Championship match -- gross scores <br>
X - add hole handicaps <br>
X - can add negative numbers to input field on scores <br>
X - calculate handicap match scores <br>
X - highlight champ table hole winner in javascript <br>
X - sort front/back net tables with None last <br>
X - Best of Worst - net score not showing if only 1 player entered <br>
X - reset scores button for admin <br>
X - Fix championship match scoring -> CONFIRM -- i think i fixed it. Was using the wrong index in the nested for loop <br>
- Add pages in the top bar to show individual tables <br>
- refresh login timeout <br>
- Update results table titles and font <br>
- Add top/bottom table margins <br>
- unittests for flask <br>
- issues with multiple open pages trying to submit scores? <br>
--- don't think so? Tried 2 users in same 4some


#### TODO 2022
X - Update players and teams
X - Add security response headers
- Add new tiebreaker
- README duck-pi.sh
- calculate handicaps.
- Add Handicap table link to top bar

#### TODO 2023
- Remove player name as key to everything
- replace @app.before_first_request
