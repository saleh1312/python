FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install alsa-utils pulseaudio

CMD ["aplay", "/usr/share/sounds/alsa/Front_Center.wav"]
