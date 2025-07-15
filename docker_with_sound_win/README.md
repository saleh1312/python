
1- download puleaudio server and setup it


docker build -t sound-demo .


docker run -it --rm -e PULSE_SERVER=host.docker.internal sound-demo

