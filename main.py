import requests

url = "https://i.stack.imgur.com/oeCG3.jpg"

response = requests.get(url)

# wb because it is not text but it is a binary file
with open("insurgent.jpg","wb") as file:
    file.write(response.content)




