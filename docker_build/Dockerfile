FROM python:3
WORKDIR /docker_build
COPY ../Vectors_SP.py  docker_build/Vectors_SP.py
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps "Vectors_SP-MelanieSawaryn-AnneRavix"
ADD test.py /
CMD ["python", "../test.py"]
