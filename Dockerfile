FROM python:3.12

WORKDIR /app

COPY pyproject.toml poetry.lock README.md ./

RUN pip install poetry --break-system-packages && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

COPY src /app/src

CMD ["litestar", "--app", "src.main:app", "run", "--host", "0.0.0.0", "--port", "8000"]
