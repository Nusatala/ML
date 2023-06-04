import requests

response = requests.post("http://localhost:5000/",
                         files={"file": open("3_bonang.jpg", "rb")})

print(response.json())
