FROM python:3.12

WORKDIR /app

COPY pyproject.toml poetry.lock README.md ./

RUN pip install poetry --break-system-packages && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

COPY . /app

RUN chmod +x /app/start.sh
