FROM python:latest
COPY requirements.txt ./
RUN pip install requests
WORKDIR /usr/app/src
COPY main.py ./
CMD ["python", "./main.py", "logfilename.txt", "10.0.2.42"]

# docker build -t test -f .\Dockerfile.dockerfile .
# docker run test