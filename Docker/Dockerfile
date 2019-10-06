FROM python:3.6.1-alpine
WORKDIR /app
COPY  PythonContainer/* ./PythonContainer/
WORKDIR /app/PythonContainer
RUN pip install -r requirements.txt
CMD ["python","app.py"]
