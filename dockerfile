FROM python:3
WORKDIR /app
COPY . /app
RUN pip install --upgrade pip
EXPOSE 5000
CMD ["python" , "app.py"]

