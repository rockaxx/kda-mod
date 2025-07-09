import os
import requests

BASE_URL = "https://ariaom.com/spacemap/ships/surgeon/"
TARGET_DIR = r"C:\Users\rocka\Desktop\mod\spacemap\spacemap\ships\surgeon"

os.makedirs(TARGET_DIR, exist_ok=True)

for i in range(0, 65):
    file_name = f"{i}.webp"
    url = BASE_URL + file_name
    local_path = os.path.join(TARGET_DIR, file_name)
    print(f"Downloading: {url} -> {local_path}")
    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            with open(local_path, 'wb') as f:
                f.write(r.content)
        else:
            print(f"Failed to download {url}: {r.status_code}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")
