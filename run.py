import os
from sys import platform

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
ENVIRONMENT_NAME = 'python_venv'

virtual_env_path = "{}/{}".format(BASE_DIR, ENVIRONMENT_NAME)
print("virtual environment path: ", virtual_env_path)

try:
    
    os.system("which python")
    
    # Check if virtual environment already created
    is_venv_created = os.path.isdir(virtual_env_path)
    print('is_venv_created', is_venv_created)
    
    # If virtual environment is not created, create virtual environment, outside project folder
    if not is_venv_created:
        print("Creating virtual environment")
        os.system("python3 -m pip install --user virtualenv")
        os.system("python3 -m venv {}".format(virtual_env_path))
    
    # Activate virtual environment
    print("platform", platform)
    activate_file_path = None
    if platform == 'win32' or platform == 'cygwin':
        activate_file_path = "{}\Scripts\activate.bat".format(virtual_env_path)
        os.system('{}'.format(activate_file_path))
    else:
        activate_file_path = "{}/bin/activate".format(virtual_env_path)
        os.system('. {}'.format(activate_file_path))
    print("activate file path: ", activate_file_path)
        
    # Install dependencies in virtual environment
    os.system("pip install -r requirements.txt")
    
    # Run Project
    os.system("python3 devops-a2/devops_project/manage.py runserver 8081")
        
except OSError as error :
    print(error)


