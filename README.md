# ﻿Docker, créer et administrer vos conteneurs virtuels d'applications - Travaux pratiques

## TP1: Installation

Vous avez à votre disposition une machine virtuelle sous Ubuntu 18.04.
* 20Go d’espace disque
* 4Go de mémoire
* 1vCPU

Activez le dépôt « Extras » via la commande :

    > sudo yum-config-manager --enable extras

Installez certains packages utiles :

    > sudo yum install -y yum-utils device-mapper-persistent-data lvm2

Déclarez le repository Docker :

    > sudo yum-config-manager 
      --add-repo https://download.docker.com/linux/centos/docker-ce.repo

Installez Docker CE :

    > sudo yum install docker-ce docker-ce-cli containerd.io

Activer Docker au démarrage puis démarrer le démon Docker pour cette session :

    > systemctl enable docker
    > systemctl start docker

Testez l’installation de Docker via la commande :

    > docker --version
    > docker info

## TP2: Charger des images docker par tag

Charger l’image par défaut (sans tag):

    > docker pull busybox

Charger les images avec les tags

    > docker pull busybox:1
    > docker pull busybox:latest
    > docker pull busybox:1.30
    > docker pull busybox:uclibc
    > docker pull busybox:1.31
    > docker pull busybox:1-uclibc

Déduire à partir de l’image ID quels sont les tags associés à chaque image:

    > docker images
    REPOSITORY      TAG         IMAGE ID        CREATED         SIZE
    busybox         1           020584afccce    4 weeks ago     1.22MB
    busybox         1-uclibc    020584afccce    4 weeks ago     1.22MB
    busybox         1.31        020584afccce    4 weeks ago     1.22MB
    busybox         latest      020584afccce    4 weeks ago     1.22M
    busybox         uclibc      020584afccce    4 weeks ago     1.22MB
    busybox         1.30        64f5d945efcc    6 months ago    1.2MB

C’est la même image pour les tags 1, 1-uclibc,1.31,latest et 1.30.


''Note'': le résultat peut changer entre le moment où je rédige ces lignes et le moment où vous expérimentez par vous-même.

## TP3: inspection

Lister les variables d’environnement (commandes env et export)
> docker run -it busybox env
> docker run -it busybox sh -c export

''Note'': la commande export est une commande interne du shell, il faut donc la démarrer dans un shell.

Lister les processus et leur PID (ps)
> docker run -it busybox ps aux

Lister les interfaces réseaux (ifconfig)
> docker run -it busybox ifconfig

## TP4: Simple MySQL

Démarrer un conteneur basé sur l’image MySQL(sans l’option “-d”)
> docker run mysql

Étudier dans la documentation quels paramètres vous permettent de démarrer le conteneur sans erreur
> docker run -e MYSQL_ROOT_PASSWORD=pa33word mysql

''Notes'': 
* Il existe d’autres variables d’environnement permettant de démarrer MySQL, voir la documentation.
* S’il est démarré sans les paramètres “-it”, le CTRL-C ne fonctionne pas.


Une fois réussi le démarrage du conteneur sans l’option “-d”,  démarrer un nouveau conteneur basé sur l’image MySQL en tâche de fond
> docker run -d -e MYSQL_ROOT_PASSWORD=pa33word mysql


Vérifier son bon fonctionnement (est il “Up” ?)
> docker ps 


Détruire l’ensemble des conteneurs arrêtés ou encore en exécution
> docker stop id_ou_nom_du_conteneur
> docker rm id_ou_nom_du_conteneur


Notes: Il est possible de stopper et détruire un conteneur par
> docker rm -f id_ou_nom_du_conteneur
TP5: ballade sur Docker Hub
Authentifier vous via docker login sur votre compte (même identifiants que Docker Hub):
> docker login                 
Login with your Docker ID to push and pull images from Docker Hub. [...]
Username: kartoch
Password:
[...]
Login Succeeded


Copier une image existante sur votre repository privé:
> docker pull hello-world:latest
> docker tag hello-world:latest kartoch/hello:basic
> docker push kartoch/hello:basic
TP7: Simple NGINX
Faire un attach dessus:
> docker attach sw


Le redémarrer:
> docker start sw


faire une pause dessus:
> docker pause sw


faire un unpause
> docker unpause sw
TP8: montage bind dans NGINX
Démarrer un conteneur nginx:
> docker run --name sw -d -p 8080:80 nginx


Utiliser docker cp pour copier le fichier /etc/nginx/nginx.conf sur votre hôte:
> docker cp sw:/etc/nginx/nginx.conf .


Éteindre le conteneur
> docker rm -f sw


Démarrer un nouveau conteneur nginx en montant:
* Le fichier sur votre hôte nginx.conf dans le chemin /etc/nginx/nginx.conf dans le conteneur
* Le répertoire html dans le chemin /usr/share/nginx/html dans le conteneur
>  docker run --name sw -d
--mount type=bind,source="$(pwd)"/nginx.conf,target=/etc/nginx/nginx.conf
--mount type=bind,source="$(pwd)"/html/,target=/usr/share/nginx/html 
-p 8080:80 nginx
TP9: montage de volumes dans NGINX
Démarrer un conteneur busybox avec un volume monté en /html
> docker run -it --mount source=html,target=/html busybox 


Créer un fichier /html/index.html avec le message “HELLO WORLD !” dans le conteneur
/# echo “HELLO WORLD” > /html/index.html


