import pytest
from movies_catalogue import tmdb_client


def test_get_single_movie(monkeypatch):
    mock_data = {"id": 123, "title": "Test Movie"}

    class MockResponse:
        def raise_for_status(self):
            pass

        def json(self):
            return mock_data

    def requests_get_mock(url, headers):
        assert url == "https://api.themoviedb.org/3/movie/123"
        assert "Authorization" in headers
        return MockResponse()

    monkeypatch.setattr(
        "movies_catalogue.tmdb_client.requests.get",
        requests_get_mock
    )

    result = tmdb_client.get_single_movie(123)
    assert result == mock_data


def test_get_single_movie_empty(monkeypatch):
    mock_data = {}

    class MockResponse:
        def raise_for_status(self):
            pass

        def json(self):
            return mock_data

    monkeypatch.setattr(
        "movies_catalogue.tmdb_client.requests.get",
        lambda *a, **kw: MockResponse()
    )
    result = tmdb_client.get_single_movie(999)
    assert result == {}


def test_get_single_movie_raises(monkeypatch):
    class MockResponse:
        def raise_for_status(self):
            raise Exception("API error")

    monkeypatch.setattr(
        "movies_catalogue.tmdb_client.requests.get",
        lambda *a, **kw: MockResponse()
    )
    with pytest.raises(Exception):
        tmdb_client.get_single_movie(111)


def test_get_single_movie_cast(monkeypatch):
    mock_cast = [{"name": "Actor 1"}, {"name": "Actor 2"}]
    mock_data = {"cast": mock_cast}

    class MockResponse:
        def raise_for_status(self):
            pass

        def json(self):
            return mock_data

    def requests_get_mock(url, headers):
        assert url == "https://api.themoviedb.org/3/movie/123/credits"
        return MockResponse()

    monkeypatch.setattr(
        "movies_catalogue.tmdb_client.requests.get",
        requests_get_mock
    )
    cast = tmdb_client.get_single_movie_cast(123)
    assert cast == mock_cast


def test_get_single_movie_cast_empty(monkeypatch):
    mock_data = {"cast": []}

    class MockResponse:
        def raise_for_status(self):
            pass

        def json(self):
            return mock_data

    monkeypatch.setattr(
        "movies_catalogue.tmdb_client.requests.get",
        lambda *a, **kw: MockResponse()
    )
    cast = tmdb_client.get_single_movie_cast(456)
    assert not cast


def test_get_movie_images(monkeypatch):
    mock_images = {
        "backdrops": [{"file_path": "/abc.jpg"}],
        "posters": [{"file_path": "/poster.jpg"}]
    }

    class MockResponse:
        def raise_for_status(self):
            pass

        def json(self):
            return mock_images

    def requests_get_mock(url, headers):
        assert url == "https://api.themoviedb.org/3/movie/123/images"
        return MockResponse()

    monkeypatch.setattr(
        "movies_catalogue.tmdb_client.requests.get",
        requests_get_mock
    )

    images = tmdb_client.get_movie_images(123)
    assert images == mock_images
    assert "backdrops" in images
    assert "posters" in images


def test_get_movie_images_empty(monkeypatch):
    mock_data = {"backdrops": [], "posters": []}

    class MockResponse:
        def raise_for_status(self):
            pass

        def json(self):
            return mock_data

    monkeypatch.setattr(
        "movies_catalogue.tmdb_client.requests.get",
        lambda *a, **kw: MockResponse()
    )
    images = tmdb_client.get_movie_images(789)
    assert not images["backdrops"]
    assert not images["posters"]



   



