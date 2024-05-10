from setuptools import find_packages,setup
from typing import List



# write function for requirement file
def get_requirements(file_path:str)->List[str]:  #file_path is my file path , all inside in string format , file returns string
    requirements=[] # created list
    with open(file_path) as file_obj:
        requirements=file_obj.readlines() # reading line in requirements
        requirements=[req.replace("\n","") for req in requirements] #replacing new line with blank as in requirements.txt,detecting /n but we replacing with space so after pandas space numpy like that it will take
    return requirements

# setup project

setup(
    name='DiamondPricePrediction',  # name of project
    version='0.0.1' , # for another version can give another number to distinguish while release
    author='VB',
    author_email='VB@gmail.com',
    #requires=['pandas','sklearn'] OR call function
    requires=get_requirements('requirements.txt'), # call get_requirements fuction here
    find_packages=find_packages()
)
