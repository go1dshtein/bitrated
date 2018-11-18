FROM python:3.7.1-stretch
RUN apt-get update && apt-get upgrade -y && apt-get install -y build-essential python-dev
RUN pip install --upgrade pip setuptools wheel
RUN mkdir /tmp/source
COPY . /tmp/source
RUN cd /tmp/source && python3 ./setup.py install
ENTRYPOINT ["/usr/local/bin/bitrated.py"]
