from python:3.6.1

COPY . .

RUN pip install pytest-runner & pip install -r requirements.txt

EXPOSE 5000

entrypoint ["python", "server.py"]