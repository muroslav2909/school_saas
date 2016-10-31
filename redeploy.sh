#git pull origin master
python manage.py collectstatic --noinput --clear
gunicorn school_saas.wsgi -b 127.0.0.1:8000