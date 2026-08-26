import requests

data = {
    "word": "python"
}
url = 'http://127.0.0.1:5000/Word'

response = requests.post(
    url,
    json=data
)
