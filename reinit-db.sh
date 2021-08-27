#!/bin/bash

rm -f scores.db
rm -rf migrations
flask db init
flask db migrate -m "users table"
flask db upgrade
flask db migrate -m "players table"
flask db upgrade
flask db migrate -m "teams table"
flask db upgrade
