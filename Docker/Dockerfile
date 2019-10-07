FROM python:3.6.1-alpine
WORKDIR /app
COPY  PythonContainer/* ./PythonContainer/
WORKDIR /app/PythonContainer
RUN pip install -r requirements.txt
EXPOSE 80
RUN chmod +x ./app.py
ENTRYPOINT ["./app.py", "80"]
