import requests
from PIL import Image
image_url = 'https://github.com/i3hsInnovation/resources/blob/master/images/puss_in_boots.jpg?raw=true'
response = requests.get(image_url)
if response.status_code == 200:
    with open("image.jpg", "wb") as f:
        f.write(response.content)
img = Image.open("image.jpg")
img.show()