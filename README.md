# Docker, Django, PostgreSQL starter (Incomplete, work-in-progress)

This is a simple starter for a
[Django](https://www.djangoproject.com/) app with a
[PostgreSQL](https://www.postgresql.org/) backend
running inside [Docker](https://www.docker.com/)
containers.

This starter is based on the following resources,
that I used to make some of the design decisions:

- [Quickstart: Compose and Django](https://docs.docker.com/compose/django/)
- [How to Dockerize a Django web app elegantly](https://medium.com/faun/tech-edition-how-to-dockerize-a-django-web-app-elegantly-924c0b83575d)
- [Dockerizing Django with Postgres, Gunicorn, and Nginx](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/)
- [lukin0110/docker-django-boilerplate](https://github.com/lukin0110/docker-django-boilerplate)

You might want to look at those resources.

## Getting started

First, you'll need the following variables in your environment. It is best to keep these in
a file called `.env` that is ignored by git.

```
ADMIN_USERNAME=CHANGE-THIS-VALUE
ADMIN_PASSWORD=CHANGE-THIS-VALUE
ADMIN_EMAIL=CHANGE-THIS-VALUE
SECRET_KEY=CHANGE-THIS-VALUE
POSTGRES_PASSWORD=CHANGE-THIS-VALUE
POSTGRES_USER=CHANGE-THIS-VALUE
POSTGRES_PASSWORD=CHANGE-THIS-VALUE
POSTGRES_DB=CHANGE-THIS-VALUE
POSTGRES_PORT=CHANGE-THIS-VALUE
```

The `POSTGRES_` values are used to configure the PostgreSQL instance running in a Docker
container when in development. In production, you might be using Heroku Postgres, in which
case the app will use the `DATABASE_URL` environment variable instead.

You'll need [docker](https://docs.docker.com/install/) to run this app on your
computer. I assume you'll run production on [Heroku](https://www.heroku.com)
and included the files necessary to do so using
[Heroku Docker deploys](https://devcenter.heroku.com/articles/build-docker-images-heroku-yml)

To start the app, run `docker-compose up`. To bring the app down, run `docker-compose down`.

The first time you start-up in development, or after you make model changes, you'll need
to run database migrations. With the app running, run `docker-compose exec web python manage.py migrate`
in order to run the migrations.

## Changing the models

If you change the models you'll need new migrations. Run

```
docker-compose exec web python manage.py makemigration -n SOMENAMEHERE
```

You'll see a new migration file that you can add to version control.
See [Django migrations](https://docs.djangoproject.com/en/2.2/topics/migrations/).

## Notes

- Whitenoise is used for static assets. See [here](https://devcenter.heroku.com/articles/django-assets).
- [Gunicorn](https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/gunicorn/) is used in production on heroku.
