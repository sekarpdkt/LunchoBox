#install latest ubuntu from ubuntu default docker
FROM ubuntu

#Where are we going to store nltk data
ENV NLTK_DATA /usr/share/nltk_data


#update ubuntu, install python and PIP3
RUN apt-get -y update && \
        apt-get -y  upgrade && \
        apt-get -y purge && \
        apt-get  -y install python3 python3-pip nginx nano wget

#Install ML packages
RUN pip3 --no-cache-dir install numpy pandas scipy python-dateutil scikit-learn nltk unidecode gensim keras flask textblob  uwsgi xxhash && \
        pip3 --no-cache-dir install tensorflow==1.5.0 && \
        python3 -m nltk.downloader -d /usr/share/nltk_data punkt wordnet stopwords && \
        chown -R www-data:www-data /usr/share/nltk_data

#Create directories for uwsgi and nginx and set access rights
#More info at https://code.luasoftware.com/tutorials/nginx/setup-nginx-and-uwsgi-for-flask-on-ubuntu/
RUN mkdir /etc/uwsgi && \
        mkdir /etc/uwsgi/vassals && \
        mkdir /machineLearning && \
        mkdir /var/log/uwsgi/ && \
        touch /var/log/uwsgi/emperor.log && \
        touch /var/log/uwsgi/pyMLB.log && \
        touch /var/log/uwsgi/SMSHamSpam.log && \
        chown -R www-data:www-data /var/log/uwsgi/ && \
        mkdir /var/run/uwsgi/ && \
        chown -R www-data:www-data /var/run/uwsgi

        
#Expose port 8085 from docker
ENV LISTEN_PORT 8085
        
EXPOSE 8085 8086
        
#Copy config files to respective location
COPY ./config/emperor.uwsgi.service  /etc/systemd/system/emperor.uwsgi.service
COPY ./config/pyMLB.ini  /etc/uwsgi/vassals/pyMLB.ini
COPY ./config/SMSHamSpam.ini  /etc/uwsgi/vassals/SMSHamSpam.ini
COPY ./config/emperor.ini  /etc/uwsgi/emperor.ini
COPY ./config/pyMLB /etc/nginx/sites-available/pyMLB
COPY ./config/SMSHamSpam /etc/nginx/sites-available/SMSHamSpam

COPY ./config/startupScritpt.sh /usr/local/bin/startupScritpt.sh
COPY ./config/startnginx.sh /usr/local/bin/startnginx.sh


RUN chmod 755 /usr/local/bin/startupScritpt.sh && \
        chmod 755 /usr/local/bin/startnginx.sh && \
        ln -s /etc/nginx/sites-available/pyMLB /etc/nginx/sites-enabled  && \
        ln -s /etc/nginx/sites-available/SMSHamSpam /etc/nginx/sites-enabled 


#Copy our app and data into docker image
COPY ./app /app
COPY ./data /data

#if in doubt refer to http://goinbigdata.com/docker-run-vs-cmd-vs-entrypoint/
#Set the command that need to run when we start container
CMD ["/usr/local/bin/startupScritpt.sh"]
