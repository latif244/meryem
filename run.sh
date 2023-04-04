docker build -t meryem . 
#docker run -it -d -p 8090:80 -v /home/ibrahim/sandbox/meryem/logs:/var/log/nginx:rw --name meryem meryem 
docker run -it -d -p 8090:80 --restart always -v /home/ibrahim/sandbox/meryem/website:/www -v /home/ibrahim/sandbox/meryem/logs:/var/log/nginx:rw --name meryem meryem 
#docker run -it meryem 
#docker run -it node
#docker exec -it meryem sh
git add .
git commit -am "$(date)"
git push