# Library Management Repository

A Python backend using FastAPI and Docker, designed for full-stack applications. This system provides features such as adding, editing, and deleting books, user checkouts, and tracking checked-out users.

## Getting Started

# 1.Running FastAPI Application as a Docker Container

1. **Login to Docker:**

    ```bash
    docker login -u "<username>" -p "<password>" docker.io
    ```

    Replace `<username>` and `<password>` with your Docker Hub credentials.

2. **Pull the Docker Image:**

    ```bash
    docker pull siddharthc23/backendapi:backendapi
     ```

3. **Run the Docker Container:**

    ```bash
    docker run -d -p 8080:80 siddharthc23/backendapi:backendapi
    ```

    This command will start the FastAPI application in a Docker container, mapping port 8000 on your local machine to port 80 inside the container.

4. **Access the FastAPI Application:**

    Open your web browser and navigate to [http://localhost:8000](http://localhost:8000) to interact with the FastAPI application. For detailed API documentation, visit [http://localhost:8000/docs](http://localhost:8000/docs).

### 2.Architecture and Flow 

![image](https://github.com/SiddharthChavan23/LibSysRepository/assets/88672777/f7dbcd40-e1f3-480f-85fa-3a0f11c9a515)

### 3.Database Schema

![image](https://github.com/SiddharthChavan23/LibSysRepository/assets/88672777/693f2219-7d7b-4d4b-a1c7-2732ee2c781a)

### 4. Running the App on Your Local Machine

Follow these steps to set up and run the application on your local machine:

#### 4.1 Clone the Repository

```bash
https://github.com/SiddharthChavan23/Library-Management.git
cd Library-Management
```

#### 4.2 Create a Virtual Environment

```bash
python -m venv env
```

#### 4.3 Activate the Virtual Environment

On Windows:

```bash
venv\Scripts\activate
```

On Linux or macOS:

```bash
source venv/bin/activate
```

#### 4.4 Install Dependencies

```bash
pip install -r requirements.txt
```

#### 4.5 Run the Application

```bash
uvicorn index:app --reload
```

The FastAPI application should now be accessible at [http://localhost:8000](http://localhost:8000) on your local machine. You can use [http://localhost:8000/docs](http://localhost:8000/docs) to check the API usage.









