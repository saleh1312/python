FROM python:3.11

RUN apt-get update 
# for opencv 
RUN apt-get install ffmpeg libsm6 libxext6  -y 
# for pulse audio
RUN apt-get install pulseaudio -y
RUN pip install moviepy

WORKDIR /home/app
COPY . .

ENV PULSE_SERVER=host.docker.internal
ENV DISPLAY=host.docker.internal:0.0

CMD [ "python", "app.py" ]