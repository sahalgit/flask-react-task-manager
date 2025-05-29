Flask + React Task Manager

A simple full-stack task management application built with:

- **Flask** (Python) as the backend
- **PostgreSQL** as the database
- **React** as the frontend
- **Docker Compose** for container orchestration


Features

- Add, view, and delete tasks
- RESTful API using Flask
- PostgreSQL integration
- React UI with Axios for API communication
- Dockerized for easy deployment

Tech Stack

- Backend: Python, Flask, psycopg2, flask-cors
- Frontend: React, Axios
- Database: PostgreSQL
- DevOps: Docker, Docker Compose

Setup Instructions:-

1. Clone the repo

"git clone https://github.com/sahalgit/flask-react-task-manager.git"
"cd flask-react-task-manager"

2. Start the full stack app

"docker-compose up --build"

Flask app runs at: http://localhost:5000
React frontend runs at: http://localhost:3000

3. Testing

Visit http://localhost:3000 in your browser to use the frontend.
Add or delete tasks using the UI.
Or, test the API directly using curl or Postman

" curl -X POST http://localhost:5000/tasks -H "Content-Type: application/json" -d '{"task": "Test"}' "

---Project Structure---

flask-react-task-manager/
├── app/                  # Flask backend
│   ├── app.py
│   ├── requirements.txt
│   └── templates/
│       └── index.html
├── client/               # React frontend
│   ├── src/
│   │   └── App.js
│   └── ...
├── docker-compose.yml
├── Dockerfile
└── README.md
