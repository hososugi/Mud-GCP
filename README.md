# Starting
docker build . -t mud-gcp
docker run -d -p 8000:8000 -v ${pwd}/app:/app mud-gcp

#Extra checking
docker ps -a
docker port mud-gcp
docker logs [container ID]

# Restarting
docker restart [container ID]

# Removing
docker stop mud-gcp
docker rm mud-gcp

# Deploying
docker login ;
docker push hososugi/mud-gcp