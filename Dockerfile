FROM orgoro/dlib-opencv-python
COPY . /usr/face-app/
EXPOSE 5001
WORKDIR /usr/face-app/
RUN pip install -r requirements.txt
CMD gunicorn main:app