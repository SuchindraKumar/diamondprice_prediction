from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'


def get_reqirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)


    return requirements    




setup(
    name='Regressorproject',
    version='0.0.1',
    author='Suchindra Kumar',
    author_email='suchindra057@gmail.com',
    install_requires=get_reqirements('requirements.txt'),
    packages=find_packages()


)

