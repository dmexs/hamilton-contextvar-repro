FROM python:3.11

ENV POETRY_VERSION=1.8.3

WORKDIR /app

RUN pip install poetry==$POETRY_VERSION

COPY pyproject.toml poetry.lock ./

# Install dependencies without venv
RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-directory --no-ansi

COPY . .

CMD ["python", "app/main.py"]