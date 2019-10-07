FROM python:3.7-alpine3.9
WORKDIR /app
COPY  PythonContainer/* ./
RUN pip install -r requirements.txt
# Standard set up Nginx finished
EXPOSE 80
# # Expose 443, in case of LTS / HTTPS
EXPOSE 443
RUN chmod +x ./app.py
CMD [ "python", "./app.py", "80" ]