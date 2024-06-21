FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    libatlas-base-dev \
    libjasper-dev \
    libqtgui4 \
    libqt4-test \
    libhdf5-dev \
    libhdf5-serial-dev \
    libhdf5-103 \
    libqtwebkit4 \
    libilmbase23 \
    libopenexr23 \
    libgstreamer1.0-0 \
    gstreamer1.0-tools \
    gstreamer1.0-plugins-base \
    gstreamer1.0-plugins-good \
    gstreamer1.0-plugins-bad \
    gstreamer1.0-plugins-ugly \
    libgstreamer-plugins-base1.0-dev \
    v4l-utils \
    python3-picamera \
    python3-opencv \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY . /app
COPY . /picam.py
WORKDIR /app
RUN pip install -r requirements.txt

CMD ["python", "picam.py"]
