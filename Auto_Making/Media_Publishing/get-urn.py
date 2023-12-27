import requests
import json

url = "https://api.linkedin.com/v2/userinfo"

headers = {
    'Authorization': 'Bearer AQXzcgGB3TifJTSzrd0PpP-V4xKAxG6YxC26fhVcrXh5VfMo4vULkHD1w19KB3U7pkJQra8jO6CkIrY8TKdI7GdD5x3738eSBLd_O8ESbNaFQDWSgHjPCnqOmldABE2aM84CyugKZ4HpZM8_L4-zZy4j9YAECr4608klJFaLVqshAJ5CYQHdNdxs6ym7KPXaD7e8oJhOOyOABwhuJ83gqU_IzWMUtHVXHQpcjSvivKrtYT7-ONqUxoKhoQPQrnSpb5P1XqvlH7k7Oz6d216Kiznz3yVAT0mORn0t1ZOG7RKuSw6GpDZ-a_vd_RoPFRnhNjkfXAJEVJyZ3K9BpmCkoc1W6Vkaxw',
    'X-Restli-Protocol-Version': '2.0.0'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    user_data = response.json()
    print(json.dumps(user_data, indent=2))
else:
    print(f"Error: {response.status_code} - {response.text}")
