FROM python:3.10

ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

RUN pip install pipenv
COPY ./Pipfile* ./
RUN pipenv install --ignore-pipfile

COPY . /app

CMD ["sh", "run.sh"]