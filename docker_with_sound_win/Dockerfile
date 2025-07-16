FROM ubuntu:22.04


RUN apt update -y
RUN apt install alsa-utils pulseaudio -y

WORKDIR /home/app

COPY audio.wav .

ENV PULSE_SERVER=host.docker.internal

CMD ["aplay", "audio.wav"]
