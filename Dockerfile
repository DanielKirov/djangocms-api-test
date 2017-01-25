FROM docker.pancentric.com/pancentric/docs-backend:base
ADD cmstest /app
ADD requirements.txt /app
WORKDIR /app
RUN rm -rf djangocms-rest-api && git clone https://github.com/DanielKirov/djangocms-rest-api 
RUN pip install uwsgi && pip install -r requirements.txt
RUN python manage.py collectstatic --noinput
EXPOSE 8080
ENTRYPOINT python manage.py migrate --noinput && \
	uwsgi --http :8080 --wsgi-file cmstest/wsgi.py --static-map /static=/app/static/
