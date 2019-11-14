FROM python:3.7-alpine
WORKDIR /data  
VOLUME /data
#RUN pip install -t lib -r /data/requirements.txt
CMD ["pip install -t lib -r /data/requirements.txt"]
CMD ["python", "main.py"]