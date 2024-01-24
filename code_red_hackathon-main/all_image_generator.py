import base64
import requests
import os
import re
from paragraphs_array import paragraphs
def img_generator(para,z):  
    url = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image"

    body = {
    "steps": 40,
    "width": 1024,
    "height": 1024,
    "seed": 0,
    "cfg_scale": 5,
    "samples": 1,
    "text_prompts": [
        {
        "text": para,
        "weight": 1
        },
        {
        "text": "blurry, bad",
        "weight": -1
        }
    ],
    }

    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Bearer sk-xa4iMtaL2mPqH7qMAoXnbVoeiVFMCpqObzVOgXI791RoCnDv",
    }

    response = requests.post(
    url,
    headers=headers,
    json=body,
    )

    if response.status_code != 200:
        raise Exception("Non-200 response: " + str(response.text))

    data = response.json()
    if not os.path.exists("./images"):
        os.makedirs("./images")
    for i, image in enumerate(data["artifacts"]):
        with open(f'./images/img_{z}.png', "wb") as f:
            f.write(base64.b64decode(image["base64"]))

'''
with open("generated_text.txt", "r") as file:
    text = file.read()
#paragraphs = text.splitlines()
paragraphs = [para.strip() for para in text.splitlines() if para.strip()]
'''
#print(len(paragraphs))
#paragraphs = re.split(r"[,.]", text)
os.makedirs("images",exist_ok=True)
z=0

for para in paragraphs:
    z+=1
    img_generator(para,z)
