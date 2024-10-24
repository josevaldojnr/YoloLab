FROM python:3.7-slim

WORKDIR /app


RUN apt-get update && \
    apt-get install ffmpeg libsm6 libxext6  -y \
    libopencv-dev
#    python3-opencv

RUN pip install notebook

RUN pip install torch==1.4.0 torchvision==0.5.0

RUN pip install opencv-python

COPY . .

EXPOSE 8093
EXPOSE 8083

CMD ["bash", "-c","jupyter notebook --ip=0.0.0.0 --allow-root --no-browser --port=8093 --NotebookApp.token='' --NotebookApp.password=''"]




