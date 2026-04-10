from setuptools import setup , find_packages

#read line by line store into single veriable "requirements"
with open("requirements.txt") as f:
    requirements =f.read().splitlines()



setup(
    name="MLOps project",
    version="0.1",
    author="vigneshwaran",
    packages=find_packages(),
    install_requires=requirements,
)