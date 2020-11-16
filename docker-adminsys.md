# Docker pour AdminSys

## TP??: limitation des CPUs

Démarrer 1 conteneur

* avec l’image `progrium/stress`
* le paramètre de stress pour utiliser quatres CPUs --cpu 4
* Mais avec les limitations des ressources CPU pour que le conteneur n’utilise que 25% maximum des ressources CPU.

> docker run --cpus=1 progrium/stress --cpu 4

'''Note''': l’affichage avec ps sur l’hôte peut montrer que chaque processus prend 25% mais la charge globale indiquée avec htop montre bien 25% au gloabl..

Démarrer 2 conteneurs:

* avec l’image progrium/stress
* Sur le premier le paramètre de stress pour utiliser quatres CPUs --cpu 4
* Sur le premier le paramètre de stress pour utiliser huit CPUs --cpu 8
* Mais avec les limitations des ressources CPU pour que le premier conteneur puisse occuper 3 fois plus de CPU que le second.

> docker run -d --cpu-shares=3096 progrium/stress --cpu 4
> docker run -d progrium/stress --cpu 8
