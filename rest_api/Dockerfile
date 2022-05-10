FROM python:3.9

COPY . .

RUN python -m pip install --upgrade pip
RUN python -m pip install .

RUN chmod +x rest_api/docker-entrypoint.sh

ENTRYPOINT [ "rest_api/docker-entrypoint.sh" ]