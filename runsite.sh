# run website
uwsgi --socket personalwebsite.sock --http :3000 --module personalwebsite.wsgi --chmod-socket=666 &
