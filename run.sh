#!/bin/bash

# author: Seongwoo Lee Lukaid
# email: crescent3859@gmail.com

if [ "$1" == "mm" ]; then
    sudo docker exec -it lukaid-me-server-django-1 python manage.py makemigrations
elif [ "$1" == "mi" ]; then
    sudo docker exec -it lukaid-me-server-django-1 python manage.py migrate
else
    sudo docker exec -it lukaid-me-server-django-1 $@
fi

# sudo chown -R dir
# sudo chmod -R 777 dir