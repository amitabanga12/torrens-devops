# Django Application for processing csv files

This project processed csv files. It reads csv files. It also enables user to search records from csv files by filtering rows which makes it easier for processing files.

To login to the application, use following credentials for superuser:
``` 
username: admin
password: Banga@987
```

**feature-x**: This enables user to read a csv file and display it in table view which is easy to read. We are also implementing table filters for easy processing of csv file.

**feature-y**: This feature allows super user to add staff user who can only view the files. 

**feature-z**: This feature allows user to edit their profile and change password. 

# Prerequisites for running the code

1. Python 3.10.6
2. Pip 22.3
3. Web browser to test the application

# To Run the application

Execute following command

``` 
python run.py
``` 
Once command is run open http://localhost:8081/userauth/login/ on browser

**run.py** creates the virtual environment and activate it. Once virtual environment is activated, it runs manage.py script which configures django project

# To Run unit tests

Execute following command

``` 
python3 devops-a2/devops_project/manage.py test --traceback usermanager
``` 
