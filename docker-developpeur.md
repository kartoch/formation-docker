# Docker pour développeurs

## TP3: Charger des images docker par tag

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

## TP4: inspection

Lister les variables d’environnement (commandes env et export)
> docker run -it busybox env
> docker run -it busybox sh -c export
> docker run -it ubuntu env
> docker run -it ubuntu sh -c export

''Note'': la commande export est une commande interne du shell, il faut donc la démarrer dans un shell.

Lister les processus et leur PID (ps)
> docker run -it busybox env
> docker run -it ubuntu env

Lister les interfaces réseaux (ifconfig)
> docker run -it busybox ifconfig

'''Note''': la commande ifconfig n'est pas disponible par défaut dans l'image ubuntu. Il faut donc d'abord installer le package contenant ifconfig:
> docker run -it ubuntu sh -c "apt-get update ; apt-get install net-tools ; ifconfig"

## TP5: Simple MySQL

Démarrer un conteneur basé sur l’image MySQL(sans l’option “-d”)
> docker run mysql

Étudier dans la documentation quels paramètres vous permettent de démarrer le conteneur sans erreur: l'image attend un ou plusieurs paramètres sous forme de variables d'environnement pour démarrer correctement.

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

Notes: Il est possible de stopper et détruire un conteneur en une seule étape:
> docker rm -f id_ou_nom_du_conteneur

## TP6: ballade sur Docker Hub

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

## TP7: Simple NGINX

Faire un attach dessus (pour regarder les logs en temps-réel):
> docker attach sw

Le redémarrer:
> docker start sw

faire une pause dessus:
> docker pause sw

faire un unpause
> docker unpause sw

## TP8: montage bind dans NGINX

Démarrer un conteneur nginx:
> docker run --name sw -d -p 8080:80 nginx

Utiliser docker cp pour copier le fichier /etc/nginx/nginx.conf sur votre hôte:
> docker cp sw:/etc/nginx/nginx.conf .

Éteindre le conteneur
> docker rm -f sw

Démarrer un nouveau conteneur nginx en montant:

* Le fichier sur votre hôte nginx.conf dans le chemin /etc/nginx/nginx.conf dans le conteneur
* Le répertoire html dans le chemin /usr/share/nginx/html dans le conteneur

> docker run --name sw -d
--mount type=bind,source="$(pwd)"/nginx.conf,target=/etc/nginx/nginx.conf
--mount type=bind,source="$(pwd)"/html/,target=/usr/share/nginx/html 
-p 8080:80 nginx

## TP9: montage de volumes dans NGINX

Démarrer un conteneur busybox avec un volume monté en /html
> docker run -it --mount source=html,target=/html busybox 

Créer un fichier /html/index.html avec le message “HELLO WORLD !” dans le conteneur
/# echo “HELLO WORLD” > /html/index.html
/# exit

Eteindre le conteneur
> docker rm -v -f busybox

Démarrer un conteneur nginx avec le volume monté sur /usr/share/nginx/html
> docker run --name sw -d --mount source=html,target=/usr/share/nginx/html -p 8080:80 nginx

## TP10: montage lecture seule et tmpfs de NGINX

Lancer un conteneur NGINX en lecture seule, en montant :

* Les répertoires nécessitant l’écriture en tmpfs (Attention à `/var/run/`, ce n’est pas un répertoire, c'est un lien vers `/run`)
* Le volume créé dans le TP8 monté en /usr/share/nginx/html en lecture seule

> docker run --name sw -d --read-only 
--mount type=tmpfs,destination=/run/  
--mount type=tmpfs,destination=/var/cache/nginx/
--mount source=html,target=/usr/share/nginx/html,ro -p 8080:80 nginx

## TP11: mise en place d’un registry

Mettez en place un conteneur Docker Registry (nom de l’image: registry) sur votre machine avec le port 5000 disponible sur votre interface localhost.
> docker run --name registry -d -p 5000:5000 registry

Charger une image ubuntu (pull) sur votre hôte
> docker pull ubuntu

Tagger cette image avec le nom localhost:5000/mypremierimage
> docker tag ubuntu localhost:5000/mypremierimage

Uploader là sur le docker registry (en utilisant le tag comme nom)
> docker push localhost:5000/mypremierimage

## TP12: mongodb et mongo-express

Créez un réseau bridge nommé backnet
> docker network create backnet

Lancez un conteneur MongoDB (image : mongo) nommé “mongo” sur ce réseau backnet.
> docker run --name mongo --network=backnet -d mongo

Lancez un service basé sur l’image mongo-express (interface d’admin web pour MongoDB) nommé mongo-express sur ce même réseau backnet , en publiant le port 8081 à l’extérieur tout en fournissant le nom d’hôte du service MongoDB via la variable d’environnement ME_CONFIG_MONGODB_SERVER.

> docker run --name mongo-express -p 8081:8081 --network=backnet
-e ME_CONFIG_MONGODB_SERVER=mongo mongo-express

## TP13: Builder vos images hello

Reprende le contenu du TP12 (idsponible dans le répertoire TP13) et éditer la chaîne de caractère retournée par la méthode `hello_world()` dans le fichier `hello.py`. Puis lancer le build de votre nouvelle image :
> docker build -t yourdockerhubname/hello:v1 .

Charger les images dans votre compte docker hub:
> docker push yourdockerhubname/hello:v1

Demander à votre voisin de charger votre image (il faut que votre image soit publique):
> docker pull yourdockerhubname/hello:v1

Puis de lancer un conteneur avec votre image:
> docker run --rm -p 5000:5000 yourdockerhubname/hello:v1 python3 -m flask run

## TP14: adapter notre image

Voir [répertoire tp14](./tp14)

## TP15: compose

Voir [répertoire tp15](./tp15)
