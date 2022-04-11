FROM orgoro/dlib-opencv-python
COPY . /usr/face-app/

WORKDIR /usr/face-app/
RUN pip install -r requirements.txt
CMD gunicorn --bind 0.0.0.0:$PORT wsgi 