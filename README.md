docker build . -t mud-gcp
#docker run --rm -v ${pwd}/vol:/data/:rw mud-gcp
docker run -d -p 8000:8000 -v ${pwd}/vol:/app/:rw --name mud-gcp mud-gcp
docker port mud-gcp
docker ps -a
docker stop mud-gcp
docker rm mud-gcp

docker login ;
docker push hososugi/mud-gcp