# Library Management Repository

A Python backend using FastAPI and Docker, designed for full-stack applications. This system provides features such as adding, editing, and deleting books, user checkouts, and tracking checked-out users.

## Getting Started

### 1. Running the App on Your Local Machine

Follow these steps to set up and run the application on your local machine:

#### 1.1 Clone the Repository

```bash
https://github.com/SiddharthChavan23/LibSysRepository.git
cd LibSysRepository
```

#### 1.2 Create a Virtual Environment

```bash
python -m venv env
```

#### 1.3 Activate the Virtual Environment

On Windows:

```bash
venv\Scripts\activate
```

On Linux or macOS:

```bash
source venv/bin/activate
```

#### 1.4 Install Dependencies

```bash
pip install -r requirements.txt
```

#### 1.5 Run the Application

```bash
uvicorn index:app --reload
```

The FastAPI application should now be accessible at [http://localhost:8000](http://localhost:8000) on your local machine. You can use [http://localhost:8000/docs](http://localhost:8000/docs) to check the API usage.
![image](https://github.com/SiddharthChavan23/LibSysRepository/assets/88672777/57e04864-01d9-43b3-859e-7ec1b9410758)

