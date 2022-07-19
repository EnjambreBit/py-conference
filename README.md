# py-conference

## Instalacíon

Requisitos previos

- postgres 10.x +
- maildev 

Instalacion

  make install

ó

  pipenv install

## Configuracion

Archivo .env

```
DEBUG=on
ENVIROMENT='DEVELOPMENT'
DATABASE_URL="postgres://postgres:postgress@localhost/conference"
REDIS_URL="redis://localhost:6379/2"
ALLOWED_HOSTS="127.0.0.1;localhost"
SENTRY_DSN=""
ENABLE_SENTRY=off
EMAIL_PORT=1025
EMAIL_HOST=localhost
EMAIL_HOST_USER=""
EMAIL_HOST_PASSWORD=""
EMAIL_USE_TLS=off
```

