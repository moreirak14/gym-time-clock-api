FROM python:3.10.4-slim-buster
ENV PYTHONBUFFERED 1
ENV PYTHONPATH /app/src

RUN apt update && apt install -y --no-install-recommends

RUN mkdir /app
WORKDIR /app
ADD pyproject.toml poetry.lock /app/

RUN apt install make
RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

ADD . /app

EXPOSE 8080

CMD ["uvicorn", "main:get_app", "--host", "0.0.0.0", "--port", "8080"]
