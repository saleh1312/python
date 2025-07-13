FROM python:3.11

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install opencv-python

WORKDIR /home/app
COPY . .

CMD [ "python", "app.py" ]
