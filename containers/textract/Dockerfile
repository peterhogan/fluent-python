FROM python:3-onbuild
RUN apt-get update -y &&\
    apt-get install -y libpulse-dev libav-tools python-dev libxml2-dev libxslt1-dev antiword unrtf poppler-utils pstotext tesseract-ocr flac lame libmad0 libsox-fmt-mp3 sox libjpeg-dev swig &&\
    pip3.6 install textract
