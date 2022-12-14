FROM nikolaik/python-nodejs:python3.9-nodejs16

RUN apt update && apt upgrade -y
RUN apt install git curl python3-pip ffmpeg -y

RUN cd /
RUN git clone https://github.com/thorthunderbot/AnjalRobot
RUN cd AnjalRobot
WORKDIR /AnajlRobot

RUN pip3 install --upgrade pip

CMD python3 main.py
