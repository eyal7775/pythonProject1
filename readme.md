# Requirements
  * Python 3.10

# How to run program in docker
### Implenents the next commands:
* docker build . -t [image_name] -f Dockerfile.dockerfile
* docker run -v $PWD/[log_file_name]:/usr/app/src/[log_file_name] [image_name] -f [log_file_name] -e [ip_server]

# Arguments to requried
* image_name - the name of image of container
* log_file_name - the name of file that docker is write
* ip_server - number of ip server

# Example to run
### write to command line:
* docker build . -t test -f Dockerfile.dockerfile
* docker run -v $PWD/logfilename.txt:/usr/app/src/logfilename.txt test -f logfilename.txt -e 10.0.2.42