FROM python:3.8
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN python setup.py install
CMD ["python"]