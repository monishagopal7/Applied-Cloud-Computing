FROM python

COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

#creat voumne named app
VOLUME /app 

WORKDIR /app

EXPOSE 8000
# -v $(pwd) it gives the path of the current working directory
#touch text.txt creates the txt file
#create project in terminal so we don't have to create project everytime you build a docker image

#ls gives list of files
#touch to create from from inside to outside
#django create project is doe in terminal and not in docker file to avoid creation of multiple projects
