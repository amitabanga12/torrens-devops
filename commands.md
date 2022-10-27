# Steps:


### 1. Create virtual environment
``` 
python3 -m venv venv 
```
_venv is the environment name. Command :  ```python -m venv <environment_name>```_


### 2. Activate virtual environment (Everytime you run the application)
**Command**: 

For windows
``` 
<environment_name>\Scripts\activate 
``` 

For linux
```
source ./<environment_name>/bin/activate 
``` 

**Example**: 
 ``` 
 source ./venv/bin/activate 
 ```


### 3. Install dependencies
``` 
pip install -r requirements.txt 
```
_We define all dependencies that are required in our project in requirements.txt_


### 4. Create project folder
``` 
mkdir devops-a2 
```


### 5. Select project folder
``` 
cd devops-a2 
```

### 6. Start project
``` 
django-admin startproject devops_project
```


### 7. Running the project
**Command**: 
``` 
cd <project_name>
python manage.py runserver 
```
**Example**:
``` 
cd devops_project
python manage.py runserver 
```
**OR**
``` 
cd devops_project
python manage.py runserver 8080
```

_By now, we have built a basic django website. Now we need to add features to it_

### 8. Run admin page or create super user
``` 
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
```
_Enter username, email and password to create super user_

### 8. Start app
**Command**: 
``` 
python manage.py startapp <app_name> 
```

**Example**: 
``` 
python manage.py startapp userauth 
```

