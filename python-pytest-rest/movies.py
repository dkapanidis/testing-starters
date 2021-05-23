import pytest
import requests

dataset = [
    ("Godfather", "Godfather II"),
]

@pytest.mark.parametrize("name, updated_name", dataset)
def test_movies_rest(name, updated_name):
    # create movie
    response = requests.post(
        f"http://localhost:8080/api/movies", json={'name': name})
    assert response.status_code == 201

    # update movie
    movie = response.json()
    movie["name"] = updated_name
    response = requests.put(
        f'http://localhost:8080/api/movies/{movie["ID"]}', json=movie)
    assert response.status_code == 200

    # get movie
    response = requests.get(f'http://localhost:8080/api/movies/{movie["ID"]}')
    assert response.json() == movie

    # delete movie
    response = requests.delete(
        f'http://localhost:8080/api/movies/{movie["ID"]}')
    response = requests.get(f'http://localhost:8080/api/movies/{movie["ID"]}')
    assert response.status_code == 404
    assert response.json() == {'error': 'record not found'}
