
1- install x server in windows and run it

docker build -t opencv-demo .

docker run -it --rm --name cv_test_gui -e DISPLAY=host.docker.internal:0.0 opencv-demo
