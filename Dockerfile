FROM python:3.11-slim

WORKDIR /app

ENV PYTHONPATH .

RUN pip install poetry

COPY poetry.lock pyproject.toml ./

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-dev|| echo "Poetry install failed"

COPY . .

CMD ["python", "-m", "app.main"]
