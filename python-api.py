import requests

# Read name from file
with open('input.txt', 'r') as f:
    name = f.read().strip()

# Call API
url = f'https://api.agify.io?name={name}'
response = requests.get(url)

# Check & print result
if response.status_code == 200:
    data = response.json()
    print(f"Predicted age for {name}: {data['age']}")
else:
    print("API request failed:", response.status_code)
