git pull 
virtualenv -p python3.7 kaid
source kaid/bin/activate
pip install -r requirements/production.txt  # all requirements - gunicorn djang$
pip install gunicorn psycopg2-binary django[argon2]
export DJANGO_SETTINGS_MODULE=myhealth.settings.production
export DATABASE_URL=postgres://blog:blog@127.0.0.1:5432/kids 
#export  SECRET_KEY=345tyu
echo DATABASE_URL=postgres://blog:blog@127.0.0.1:5432/kids >> src/myhealth/sett$
echo SECRET_KEY=345tyu >> src/myhealth/settings/local.env
python src/manage.py migrate
python src/manage.py collectstatic --noinput
sudo systemctl restart kaid
deactivate
