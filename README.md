<h1 align="center">
<br>
Twitter Bot
</h1>

<p align="center">conquer twitter</p>

<hr />
<br />


## 📚 Project Definition

Simple API for social media platform(currently only twitter is supported)


## 🛠️ Features

Technologies used:

- ⚛️ **Flask** — Python library
- 🌐 **Docker** — Containerization
- 📊 **PostgreSQL** - Database
- 📊 **GitHub Actions** - Deployment

## Deployment
* cp .env.example .env
* for GitHub actions we need to set secrets from deploy_fly.yml

# Docker
```
  docker-compose up -d
```
```
  ./scripts/run_server.sh
```


## Commands
* flask db migrate -m <message> 
* flask db upgrade
* flask configure-db (commands are located in <PROJECT_ROOT>\app\commands.py)

## Build docker image
* docker build -f Dockerfile.fly --build-arg https_proxy=<proxy> --progress=plain --no-ca che .

## Misc
OPTIONAL
* changes for migrations so we can use a optional schema(other than "public")

\migrations\env.py
```
    schema = current_app.config['DB_SCHEMA']

    def include_object(object, name, type_, reflected, compare_to):
        if type_ == "table" and object.schema != schema:
            return False
        else:
            return True

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            include_schemas=True,
            version_table_schema=schema,
            include_object=include_object,
            process_revision_directives=process_revision_directives,
            **current_app.extensions['migrate'].configure_args
        )
```

# TODO
- [] terraform pentru fly.io https://fly.io/docs/app-guides/terraform-iac-getting-started/
- [] add a post model type (joke, recepie, etc...)
- [] endpoint for adding a role to an user