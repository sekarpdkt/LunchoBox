#!/bin/bash
#As uwsgi will take more time to load ML data etc, start nginx after few min and run it in back ground
/bin/bash /usr/local/bin/startnginx.sh &

#Start uwsgi service. As it is inside a docker, we can not use start service. 
#Rest of the information as available in https://code.luasoftware.com/tutorials/nginx/setup-nginx-and-uwsgi-for-flask-on-ubuntu/
#basically /etc/uwsgi/emperor.ini ==> /etc/uwsgi/vassals/myapp.ini ==> /app/ ==> app:main and also socket /var/run/uwsgi/pyMLB.sock
/usr/local/bin/uwsgi --ini /etc/uwsgi/emperor.ini
