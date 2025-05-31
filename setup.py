from setuptools import find_packages, setup
from typing import List

#this function returns all packages etc in requiremnets.txt
def get_requirements(file_path:str) -> List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n',"") for req in requirements]

    return requirements







setup(
    name='Data Science Project',
    author='pallavi',
    version='0.0.1',
    author_email='pallavipalthya@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)