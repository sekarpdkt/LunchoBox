#!/bin/bash
#Sleep for 60 sec to allow /usr/local/bin/uwsgi --ini /etc/uwsgi/emperor.ini to come up
/usr/sbin/service nginx start
/bin/sleep 60
/usr/sbin/service nginx restart
/bin/sleep 60
/usr/sbin/service nginx start
/bin/sleep 60
/usr/sbin/service nginx start
/bin/sleep 60
/usr/sbin/service nginx start
