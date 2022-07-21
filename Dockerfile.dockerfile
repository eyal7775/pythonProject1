# on linux - /mnt/linux/c/Users/eyal999/PycharmProjects/pythonProject1/
# on Windows - C:\Users\eyal999\PycharmProjects\pythonProject1

FROM python:latest
COPY requirements.txt ./
RUN pip install -r requirements.txt
WORKDIR /usr/app/src
COPY main.py ./
ENV TZ="Asia/Jerusalem"
ENTRYPOINT ["python", "./main.py"]

# docker build -t test -f .\Dockerfile.dockerfile .
# docker run -v $PWD/logfilename.txt:/usr/app/src/logfilename.txt test logfilename.txt 10.0.2.42