Eteindre le conteneur
> docker rm -v -f busybox 


Démarrer un conteneur nginx avec le volume monté sur /usr/share/nginx/html
> docker run --name sw -d --mount source=html,target=/usr/share/nginx/html -p 8080:80 nginx
TP10: montage lecture seule et tmpfs de NGINX
Lancer un conteneur NGINX en lecture seule, en montant
* Les répertoires nécessitant l’écriture en tmpfs
   * Attention à /var/run/, ce n’est pas un répertoire
* Le volume créé dans le TP8 monté en /usr/share/nginx/html en lecture seule
> docker run --name sw -d --read-only 
--mount type=tmpfs,destination=/run/  
--mount type=tmpfs,destination=/var/cache/nginx/ 
--mount source=html,target=/usr/share/nginx/html,ro -p 8080:80 nginx
TP11: mongodb et mongo-express
Créez un réseau bridge nommé backnet
> docker network create backnet


Lancez un conteneur MongoDB (image : mongo) nommé “mongo” sur ce réseau backnet.
> docker run --name mongo --network=backnet -d mongo


Lancez un service basé sur l’image mongo-express (interface d’admin web pour MongoDB) nommé mongo-express sur ce même réseau backnet , en publiant le port 8081 à l’extérieur tout en fournissant le nom d’hôte du service MongoDB via la variable d’environnement ME_CONFIG_MONGODB_SERVER.
> docker run --name mongo-express -p 8081:8081 --network=backnet
-e ME_CONFIG_MONGODB_SERVER=mongo mongo-express
TP12: mise en place d’un registry
Mettez en place un conteneur Docker Registry (nom de l’image: registry) sur votre machine avec le port 5000 disponible sur votre interface localhost.
> docker run --name registry -d -p 5000:5000 registry


Charger une image ubuntu (pull) sur votre hôte
> docker pull ubuntu


Tagger cette image avec le nom localhost:5000/mypremierimage
> docker tag ubuntu localhost:5000/mypremierimage


Uploader là sur le docker registry (en utilisant le tag comme nom)
> docker push localhost:5000/mypremierimage
TP13: limitation des CPUs
Démarrer 1 conteneur
* avec l’image progrium/stress 
* le paramètre de stress pour utiliser quatres CPUs --cpu 4
* Mais avec les limitations des ressources CPU pour que le conteneur n’utilise que 25% maximum des ressources CPU.
> docker run --cpus=1 progrium/stress --cpu 4


Note: l’affichage avec ps sur l’hôte peut montrer que chaque processus prend 25% mais la charge globale indiquée avec htop montre bien 25% au gloabl..


Démarrer 2 conteneurs
* avec l’image progrium/stress 
* Sur le premier le paramètre de stress pour utiliser quatres CPUs --cpu 4
* Sur le premier le paramètre de stress pour utiliser huit CPUs --cpu 8
* Mais avec les limitations des ressources CPU pour que le premier conteneur puisse occuper 3 fois plus de CPU que le second.
> docker run -d --cpu-shares=3096 progrium/stress --cpu 4
> docker run -d progrium/stress --cpu 8                      
TP14: Builder vos images hello
Créer 2 images de notre application:
* yourdockerhubname/hello:v1 qui affiche “NOM - PRÉNOM - Hello World”
* yourdockerhubname/hello:v2 qui affiche “NOM - PRÉNOM - Hello World Again”
# Modifier hello.py pour ajouter votre nom et prénom
> docker build -t kartoch/hello:v2 .
# Modifier hello.py pour ajouter again
> docker build -t kartoch/hello:v3 .


Charger les images dans votre compte docker hub
> docker push kartoch/hello:v2
> docker push kartoch/hello:v3


Demander à votre voisin de lancer deux conteneurs avec vos images mappés sur deux ports différentes
> docker run --rm -p 5000:5000 kartoch/hello:v2 python hello.py
> docker run --rm -p 5001:5000 kartoch/hello:v3 python hello.py
TP15: adapter notre image
Dockerfile


FROM ubuntu:latest
LABEL maintainer="kartoch@gmail.com"
ARG MY_NAME
RUN apt-get update
RUN apt-get install -y python3 python3-pip
RUN pip3 install Flask
RUN apt-get install -y curl
ADD hello.py /home/hello.py
ADD static /home/static
RUN echo "${MY_NAME}" > /home/static/name.txt
WORKDIR /home
CMD ["/usr/bin/python3", "hello.py"]
HEALTHCHECK --interval=5m --timeout=3s CMD curl -f \ 
    http://localhost:5000/healthz || exit 1
VOLUME /home/static/
USER 1000
EXPOSE 5000
TP16: compose du TP15
docker-compose.yaml


version: '3.7'
services:
  some-postgres:
        image: "postgres:10"
        environment:
          POSTGRES_USER: ${POSTGRES_USER}
          POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
  adminer:
        image: "adminer"
        ports:
          - "8080:8080"
  some-drupal:
        image: "drupal:8-apache"
        ports:
          - "80:80"
        environment:
          POSTGRES_USER: ${POSTGRES_USER}
          POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
TP19: déploiement Swarm
> docker service create --replicas 1 --name helloworld kartoch/hello:v3
> docker service scale helloworld=5




© Julien Cartigny Consulting – Tous droits réservés – 2019 - Version 1.0.1 (30/11/2019)                                /
