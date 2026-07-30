from app import app


def get_client():
    app.testing = True
    return app.test_client()


def test_home():
    client = get_client()
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.get_json()["message"] == "Hello from the Jenkins demo app!"


def test_health():
    client = get_client()
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json()["status"] == "ok"


def test_greet():
    client = get_client()
    resp = client.get("/api/greet/Muneeb")
    assert resp.status_code == 200
    assert resp.get_json()["message"] == "Hello, Muneeb!"
