# jenkins-python-demo

A small Flask app used as a test subject for a Jenkins pipeline (build → test → lint → docker build → push/deploy).

## Structure
```
jenkins-python-demo/
├── app.py            # Flask app
├── tests/
│   ├── conftest.py   # lets tests/ import app.py from project root
│   └── test_app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
└── README.md
```

## Endpoints
- `GET /` — sample message
- `GET /health` — health check
- `GET /api/greet/<name>` — greeting

## Local run
```
pip install -r requirements.txt
python app.py
```

## Test / lint
```
pytest
flake8 app.py tests/ --max-line-length=100
```

## Docker
```
docker build -t jenkins-python-demo .
docker run -p 5000:5000 jenkins-python-demo
```
