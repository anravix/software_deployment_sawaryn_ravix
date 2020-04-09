FROM ubuntu

RUN apt-get update && apt-get install -y python-pip

RUN pip install --upgrade setuptools

RUN pip install numpy

WORKDIR /docker_build
COPY test.py  docker_build/test.py
RUN  pip install -i https://test.pypi.org/simple/ Vectors-SP-MelanieSawaryn-AnneRavix==0.0.3

CMD ["python", "../test.py"]
