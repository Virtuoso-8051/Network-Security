''' setup.py file is essential for packaging and distributing Python projects. It contains metadata about the project, such as its name, version, author, and dependencies. The setup.py file is used by tools like pip to install the package and its dependencies. It can also include additional information like entry points for command-line scripts, classifiers for categorizing the project, and other configuration options. Overall, setup.py is a crucial component for managing and sharing Python projects effectively. '''
# setup file is essential part of packaging


from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]: # this fn will return list of requirements
    requirement_lst:List[str] = []
    try:
        with open('requirements.txt','r') as file:
            lines = file.readlines() #read lines from requirements.txt file
            for line in lines: # process each line
                requirement = line.strip()
                if requirement and requirement!= '-e .': # ignore empty lines and -e. (end of file)
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")
    
    return requirement_lst

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Anurag Raj",
    author_email="rajanurag1508@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)

