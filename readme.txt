### This is docker-01 guide.
1. Create "Dockerfile" file inorder to create docker image.
2. "app.py" and "requirment.txt" files are the common files for wev application develpment.

## How to create docker image
1. >> docker build -t <image_name> .
2. >> docker images
3. >> docker ps

# Run docker image
4. >>docker run -d -p 5000:5000 <image_name>

# Docker container running & created.

------------------------------------------------------------------
### How to create Environment for docker using python env 

# Option is to go to the project folder and type
>>  python -m venv env_name

# then all the necessory files will be created
>>  cd project_path
>>  dir

#  Thier will be a env_name folder in that scripts are imp
>>  project_path\env_name\Scripts\activate

#  to list all installed Python packages and their versions in the current environment. 
# It is commonly used to generate a list of dependencies for a project.
>> pip freeze

# how to install new lib
>>  pip install lib-name

# This command will create a file named 'requirements.txt' in 
# the current directory containing the list of installed packages and their versions.
>>  pip freeze > requirment.txt

# install all the required lib from the files
>>  python -m install requirent.txt
            ==== or =====
>>  pip install -r requirements.txt

#  How to uninstall the lib
>>  pip uninstall -r requirment.txt -y

#  check all the lib
>>  pip freeze

#  deactivate the env
>> deactivate
--------------------------------------------------------------------------------
working on Docker-02 ..
--------------------------------------------------------------------------------
THANK YOU!!