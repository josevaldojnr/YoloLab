FROM python:3.8-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    python3-opencv \
    x11-apps \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libopencv-dev

RUN pip install notebook

RUN pip install torch==1.7.1 torchvision==0.8.2

RUN pip install opencv-python

COPY . .

EXPOSE 8095
EXPOSE 8085

CMD ["bash", "-c","jupyter notebook --ip=0.0.0.0 --allow-root --no-browser --port=8095 --NotebookApp.token='' --NotebookApp.password=''"]



