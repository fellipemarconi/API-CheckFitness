FROM python:3.11.3-alpine3.18

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

WORKDIR /project

COPY requirements.txt requirements.txt
COPY scripts /scripts

RUN pip install -r requirements.txt
RUN adduser --disabled-password --no-create-home duser
RUN mkdir -p /data/web/static
RUN mkdir -p /data/web/media
RUN chown -R duser:duser /data/web/static
RUN chown -R duser:duser /data/web/media
RUN chmod -R 755 /data/web/static
RUN chmod -R 755 /data/web/media
RUN chmod -R +x /scripts

COPY . .

ENV PATH="/scripts:$PATH"

USER duser

EXPOSE 8000

CMD ["commands.sh"]