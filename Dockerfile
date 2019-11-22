FROM ubuntu:16.04
LABEL maintainer="danelhombre@gmail.com"
RUN apt-get update -y && apt-get install -y python-pip python-dev gunicorn
# Copy just the requirements.txt first to leverage Docker cache.
COPY ./app/requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8000
CMD gunicorn -b 0.0.0.0:8000 -k flask_sockets.worker app:app

#ENTRYPOINT ["python"]
#CMD ["app.py"]