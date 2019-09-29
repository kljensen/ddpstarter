# Docker, Django, PostgreSQL starter (Incomplete, work-in-progress)

This will be a simple starter for a
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

## Requirements

The requirements for this project are as follows. As a developer...

1. I should be able start my app using [docker-compose](https://docs.docker.com/compose/)
2. I should be able to create all the "fixtures" for my database, easily, such
   as superuser accounts and associated passwords.
3. I should be able to specify any URL for the PostgreSQL database, e.g.
   either locally in docker or remotely if I'm using a hosted PostgreSQL
   instance as I might find on Heroku or AWS.
4. I can run various Django admin functions such as migrations.
5. I can deploy my app on Heroku.
6. I can turn on "debugging" or "development mode" when working locally.
7. I can practice test driven development.
8. I can write end-to-end tests and run them in development.
9. I can use continuous deployment with GitHub and [Heroku Pipelines](https://devcenter.heroku.com/articles/pipelines).

## Bootstrapping new deployment

If you're deploying to a fresh environment, you'll
need to run the following

```
docker-compose exec web python manage.py migrate auth
docker-compose exec web python manage.py migrate
```

There are some data migrations, e.g. `./web/awaydays/migrations/0001_initial.py` will add a super user based on the following
environment variables:

```
SUPERUSER_USERNAME
SUPERUSER_PASSWORD
SUPERUSER_EMAIL
```
