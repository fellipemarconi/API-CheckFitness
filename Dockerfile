FROM python:3.11.3-alpine3.18

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

WORKDIR /project

COPY requirements.txt requirements.txt
COPY scripts /scripts

RUN pip install -r requirements.txt
RUN adduser --disabled-password --no-create-home duser
RUN mkdir -p static
RUN mkdir -p media
RUN chown -R duser:duser static
RUN chown -R duser:duser media
RUN chmod -R 755 static
RUN chmod -R 755 media
RUN chmod -R +x /scripts

COPY . .

ENV PATH="/scripts:$PATH"

USER duser

EXPOSE 8000

CMD ["commands.sh"]