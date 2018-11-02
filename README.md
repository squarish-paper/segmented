# Segmented

A Django Heroku app which displays segment details from Strava APIs.

## Running Locally

Make sure you have Python 3.7 [installed locally](http://install.python-guide.org). To push to Heroku, you'll need to install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli), as well as [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```sh
$ git clone https://github.com/heroku/python-getting-started.git
$ cd python-getting-started

$ virtualenv --python python3 env
$ source env/bin/activate
$ pip install -r requirements.txt

$ heroku create
$ heroku addons:add heroku-postgresql:hobby-dev
$ python manage.py migrate
$ python manage.py collectstatic

$ heroku local web
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Clearing local db
```sh
rm main/migrations/*
rm db.sqlite3
echo "" > main/migrations/__init__.py
python manage.py makemigrations
python manage.py migrate
```

## Deploying to Heroku

```sh
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku open
```

## TODOS

This is very much an application for me to learn python/django/heroku as well as calling Strava APIs, and will continually improve

Functionally, these are the tings it should do
- [x] Strava Authentication
- [x] Get user, activities, segments and leaderboards
- [x] Get efforts for user in segments
- [ ] "Recent" - get recently attempted segments
- [ ] "Starred" - get user starred segments
- [ ] "Opportunities" - get segments that there is a chance to get into top 10
- [ ] "Threats" - Any KOMs that are very close to being lost
- [ ] Manual Refresh
- [ ] Table Sorting
- [ ] Segment Searching
- [ ] Deauth
- [ ] Public/private

Code wise, here are the thins it should do
- [x] Dashboard styling
- [ ] Home page styling
- [ ] Private/reconnect page styling
- [ ] Config
- [ ] AJAX Calls
- [ ] Rank / tenth bug
