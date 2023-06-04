docker rm -f meryem

git add .
git commit -am "$(date)"
git push

docker build -t meryem:latest -t meryem:v2.0 . 
#docker run -it -d -p 8090:80 -v /home/ibrahim/sandbox/meryem/logs:/var/log/nginx:rw --name meryem meryem 
#docker run -it -d -p 8090:80 --name meryem --restart always -v /home/ibrahim/sandbox/meryem/website:/www -v /home/ibrahim/sandbox/meryem/logs:/var/log/nginx:rw meryem:latest 
docker run -it -d -p 8090:8000 --name meryem --restart always meryem:latest 
#docker run -it meryem 
#docker run -it node
#docker exec -it meryem sh
