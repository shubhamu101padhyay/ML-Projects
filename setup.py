from setuptools import find_packages,setup
from typing import List

hype_e='-e.'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requiements 
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]
        if hype_e in requirements:
            requirements.remove(hype_e)
    return requirements
setup(
name='MLproject',
version='0.0.1',
author='Shubham',
author_email='shubham101upadhyay@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)