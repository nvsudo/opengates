from fastapi.testclient import TestClient

from opengates_cc.app import create_app


def test_demo_intake_renders_topics(monkeypatch, tmp_path) -> None:
    monkeypatch.setenv("OPENGATES_CC_DATA_DIR", str(tmp_path / "data"))
    client = TestClient(create_app())

    response = client.get("/demo")
    assert response.status_code == 200
    assert "Investor Desk" in response.text
    assert "Start conversation" in response.text
    assert "Applied AI with real user pull" in response.text


def test_thread_create_and_view(monkeypatch, tmp_path) -> None:
    monkeypatch.setenv("OPENGATES_CC_DATA_DIR", str(tmp_path / "data"))
    client = TestClient(create_app())

    create = client.post(
        "/g/demo-investor/threads",
        data={
            "name": "Founder",
            "email": "founder@example.com",
            "topic": "Applied AI with real user pull",
            "content": "We are building an AI startup for finance teams.",
        },
        follow_redirects=False,
    )
    assert create.status_code == 303
    location = create.headers["location"]

    page = client.get(location)
    assert page.status_code == 200
    assert "Topic: Applied AI with real user pull" in page.text
    assert "You" in page.text
