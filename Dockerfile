FROM python:3.11-slim

WORKDIR /code

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir -r /code/requirements.txt

COPY ./app /code/app

CMD ["fastapi", "run", "app/main.py", "--port", "80"]