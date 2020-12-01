# Traefik avec exposition des ports sur Internet

## Installation du stack

```shell
> docker stack deploy traefik-external --compose-file docker-compose.yml
Creating network traefik-external_default
Creating service traefik-external_traefik
Creating service traefik-external_whoami
```

### Test

```shell
> docker-machine ssh manager1
   ( '>')
  /) TC (\   Core is distributed with ABSOLUTELY NO WARRANTY.
 (/-_--_-\)           www.tinycorelinux.net

docker@manager1:~$ curl --header "Host: example.com" http://127.0.0.1:80/
Hostname: e7e2b1130158
IP: 127.0.0.1
IP: 10.0.10.3
IP: 172.18.0.3
RemoteAddr: 10.0.10.6:49414
GET / HTTP/1.1
Host: example.com
User-Agent: curl/7.54.1
Accept: */*
Accept-Encoding: gzip
X-Forwarded-For: 10.0.0.2
X-Forwarded-Host: example.com
X-Forwarded-Port: 80
X-Forwarded-Proto: http
X-Forwarded-Server: c80149abca58
X-Real-Ip: 10.0.0.2

```
