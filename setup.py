from setuptools import find_packages, setup
from typing import List

''' Created function to return list of requirements '''
HYPEN_E_DOT="typing -e ."
def get_requirements(file_path:str)->List[str]: # type: ignore
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='Github_setup',
    version='0.0.1',
    author='Ram',
    author_email='dnshram013@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)