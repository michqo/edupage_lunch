ARG PYTHON_VERSION=3.11.3-alpine

FROM python:${PYTHON_VERSION}


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /code

WORKDIR /code

RUN pip install poetry
COPY pyproject.toml poetry.lock /code/
RUN poetry config virtualenvs.create false
RUN poetry install --only main --no-root --no-interaction
COPY . /code

CMD ["python", "-m", "edupage_lunch.main"]
