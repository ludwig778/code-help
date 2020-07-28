# Nginx configuration

## Upstreams

### HTTP/Uwsgi

```
upstream my_app {
    server my_app:8080;
}
```

### Unix socket

```
upstream my_app {
    server unix:/my_app/unicorn.sock
}
```

## Proxy confs

### Basic

```
server {
    listen 80;
    server_name _;
}
```

### Http pass

```
    location / {
        proxy_pass my_app;
    }
```

### Uwsgi pass

```
    location / {
        uwsgi_pass my_app;
    }
```

### Headers

```
    location / {
        proxy_pass my_app;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
```

### Static

```
    location /static {
        alias /var/www/my_app/static;
    }
```
