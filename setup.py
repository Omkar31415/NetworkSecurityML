'''
The setup.py is an essential part of packaging and distributing Python projects. it is used by setuptools
(or distutils in older python versions) to define the configuration
of your project, such as its metadata, dependencies, and more.
'''

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    '''
    This function will return list of requirements
    '''
    requirement_lst=[]
    try:
        with open('requirements.txt','r') as file:
            #Read lines from the file
            lines=file.readlines()
            #process each line
            for line in lines:
                #ignore empty lines and -e .
                requirement=line.strip()
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print('requirements.txt file not found')
    
    return requirement_lst

setup(
    name='Network Security',
    version='0.0.1',
    author='Omkar Datta Sowri',
    author_email='vullaganti.omkar.4@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)
