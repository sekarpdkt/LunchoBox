# LunchoBox
---

## How to use

Step #1: First clone the repository using following command

```
git clone https://github.com/sekarpdkt/LunchoBox.git
```

Step #2: Build the docker from scratch. Get into that directory where you have dockerfile and execute following command
```
docker build --rm -t lunchbox/pyml:ubuntu_1804.v1 .
```

Step #3: Run docker first time, bind port, give name for container
```
docker run -p 127.0.0.1:8085:8085/tcp -t -i --name LunchBox-pyML lunchbox/pyml:ubuntu_1804.v1 
```

Step #4: Restart stopped container.. No need to give port as it is already configured n above run command

```
docker start -i LunchBox-pyML
```

## Architecure

This is based on various best practices available, like

https://code.luasoftware.com/tutorials/nginx/setup-nginx-and-uwsgi-for-flask-on-ubuntu/

http://goinbigdata.com/docker-run-vs-cmd-vs-entrypoint/

https://hub.docker.com/r/tiangolo/uwsgi-nginx-flask/
