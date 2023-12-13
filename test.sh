#
docker rm -f meryemtest
#
sudo chmod 777 ./docker/* -R
sudo chown ibrahim:ibrahim ./* -R
#
git add .
git commit -am "$(date)"
git push

docker build -t meryemtest:test . 
#docker build -t meryem:latest -t meryem:v2.0 . 
#docker run -it -d -p 8090:80 -v /home/ibrahim/sandbox/meryem/logs:/var/log/nginx:rw --name meryem meryem 
#docker run -it -d -p 8090:80 --name meryem --restart always -v /home/ibrahim/sandbox/meryem/website:/www -v /home/ibrahim/sandbox/meryem/logs:/var/log/nginx:rw meryem:latest 
##docker run -it -d -p 8090:8000 --name meryem --restart always meryem:latest 
#docker run -it meryem 
#docker run -it node
#docker exec -it meryem sh
docker run -it -d \
    -p 8091:8000 \
    --name meryemtest \
    --restart always \
    meryemtest:test

#     -v ./docker/code:/code/db \

#git clone -b email https://github.com/ichibsah/meryem.git ./email
