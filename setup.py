from setuptools import find_packages,setup
from typing import List

HYPEN_E_DASH = '-e .'
def get_requirements(file_path):
    """ This function will return the list of requirements """
    with open(file_path) as f:
        req = f.readlines()
        req = [i.replace("\n", "") for i in req]
        if HYPEN_E_DASH in req:
            req.remove(HYPEN_E_DASH)
    return req

setup(
  name="IdeoScore",
  version="0.0.1",
  author="Daxil Modi",
  author_email="daxmodi8521@gmail.com",
  packages=find_packages(),
  install_requires=get_requirements('requirements.txt'),
)
