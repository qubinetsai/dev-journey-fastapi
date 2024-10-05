# FastAPI Example Application

Project implements a basic user registration and greeting system.

## FastAPI Structure

 1. app/: Main application directory.
    - __init__.py: Makes `app` a package.
    - main.py: Entry point of the application, where FastAPI instance is created and routes are included.
    - config/: Configuration settings for the application (e.g., database connection, environment variables). 
    - models/: Directory for database models. 
    - routes/: Directory for route definitions.
    - schemas/: Directory for Pydantic models (data validation and serialization)
    - services/: Directory for business logic and service functions.
    - tests/: Directory for test files.
    - utils/: Directory for utility functions and helpers.
 2. .gitignore: Git ignore file to exclude unnecessary files from version control.
 3. requirements.txt: List of dependencies for the project.
 4. README.md: Project documentation.

## Running the Project

Set Up Virtual Environment (Optional but recommended)

```shell
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Run the Application

```shell
uvicorn app.main:app --reload
```

Access the Application

```shell
curl -X 'POST' \
  'http://127.0.0.1:8000/users/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "username": "testuser",
  "email": "testuser@example.com"
}'
```
```shell
curl -X GET "http://127.0.0.1:8000/"
```

Deactivate the Virtual Environment

```shell
deactivate
```

## Steps to Build and Run the Docker Image

 1. Build the Docker Image:

```shell
docker build -t dev-journey-fastapi .
```

 2. Run the Docker Container:

```shell
docker run -d -p 8000:80 --name dev-journey-fastapi dev-journey-fastapi
```

The Application can be tested with above `curl` commands.

 3. Stopping and Removing the Docker Container:

```shell
docker stop dev-journey-fastapi
docker rm dev-journey-fastapi
```

## Helm chart

Application can be deployed using the helm chart located in `charts/dev-journey-fastapi` directory.
Apply the Helm chart:

```shell
helm install dev-journey-fastapi charts/dev-journey-fastapi \
--set imageCredentials.username=<username> \
--set imageCredentials.password=<password>
```

## Qubes contributions

In order to add the new application to Qubinets inventory the files located in qubes-contributions need to be commited
to Gitlab branch https://gitlab.com/qubes-contributions/qubes-contributions and merge request to be opened. Once the 
merge request is approved by Qubinets team the new Qube will be visible in Qubinets inventory. Before commiting the
files following prerequisites need to be checked:

    1. Ensure qube.yaml has the correct "version" and "repo" settings
    2. Ensure values.yaml has the correct "repository" settings

The Qubes-contribiutions README also contains detail information how to expand the basic configuration with connections 
and extra parameters.