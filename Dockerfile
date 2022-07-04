FROM pytorch/pytorch:1.11.0-cuda11.3-cudnn8-runtime

RUN apt update
RUN apt-get install git wget ffmpeg libsm6 libxext6  -y

RUN pip install --upgrade pip

WORKDIR /api
COPY models-API .

RUN pip install -r requirements.txt
RUN chmod +x setup.sh
RUN bash setup.sh

EXPOSE 80

# ENTRYPOINT ls SwinIR
ENTRYPOINT python main.py