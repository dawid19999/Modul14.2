
import requests

API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhZGY1ZjU5ZGZjNzk1ZjgxNmUxYzM0NmFjYjZiNjVkNiIsIm5iZiI6MTc1MjU5Nzk4MS41LCJzdWIiOiI2ODc2ODVkZDdjYzI4MmQwODQ3MzMzODMiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.HMc5GqxsiBbX3uBX_IqCvEQoKPqgvrl3d5rEEXSEKlY"

MOVIE_LISTS = [
    "popular",
    "now_playing",
    "top_rated",
    "upcoming"
]

def check_api_token():
    if not API_TOKEN:
        raise ValueError("Brak API_TOKEN. Ustaw prawidłowy klucz w zmiennej API_TOKEN.")
    print("API_TOKEN jest ustawiony i gotowy do użycia.")

def get_movies_list(list_type="popular"):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Accept": "application/json"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json().get("results", [])

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Accept": "application/json"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()

def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Accept": "application/json"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json().get("cast", [])


def get_movie_images(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Accept": "application/json"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()
