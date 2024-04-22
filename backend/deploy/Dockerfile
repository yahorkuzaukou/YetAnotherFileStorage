FROM python:3.12.3-slim-bookworm

WORKDIR /secret_path
RUN apt-get update && apt-get install -y netcat-openbsd

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip install pipenv
COPY ./Pipfile ./Pipfile.lock /secret_path/
RUN pipenv install --system --deploy

COPY ./src /secret_path/src
COPY ./deploy/entrypoint.sh /secret_path/

RUN chmod +x /secret_path/entrypoint.sh
ENTRYPOINT ["sh", "./entrypoint.sh"]