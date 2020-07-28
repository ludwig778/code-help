# Uwsgi configuration

## Basic

```
[uwsgi]
chdir=/home/my_app
module=my_app.wsgi:application
socket=0.0.0.0:8080
master=True
vacuum=True
max-requests=5000
processes = 4
die-on-term = true
```

## Protocol

```
protocol=http
```

or

```
protocol=uwsgi
```

## Stats

```
stats=:5001
stats-http=true
```

## Spooler

```
spooler-processes=4
spooler-python-import=my_app.spooler
spooler=/tmp/uwsgi_spool/
```
