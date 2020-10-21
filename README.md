# demo_python
ejercicio demo de Python y Docker

docker build --build-arg UWSGI_HTTP_PORT=9000 -t demo/uwsgi .
docker build -t demo/uwsgi .
docker run -d -p 8080:8000 --restart unless-stopped -v $(pwd)/app:/app demo/uwsgi