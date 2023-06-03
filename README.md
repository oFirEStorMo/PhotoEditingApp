# PhotoEditingApp

This guide will walk you through the steps to set up and run a Flask and React project from scratch. We'll assume that you don't have any dependencies installed on your system. Please follow the instructions below:

## Prerequisites

Before you begin, ensure that you have the following installed on your system:

- Python 3.11 or higher
- Node.js 18 or higher
- npm (Node Package Manager) 

## Setup Backend (Flask)

1. Clone the repository or download the project files.

2. Navigate to the server directory using the command line:
   ```
   cd server
   ```

3. Install pipenv if you haven't already:
   ```
   pip install pipenv
   ```

4. Install project dependencies using pipenv:
   ```
   pipenv install
   ```

5. Activate the virtual environment:
   ```
   pipenv shell
   ```

6. Start the Flask backend server:
   ```
   python app.py
   ```

## Setup Frontend (React)

1. Open a new command line window and navigate to the client directory:
   ```
   cd client
   ```

2. Install frontend dependencies using npm:
   ```
   npm install
   ```

3. Start the React development server:
   ```
   npm start
   ```

## Access the Application

Once both the Flask backend server and React development server are running, you can access the application in your web browser at `http://localhost:3000`. The React development server proxies requests to the Flask backend server automatically.


Remember to deactivate the virtual environment when you're finished:
```
exit
```

That's it! You now have a Flask and React project set up and running.