#Applied Cloud Computing - Assignment 2
#From Sep29th 2022 to Sep30th 2022

FROM python:3.10.7 AS build
# command line tool for interacting with the Advanced Package Tool (APT) library
RUN apt-get update
#wget downloads files from web
RUN apt-get install wget

#add user
ARG username=MonaGopal
ENV username $username
RUN useradd  -m $username
RUN mkdir /home/$username/pyNotebook

#download files onto container
RUN wget https://raw.githubusercontent.com/monishagopal7/Applied-Cloud-Computing/Assignment2/Applied_Assignment_2.ipynb -P ./home/$username/pyNotebook/
RUN wget https://raw.githubusercontent.com/monishagopal7/Applied-Cloud-Computing/Assignment2/requirements.txt -P ./home/$username/pyNotebook/

#chown changes the user and/or group ownership of each given file
RUN chown $username:$username ./home/$username/pyNotebook/*
#hmod stands for "change mode." It restricts the way a file can be accessed
RUN chmod u+rw ./home/$username/pyNotebook/*

#pip instals all needed pacages for the python notebook to run
RUN pip3 install -r ./home/$username/pyNotebook/requirements.txt

USER ${username}
WORKDIR /home/${username}/pyNotebook/

#Expose the port before its used for better working 
EXPOSE 8888

#The su (short for substitute or switch user) utility allows you to run commands with another user's privileges, by default the root user.

ENTRYPOINT ["jupyter", "notebook","./Applied_Assignment_2.ipynb", "--ip=0.0.0.0","--allow-root"]
