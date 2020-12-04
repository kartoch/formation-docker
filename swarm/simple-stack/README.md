# Simple stack

## Deploy

Avec utilisation du placement spread.

```shell
> docker node update --label-add worker=1 worker1
> docker node update --label-add worker=2 worker2
> docker stack deploy simple-stack --compose-file docker-compose.yml --with-registry-auth
```
