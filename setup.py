import os
from setuptools import setup, find_packages

def get_requirements(file_path:str)->list[str]:
    '''
    this function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace('\n','') for req in requirements]
    requirements

setup(
    name = "mlproject",
    version = "0.0.4",
    author = "Amrit",
    author_email = "amrit.nt.9@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements('requirement.txt'),
)