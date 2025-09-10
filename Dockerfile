###########################
# Prod runtime
###########################

FROM python:3.12-slim as runtime

WORKDIR /app

COPY pytest.ini .

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src/ ./src/
RUN pip install -e ./src/helloworld/

CMD ["python", "-m", "helloworld.main"]

###########################
# Dev runtime
###########################

FROM python:3.12-slim as dev

WORKDIR /app

COPY pytest.ini .

COPY requirements.txt .
COPY requirements-dev.txt .
RUN pip install -r requirements-dev.txt

COPY src/ ./src/
RUN pip install -e ./src/helloworld/

CMD ["python", "-m", "helloworld.main"]

