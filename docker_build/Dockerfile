FROM ubuntu

RUN apt-get update && apt-get install -y python3-pip



RUN pip3 install --upgrade setuptools

RUN pip3 install numpy

WORKDIR /docker_build
COPY test.py  docker_build/test.py
RUN  pip3 install -i https://test.pypi.org/simple/ Vectors-SP-MelanieSawaryn-AnneRavix==0.0.3

CMD ["python3", "docker_build/test.py"]
