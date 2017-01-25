FROM python:2.7.13
ADD cmstest /app
ADD requirements.txt /app
WORKDIR /app
RUN git submodule init && git submodule update
RUN pip install uwsgi && pip install -r requirements.txt
EXPOSE 8080
ENTRYPOINT uwsgi --http :8080 --wsgi-file cmstest/wsgi.py
