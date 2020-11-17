# Container image that runs your code
FROM ubuntu:18.04

RUN apt-get update \
    && apt-get install -y \
    build-essential \
    python3-pip \
    python3.8 \
    git \
    && python3 -m pip install --upgrade pip \
    && python3 -m pip install --upgrade setuptools \
    && python3 -m pip install --upgrade wheel \
    && python3 -m pip install git+https://github.com/OpenAstronomy/baldrick#egg=baldrick

# Copies code file action repository to the filesystem path `/` of the container
COPY entrypoint.sh /entrypoint.sh

COPY check_milestone.py /check_milestone.py

# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["/entrypoint.sh"]
