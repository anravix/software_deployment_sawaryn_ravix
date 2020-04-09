import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Vectors_SP-MelanieSawaryn-AnneRavix", # Replace with your own username
    version="0.0.3",
    author="Melanie Sawaryn - Anne Ravix",
    author_email="melanie.sawaryn@insa-lyon.fr",
    description="Manipulation of vectors and strings",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/anravix/software_deployment_sawaryn_ravix.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
