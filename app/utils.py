import requests
import os

API_URL = "https://api-inference.huggingface.co/models/dandelin/vilt-b32-finetuned-vqa"
API_KEY = os.getenv("your_API_KEY")
headers = {"Authorization": f"Bearer {API_KEY}"}

def query_huggingface_api(image_path, question):
    with open(image_path, "rb") as image_file:
        files = {"image": image_file}
        data = {"inputs": {"question": question}}
        response = requests.post(API_URL, headers=headers, files=files, json=data)

    if response.status_code == 200:
        return response.json()
    else:
        return {"answer": "No answer found"}
