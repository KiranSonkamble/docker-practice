FROM python:3.9-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirments.txt
CMD [ "python","app.py"]