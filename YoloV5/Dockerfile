FROM python:3.8

WORKDIR /app

RUN apt-get update && \
    apt-get install -y && \
    apt-get -y install python3-pip && \
    apt-get install git-all -y && \
    apt install libgl1
RUN git clone https://github.com/ultralytics/yolov5.git
RUN cd yolov5 && \
    python3 -m pip install -r requirements.txt
RUN rm -rf /var/lib/apt/lists/*

RUN pip install jupyter

COPY . .

EXPOSE 8095
EXPOSE 8085

CMD ["bash", "-c","jupyter notebook --ip=0.0.0.0 --allow-root --no-browser --port=8095 --NotebookApp.token='' --NotebookApp.password=''"]
