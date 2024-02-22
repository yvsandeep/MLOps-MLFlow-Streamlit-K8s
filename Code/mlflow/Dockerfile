FROM python:3.8-slim-bullseye

ARG WORKDIR=/mlflow
RUN mkdir /mlflow
WORKDIR ${WORKDIR}

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN echo "export LC_ALL=$LC_ALL" >> /etc/profile.d/locale.sh
RUN echo "export LANG=$LANG" >> /etc/profile.d/locale.sh

COPY requirements.txt ${WORKDIR}
RUN pip install -U pip && \
  pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV DB_NAME=postgres
ENV DB_USERNAME=postgres
ENV DB_HOST=127.0.0.1
ENV DB_PASSWORD=password
ENV DEFAULT_ARTIFACT_ROOT=gs://example

ENTRYPOINT mlflow server \
  --host=0.0.0.0 \
  --port=5000 \
  --backend-store-uri=postgresql://${DB_USERNAME}:${DB_PASSWORD}@${DB_HOST}:5432/${DB_NAME} \
  --default-artifact-root=${DEFAULT_ARTIFACT_ROOT}
