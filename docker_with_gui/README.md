docker build -t opencv-demo .

xhost +local:docker

docker run -it --rm --name cv_test_gui -v /tmp/.X11-unix:/tmp/.X11-unix:ro -e DISPLAY=$DISPLAY opencv-demo

xhost -local:docker