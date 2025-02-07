import os
import requests
import time
from io import BytesIO
from PIL import Image

def generate_image(prompt: str):
    IMAGE_API_KEY = os.getenv("IMAGE_API_KEY")
    if not IMAGE_API_KEY:
        print("Error: IMAGE_API_KEY not found in environment variables.")
        return None

    url = "https://api.bfl.ml/v1/flux-pro-1.1"
    headers = {
        "accept": "application/json",
        "x-key": IMAGE_API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "prompt": prompt,
        "width": 1024,
        "height": 1024,
        "guidance_scale": 1,
        "num_inference_steps": 50,
        "max_sequence_length": 512,
        "Safety Tolerance": 3,
    }
    
    # Sending the initial request to generate the image
    response = requests.post(url, headers=headers, json=payload).json()
    if "id" not in response:
        print("Error generating image:", response)
        return None
    
    request_id = response["id"]
    
    # Polling for the result
    while True:
        time.sleep(0.5)
        result = requests.get(
            "https://api.bfl.ml/v1/get_result",
            headers=headers,
            params={"id": request_id},
        ).json()
        
        status = result.get("status")
        if status == "Ready":
            if "result" in result and "sample" in result["result"]:
                image_url = result["result"]["sample"]
                image_response = requests.get(image_url)
                if image_response.status_code == 200:
                    image = Image.open(BytesIO(image_response.content))
                    return image
                else:
                    print("Error fetching the image from the URL.")
                    return None
            else:
                print("Error: No 'sample' key in result.")
                return None
        elif status == "Content Moderated":
            print("Image generation status: Content Moderated. Stopping generation.")
            break
        else:
            print(f"Image generation status: {status}")
    
    return None
