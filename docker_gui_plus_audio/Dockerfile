FROM python:3.11

RUN apt-get update 
RUN apt-get install ffmpeg libsm6 libxext6  -y 
RUN apt-get install pulseaudio -y
RUN pip install moviepy

WORKDIR /home/app
COPY . .

CMD [ "python", "app.py" ]