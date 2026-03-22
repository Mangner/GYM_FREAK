from __future__ import annotations

from fastapi.testclient import TestClient


def test_create_and_fetch_parties(client: TestClient) -> None:
    person_payload = {
        "first_name": "Test",
        "last_name": "User",
        "gender": "OTHER",
        "birth_date": "2000-01-01",
        "username": "tester",
        "email": "test@example.com",
    }
    person_response = client.post("/people/", json=person_payload)
    assert person_response.status_code == 201
    person_data = person_response.json()
    person_id = person_data["id"]

    org_payload = {
        "name": "Test Group",
        "description": "A test org",
    }
    org_response = client.post("/organizations/", json=org_payload)
    assert org_response.status_code == 201
    org_data = org_response.json()
    org_id = org_data["id"]

    party_person_response = client.get(f"/parties/{person_id}")
    assert party_person_response.status_code == 200
    party_person_data = party_person_response.json()
    assert party_person_data["type"] == "PERSON"

    party_org_response = client.get(f"/parties/{org_id}")
    assert party_org_response.status_code == 200
    party_org_data = party_org_response.json()
    assert party_org_data["type"] == "ORGANIZATION"
