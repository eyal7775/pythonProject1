FROM python:latest
COPY requirements.txt ./
RUN pip install -r requirements.txt
WORKDIR /usr/app/src
COPY main.py ./
RUN ["python", "./main.py", "logfilename.txt", "10.0.2.42"]
CMD cat logfilename.txt

# docker build -t test -f .\Dockerfile.dockerfile .
# docker run test