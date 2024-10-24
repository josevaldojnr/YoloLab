
FROM python:3.9

WORKDIR /app

RUN apt-get update && apt-get install -y \
    python3-opencv \
    x11-apps \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libopencv-dev

RUN pip install notebook

RUN pip install torch==1.8.0 torchvision==0.9.0

RUN pip install opencv-python

COPY . .

EXPOSE 8111
EXPOSE 8112



CMD ["bash", "-c","jupyter notebook --ip=0.0.0.0 --allow-root --no-browser --port=8111 --NotebookApp.token='' --NotebookApp.password=''"]




