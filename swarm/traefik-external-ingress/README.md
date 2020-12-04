# Traefik avec exposition des ports sur Internet via Ingress

## Installation du stack

```shell
> docker stack deploy traefik-external-ingress --compose-file docker-compose.yml
Creating network traefik-external-ingress_default
Creating service traefik-external-ingress_traefik
Creating service traefik-external-ingress_whoami
```

### Test

2 instances de traefik + 5 instances de whoami

```shell
> curl --header "Host: example.com"  http://192.168.99.108/
Hostname: 52681dc30a17
IP: 127.0.0.1
IP: 10.0.4.11
IP: 172.18.0.4
RemoteAddr: 10.0.4.3:46224
GET / HTTP/1.1
Host: example.com
User-Agent: curl/7.68.0
Accept: */*
Accept-Encoding: gzip
X-Forwarded-For: 10.0.0.2
X-Forwarded-Host: example.com
X-Forwarded-Port: 80
X-Forwarded-Proto: http
X-Forwarded-Server: 2d3b3de7454b
X-Real-Ip: 10.0.0.2
> curl --header "Host: example.com"  http://192.168.99.108/
Hostname: 66ff744c3680
IP: 127.0.0.1
IP: 10.0.4.9
IP: 172.18.0.5
RemoteAddr: 10.0.4.4:36048
GET / HTTP/1.1
Host: example.com
User-Agent: curl/7.68.0
Accept: */*
Accept-Encoding: gzip
X-Forwarded-For: 10.0.0.2
X-Forwarded-Host: example.com
X-Forwarded-Port: 80
X-Forwarded-Proto: http
X-Forwarded-Server: e3090d72fa38
X-Real-Ip: 10.0.0.2
```
