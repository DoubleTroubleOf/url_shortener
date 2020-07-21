heroku pg:reset DATABASE_URL

release: python manage.py makemigrations --no-input
release: python manage.py migrate --no-input

web: gunicorn config.wsgi