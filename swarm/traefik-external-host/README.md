# Traefik avec exposition des ports sur Internet

## Installation du stack

```shell
> docker stack deploy traefik-external --compose-file docker-compose.yml
Creating network traefik-external_default
Creating service traefik-external_traefik
Creating service traefik-external_whoami
```

### Test

Une instance de traefik (un replica seulement par noeud et seulement sur le manager) + 5 instances de whoami.

```shell
> curl --header "Host: example.com"  http://192.168.99.100:80/
Hostname: b0dc376c36d2
IP: 127.0.0.1
IP: 10.0.13.6
IP: 172.18.0.3
RemoteAddr: 10.0.13.3:40574
GET / HTTP/1.1
Host: example.com
User-Agent: curl/7.68.0
Accept: */*
Accept-Encoding: gzip
X-Forwarded-For: 192.168.99.1
X-Forwarded-Host: example.com
X-Forwarded-Port: 80
X-Forwarded-Proto: http
X-Forwarded-Server: a8f1ab6c8aa1
X-Real-Ip: 192.168.99.1
```
