# Simple gestion de secret

## Installation du stack

```shell
> docker stack deploy simple-secret --compose-file docker-compose.yml
Creating network simple-secret_default
Creating secret simple-secret_my_pass
Creating service simple-secret_just-a-test
```

## Test

```shell
> docker service logs simple-secret_just-a-test
simple-secret_just-a-test.1.xdsqzike507k@manager    | abc123%
```