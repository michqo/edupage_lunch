# Script to order edupage lunch

Automate ordering lunches on edupage.

## Developing

Copy `.env.dev` to `.env`

Fill out variables in `.env` file

Install dependencies using [poetry](https://python-poetry.org)

```
poetry install
```

Activate virtual environment

```
poetry shell
```

Run script

```
python -m edupage_lunch.main
```

## Docker

Build the image

```
docker build .
```

Create and run a container

```
docker run -d --name edupage_lunch --env-file .env image_id
```
