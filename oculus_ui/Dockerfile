# app/Dockerfile

FROM python:3.8

WORKDIR /app
COPY  . /app

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y --no-install-recommends \
    libopencv-dev \
    python3-opencv \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN pip install --upgrade pip

RUN pip3 install -r requirements.txt
EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
